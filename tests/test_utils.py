"""Unit tests for bi4media.utils module."""

from __future__ import annotations

import tempfile
from pathlib import Path

import numpy as np
import pytest

from bi4media.microservices.image_score import ImageQualityScorer
from bi4media.microservices.utils import (
    FolderInfo,
    ImageMetadata,
    VideoMetadata,
    gather_folder_info,
    get_folder_path_from_file,
    get_image_metadata,
    get_video_metadata,
)


@pytest.fixture()
def scorer() -> ImageQualityScorer:
    return ImageQualityScorer()


@pytest.fixture()
def sample_image_path(tmp_path: Path) -> Path:
    """Create a minimal valid PNG image for testing."""
    from PIL import Image

    img = Image.new("RGB", (64, 64), color=(128, 64, 32))
    path = tmp_path / "test_image.png"
    img.save(path)
    return path


@pytest.fixture()
def sample_video_path(tmp_path: Path) -> Path:
    """Create a dummy file pretending to be a video."""
    path = tmp_path / "test_video.mp4"
    path.write_bytes(b"\x00" * 1024)
    return path


@pytest.fixture()
def folder_with_files(tmp_path: Path, sample_image_path: Path) -> Path:
    """Set up a folder structure with images and a text config."""
    sub = tmp_path / "subdir"
    sub.mkdir()

    from PIL import Image

    img = Image.new("RGB", (32, 32), color=(255, 0, 0))
    img.save(sub / "img2.jpg")

    img2 = Image.new("RGB", (32, 32), color=(0, 255, 0))
    img2.save(tmp_path / "img3.png")

    (tmp_path / "config.txt").write_text(".")
    return tmp_path


class TestGetFolderPathFromFile:
    def test_reads_path_from_file(self, folder_with_files: Path) -> None:
        config = folder_with_files / "config.txt"
        result = get_folder_path_from_file(config)
        assert result.is_dir()

    def test_expands_user(self, tmp_path: Path) -> None:
        config = tmp_path / "path.txt"
        config.write_text("~/some_dir")
        result = get_folder_path_from_file(config)
        assert "some_dir" in str(result)


class TestGetImageMetadata:
    def test_extracts_metadata(self, scorer: ImageQualityScorer, sample_image_path: Path) -> None:
        meta = get_image_metadata(sample_image_path, scorer)
        assert meta is not None
        assert meta.filename == "test_image.png"
        assert meta.size == (64, 64)
        assert meta.resolution == 64 * 64
        assert meta.file_size > 0
        assert isinstance(meta.scores, dict)

    def test_returns_none_for_missing_file(self, scorer: ImageQualityScorer) -> None:
        result = get_image_metadata(Path("/nonexistent/image.png"), scorer)
        assert result is None


class TestGetVideoMetadata:
    def test_extracts_metadata(self, sample_video_path: Path) -> None:
        meta = get_video_metadata(sample_video_path)
        assert meta is not None
        assert meta.filename == "test_video.mp4"
        assert meta.file_size == 1024

    def test_returns_none_for_missing_file(self) -> None:
        result = get_video_metadata(Path("/nonexistent/video.mp4"))
        assert result is None


class TestGatherFolderInfo:
    def test_counts_images_and_videos(self, folder_with_files: Path) -> None:
        info_list = gather_folder_info(folder_with_files)
        assert len(info_list) > 0
        total_images = sum(f.images for f in info_list)
        assert total_images >= 2

    def test_empty_folder(self, tmp_path: Path) -> None:
        info_list = gather_folder_info(tmp_path)
        assert len(info_list) == 1
        assert info_list[0].images == 0
        assert info_list[0].videos == 0


class TestDataclasses:
    def test_image_metadata_fields(self) -> None:
        meta = ImageMetadata(
            filename="a.png", size=(100, 100), mode="RGB", fmt="PNG",
            created_at=None, file_size=1024, resolution=10000,
        )
        assert meta.filename == "a.png"
        assert meta.scores == {}

    def test_video_metadata_fields(self) -> None:
        meta = VideoMetadata(filename="v.mp4", created_at=None, file_size=512)
        assert meta.filename == "v.mp4"

    def test_folder_info_defaults(self) -> None:
        info = FolderInfo(path="/tmp")
        assert info.images == 0
        assert info.videos == 0
