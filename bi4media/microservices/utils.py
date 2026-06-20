"""Utility functions for folder traversal and media metadata extraction."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
from PIL import Image

from .image_score import ImageQualityScorer

logger = logging.getLogger(__name__)

IMAGE_EXTENSIONS: frozenset[str] = frozenset({".png", ".jpg", ".jpeg", ".bmp", ".gif"})
VIDEO_EXTENSIONS: frozenset[str] = frozenset({".mp4", ".avi", ".mov", ".mkv"})


@dataclass(frozen=True, slots=True)
class ImageMetadata:
    filename: str
    size: tuple[int, int]
    mode: str
    fmt: str
    created_at: datetime
    file_size: int
    resolution: int
    scores: dict[str, float] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class VideoMetadata:
    filename: str
    created_at: datetime
    file_size: int


@dataclass(slots=True)
class FolderInfo:
    path: str
    images: int = 0
    videos: int = 0


def get_folder_path_from_file(file_path: Path) -> Path:
    """Read and resolve a folder path from a text config file."""
    config_dir = file_path.resolve().parent
    raw = file_path.read_text().strip()
    resolved = (config_dir / raw).expanduser().resolve()
    logger.info("Reading folder path from %s: %s", file_path, resolved)
    return resolved


def get_image_metadata(
    image_path: Path, scorer: ImageQualityScorer
) -> Optional[ImageMetadata]:
    """Extract metadata and IQA scores from a single image."""
    try:
        with Image.open(image_path) as img:
            img_cv = np.array(img)[:, :, ::-1].copy()
            scores = scorer.compute_all_scores(img_cv)
            return ImageMetadata(
                filename=image_path.name,
                size=img.size,
                mode=img.mode,
                fmt=img.format or "",
                created_at=datetime.fromtimestamp(image_path.stat().st_ctime),
                file_size=image_path.stat().st_size,
                resolution=img.size[0] * img.size[1],
                scores=scores,
            )
    except Exception:
        logger.exception("Error extracting metadata for %s", image_path)
        return None


def get_video_metadata(video_path: Path) -> Optional[VideoMetadata]:
    """Extract basic metadata from a video file."""
    try:
        stat = video_path.stat()
        return VideoMetadata(
            filename=video_path.name,
            created_at=datetime.fromtimestamp(stat.st_ctime),
            file_size=stat.st_size,
        )
    except Exception:
        logger.exception("Error extracting metadata for %s", video_path)
        return None


def gather_folder_info(folder_path: Path) -> list[FolderInfo]:
    """Walk a directory tree and count images/videos per subfolder."""
    info: list[FolderInfo] = []
    try:
        for root, _, files in folder_path.walk():
            image_count = sum(
                1 for f in files if Path(f).suffix.lower() in IMAGE_EXTENSIONS
            )
            video_count = sum(
                1 for f in files if Path(f).suffix.lower() in VIDEO_EXTENSIONS
            )
            info.append(
                FolderInfo(path=str(root), images=image_count, videos=video_count)
            )
    except Exception:
        logger.exception("Failed to gather folder info from %s", folder_path)
    return info


def gather_metadata(
    folder_path: Path,
    scorer: ImageQualityScorer,
    max_per_type: int = 2,
) -> pd.DataFrame:
    """Collect metadata from up to `max_per_type` images and videos per folder."""
    records: list[dict] = []
    try:
        for root, _, files in folder_path.walk():
            image_count = 0
            video_count = 0
            for fname in files:
                fpath = root / fname
                ext = fpath.suffix.lower()
                if ext in IMAGE_EXTENSIONS and image_count < max_per_type:
                    meta = get_image_metadata(fpath, scorer)
                    if meta is not None:
                        records.append(_image_meta_to_dict(meta))
                        image_count += 1
                elif ext in VIDEO_EXTENSIONS and video_count < max_per_type:
                    meta = get_video_metadata(fpath)
                    if meta is not None:
                        records.append(_video_meta_to_dict(meta))
                        video_count += 1
                if image_count >= max_per_type and video_count >= max_per_type:
                    break
    except Exception:
        logger.exception("Failed to gather metadata from %s", folder_path)
    return pd.DataFrame(records)


def _image_meta_to_dict(meta: ImageMetadata) -> dict:
    d: dict = {
        "filename": meta.filename,
        "size": meta.size,
        "mode": meta.mode,
        "format": meta.fmt,
        "created_at": meta.created_at,
        "file_size": meta.file_size,
        "resolution": meta.resolution,
        "type": "image",
    }
    d.update(meta.scores)
    return d


def _video_meta_to_dict(meta: VideoMetadata) -> dict:
    return {
        "filename": meta.filename,
        "created_at": meta.created_at,
        "file_size": meta.file_size,
        "type": "video",
    }
