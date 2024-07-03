import os
import pandas as pd
from PIL import Image
from datetime import datetime
import numpy as np
import logging
from image_score import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_folder_path_from_file(file_path1):
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.abspath(os.path.join(current_dir, file_path1))
        print(file_path)

        with open(file_path, 'r') as file:
            #folder_path = file.readline().strip()
            folder_path = os.path.expanduser(os.path.normpath(os.path.join(current_dir, file.read().strip())))
            logging.info(f'Reading folder path from {file_path}: {folder_path}')
            return folder_path
    except Exception as e:
        logging.error(f"Failed to read the folder path from {file_path}: {e}")
        raise

def get_image_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            img_cv = np.array(img)
            img_cv = img_cv[:, :, ::-1].copy()
            thumbnail = img.resize((100, 100))
            return {
                "filename": os.path.basename(image_path),
                "size": img.size,
                "mode": img.mode,
                "format": img.format,
                "created_at": datetime.fromtimestamp(os.path.getctime(image_path)),
                "file_size": os.path.getsize(image_path),
                "resolution": img.size[0] * img.size[1],
                "thumbnail": thumbnail,
                "calculate_mscn_coefficients": calculate_mscn_coefficients(img_cv),
                "compute_niqe_features": compute_niqe_features(img_cv),
                "calculate_piqe_index": calculate_piqe_index(img_cv),
                "estimate_jpeg_quality": estimate_jpeg_quality(img_cv),
                "compute_bliinds_features": compute_bliinds_features(img_cv),
                "extract_cornia_features": extract_cornia_features(img_cv),
                "calculate_sseq": calculate_sseq(img_cv),
                "calculate_fqadi_features": calculate_fqadi_features(img_cv)
            }
    except Exception as e:
        logging.error(f"Error extracting metadata and computing scores for image {image_path}: {e}")
        return None

def get_video_metadata(video_path):
    try:
        return {
            "filename": os.path.basename(video_path),
            "created_at": datetime.fromtimestamp(os.path.getctime(video_path)),
            "file_size": os.path.getsize(video_path)
        }
    except Exception as e:
        logging.error(f"Error extracting metadata from video {video_path}: {e}")
        return None

def gather_folder_info(folder_path):
    folder_info = {}
    try:
        for root, _, files in os.walk(folder_path):
            image_count = sum(1 for file in files if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')))
            video_count = sum(1 for file in files if file.lower().endswith(('mp4', 'avi', 'mov', 'mkv')))
            folder_info[root] = {'images': image_count, 'videos': video_count}
        return folder_info
    except Exception as e:
        logging.error(f"Failed to gather folder info from {folder_path}: {e}")
        return {}

def gather_metadata(folder_path):
    metadata = []
    try:
        for root, _, files in os.walk(folder_path):
            image_count = 0
            video_count = 0
            for file in files:
                if image_count >= 2 and video_count >= 2:
                    break
                file_path = os.path.join(root, file)
                if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')) and image_count < 2:
                    meta = get_image_metadata(file_path)
                    #image_count += 1
                elif file.lower().endswith(('mp4', 'avi', 'mov', 'mkv')) and video_count < 2:
                    meta = get_video_metadata(file_path)
                    #video_count += 1
                else:
                    continue
                if meta:
                    metadata.append(meta)
        return pd.DataFrame(metadata)
    except Exception as e:
        logging.error(f"Failed to gather metadata from {folder_path}: {e}")
        return pd.DataFrame()
