"""Unit tests for bi4media.image_score module."""

from __future__ import annotations

import numpy as np
import pytest

from bi4media.microservices.image_score import ImageQualityScorer


@pytest.fixture()
def scorer() -> ImageQualityScorer:
    return ImageQualityScorer()


@pytest.fixture()
def random_image() -> np.ndarray:
    return np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)


@pytest.fixture()
def solid_black_image() -> np.ndarray:
    return np.zeros((256, 256, 3), dtype=np.uint8)


class TestMscnCoefficients:
    def test_returns_ndarray(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        result = scorer.calculate_mscn_coefficients(random_image)
        assert isinstance(result, np.ndarray)

    def test_shape_matches_grayscale(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        result = scorer.calculate_mscn_coefficients(random_image)
        assert result.shape == (256, 256)

    def test_solid_image_near_zero(self, scorer: ImageQualityScorer, solid_black_image: np.ndarray) -> None:
        result = scorer.calculate_mscn_coefficients(solid_black_image)
        assert np.all(np.abs(result) < 1e-6)


class TestNiqeFeatures:
    def test_returns_tuple_of_floats(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        mu, sigma = scorer.compute_niqe_features(random_image)
        assert isinstance(mu, float)
        assert isinstance(sigma, float)

    def test_mu_in_zero_one(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        mu, _ = scorer.compute_niqe_features(random_image)
        assert 0.0 <= mu <= 1.0

    def test_sigma_non_negative(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        _, sigma = scorer.compute_niqe_features(random_image)
        assert sigma >= 0.0


class TestPiqeIndex:
    def test_returns_non_negative_float(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        result = scorer.calculate_piqe_index(random_image)
        assert isinstance(result, float)
        assert result >= 0.0

    def test_solid_image_is_zero(self, scorer: ImageQualityScorer, solid_black_image: np.ndarray) -> None:
        result = scorer.calculate_piqe_index(solid_black_image)
        assert result == pytest.approx(0.0, abs=1e-10)


class TestJpegQuality:
    def test_returns_float_in_range(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        result = scorer.estimate_jpeg_quality(random_image)
        assert isinstance(result, float)
        assert 0.0 <= result <= 100.0


class TestBliindsFeatures:
    def test_returns_non_negative(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        result = scorer.compute_bliinds_features(random_image)
        assert isinstance(result, float)
        assert result >= 0.0


class TestCorniaFeatures:
    def test_returns_array(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        result = scorer.extract_cornia_features(random_image)
        assert isinstance(result, np.ndarray)
        assert result.ndim == 1

    def test_fallback_to_zeros_when_no_keypoints(self, scorer: ImageQualityScorer, solid_black_image: np.ndarray) -> None:
        result = scorer.extract_cornia_features(solid_black_image)
        assert isinstance(result, np.ndarray)


class TestSseq:
    def test_returns_non_negative(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        result = scorer.calculate_sseq(random_image)
        assert isinstance(result, float)
        assert result >= 0.0


class TestFqadi:
    def test_returns_non_negative(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        result = scorer.calculate_fqadi_features(random_image)
        assert isinstance(result, float)
        assert result >= 0.0


class TestAggregateScore:
    def test_returns_float(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        score = scorer.compute_aggregate_score(random_image)
        assert isinstance(score, float)

    def test_compute_all_scores_returns_dict(self, scorer: ImageQualityScorer, random_image: np.ndarray) -> None:
        scores = scorer.compute_all_scores(random_image)
        assert isinstance(scores, dict)
        expected_keys = {
            "mscn", "niqe", "piqe", "jpeg_quality",
            "bliinds", "cornia", "sseq", "fqadi",
        }
        assert set(scores.keys()) == expected_keys
