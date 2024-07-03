# Farshid Pirahansiah
# Create : 2024 - May
# update: 2024 - June
import subprocess
import os
import time

# Define the paths to your service scripts
services = [
    "1_main_service.py",
    "2_bi_tools.py",
    "3_image_video_metadata_dashboard.py"
]

processes = []

try:
    for service in services:
        script_path = os.path.join(os.path.dirname(__file__), "microservices", service)
        process = subprocess.Popen(['python', script_path])
        processes.append(process)
        time.sleep(1)  # Ensure services start in order without conflicts

    # Keep the script running to keep the subprocesses alive
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down services...")
    for process in processes:
        process.terminate()
    for process in processes:
        process.wait()
