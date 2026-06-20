"""Pytest configuration for BI4CV test suite."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure bi4media package is importable from the project root
_project_root = str(Path(__file__).resolve().parent.parent)
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)
