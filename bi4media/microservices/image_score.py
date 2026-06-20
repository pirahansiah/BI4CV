"""No-reference image quality assessment metrics.

Implements BRISQUE (MSCN), NIQE, PIQE, JPEG-Q, BLIINDS-II, CORNIA,
SSEQ, and FQADI feature extractors for blind image quality evaluation.
"""

from __future__ import annotations

from pathlib import Path
from typing import final

import cv2
import numpy as np


@final
class ImageQualityScorer:
    """Aggregates multiple no-reference IQA metrics into a single score."""

    IMAGE_EXTENSIONS: tuple[str, ...] = (
        ".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif", ".webp",
    )

    def calculate_mscn_coefficients(
        self,
        image: np.ndarray,
        kernel_size: int = 7,
        sigma: float = 1.166,
    ) -> np.ndarray:
        """Compute Mean Subtracted Contrast Normalized coefficients (BRISQUE)."""
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) / 255.0
        blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)
        blurred_sq = blurred * blurred
        sigma_map = np.sqrt(
            cv2.GaussianBlur(img * img, (kernel_size, kernel_size), sigma)
            - blurred_sq
            + 1e-10
        )
        return (img - blurred) / sigma_map

    def compute_niqe_features(self, image: np.ndarray) -> tuple[float, float]:
        """Compute NIQE natural scene statistics (mu, sigma)."""
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) / 255.0
        return float(np.mean(img)), float(np.std(img))

    def calculate_piqe_index(self, image: np.ndarray) -> float:
        """Compute PIQE local variance index."""
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) / 255.0
        return float(cv2.Laplacian(img, cv2.CV_64F).var())

    def estimate_jpeg_quality(self, image: np.ndarray) -> float:
        """Estimate JPEG compression quality (0-100)."""
        ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        y_channel = ycrcb[:, :, 0]
        dct = cv2.dct(np.float32(y_channel) / 255.0)
        zeros = float(np.sum(dct < 0.01))
        return 100.0 - (zeros / np.size(dct) * 100.0)

    def compute_bliinds_features(self, image: np.ndarray) -> float:
        """Compute BLIINDS-II DCT block variance score."""
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img_dct = cv2.dct(np.float32(img) / 255.0)
        block_size = 8
        h, w = img.shape
        blocks_variance: list[float] = []
        for i in range(0, h, block_size):
            for j in range(0, w, block_size):
                block = img_dct[i : i + block_size, j : j + block_size]
                blocks_variance.append(float(np.var(block)))
        return float(np.mean(blocks_variance))

    def extract_cornia_features(self, image: np.ndarray) -> np.ndarray:
        """Extract CORNIA SIFT-based visual features."""
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sift = cv2.SIFT_create()
        _keypoints, descriptors = sift.detectAndCompute(img, None)
        if descriptors is None:
            return np.zeros(128, dtype=np.float64)
        return np.mean(descriptors, axis=0)

    def calculate_sseq(self, image: np.ndarray) -> float:
        """Compute Spatial-Spectral Entropy-Based Quality score."""
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
        hist_norm = hist.ravel() / hist.sum()
        positive = hist_norm[hist_norm > 0]
        spatial_entropy = float(-1.0 * (positive * np.log2(positive)).sum())

        img_dct = cv2.dct(np.float32(img_gray) / 255.0)
        dct_hist = cv2.calcHist([img_dct], [0], None, [256], [0, 256])
        dct_norm = dct_hist.ravel() / dct_hist.sum()
        positive_dct = dct_norm[dct_norm > 0]
        spectral_entropy = float(
            -1.0 * (positive_dct * np.log2(positive_dct)).sum()
        )
        return spatial_entropy + spectral_entropy

    def calculate_fqadi_features(self, image: np.ndarray) -> float:
        """Compute FQADI edge density feature."""
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img, 100, 200)
        return float(np.sum(edges)) / float(img.shape[0] * img.shape[1])

    def compute_all_scores(self, image: np.ndarray) -> dict[str, float]:
        """Compute all IQA metrics and return as a dict."""
        return {
            "mscn": float(np.mean(self.calculate_mscn_coefficients(image))),
            "niqe": float(np.mean(self.compute_niqe_features(image))),
            "piqe": float(np.mean(self.calculate_piqe_index(image))),
            "jpeg_quality": float(np.mean(self.estimate_jpeg_quality(image))),
            "bliinds": float(np.mean(self.compute_bliinds_features(image))),
            "cornia": float(np.mean(self.extract_cornia_features(image))),
            "sseq": float(np.mean(self.calculate_sseq(image))),
            "fqadi": float(np.mean(self.calculate_fqadi_features(image))),
        }

    def compute_aggregate_score(self, image: np.ndarray) -> float:
        """Return a single aggregate IQA score (mean of all metrics)."""
        scores = self.compute_all_scores(image)
        return float(np.mean(list(scores.values())))

    def score_folder(self, folder_path: Path) -> dict[str, float]:
        """Score all images in a folder, keyed by filename."""
        results: dict[str, float] = {}
        for file_path in folder_path.iterdir():
            if file_path.suffix.lower() in self.IMAGE_EXTENSIONS:
                image = cv2.imread(str(file_path))
                if image is not None:
                    results[str(file_path)] = self.compute_aggregate_score(image)
        return results


scorer = ImageQualityScorer()


if __name__ == "__main__":
    config_dir = Path(__file__).resolve().parent
    folder_path_file = config_dir / "folder_path.txt"
    if folder_path_file.exists():
        raw = folder_path_file.read_text().strip()
        data_dir = (config_dir / raw / "datasets").resolve()
        if data_dir.is_dir():
            for file_path in data_dir.iterdir():
                image = cv2.imread(str(file_path))
                if image is not None:
                    print(f"{file_path}: {scorer.compute_aggregate_score(image):.4f}")
                else:
                    print(f"Unable to read image: {file_path.name}")
