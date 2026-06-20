"""Orchestrator: launches all BI4CV microservices as subprocesses."""

from __future__ import annotations

import logging
import subprocess
import sys
import time
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

SERVICES: list[str] = [
    "1_main_service.py",
    "2_bi_tools.py",
    "3_image_video_metadata_dashboard.py",
]

MICROSERVICES_DIR = Path(__file__).resolve().parent / "microservices"


def _launch_services() -> list[subprocess.Popen[str]]:
    """Start each microservice subprocess and return their handles."""
    processes: list[subprocess.Popen[str]] = []
    for service in SERVICES:
        script = MICROSERVICES_DIR / service
        logger.info("Starting %s", script)
        proc = subprocess.Popen([sys.executable, str(script)])
        processes.append(proc)
        time.sleep(1)
    return processes


def _shutdown(processes: list[subprocess.Popen[str]]) -> None:
    """Gracefully terminate all subprocesses."""
    logger.info("Shutting down services...")
    for proc in processes:
        proc.terminate()
    for proc in processes:
        proc.wait()


def main() -> None:
    """Entry point: launch microservices and keep alive until interrupted."""
    processes = _launch_services()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        _shutdown(processes)


if __name__ == "__main__":
    main()
