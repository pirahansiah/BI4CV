import cv2
import os
import numpy as np
from scipy.special import gamma
            # BRISQUE (Blind/Referenceless Image Spatial Quality Evaluator)
            # BRISQUE measures the naturalness of images using scene statistics without requiring a reference image. A Python implementation can be crafted by extracting Mean Subtracted Contrast Normalized (MSCN) coefficients, which are then used to train a support vector machine (SVM) to predict quality scores.
def calculate_mscn_coefficients(image, kernel_size=7, sigma=1.166):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) / 255.0
    blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)
    blurred_sq = blurred * blurred
    sigma = np.sqrt(cv2.GaussianBlur(img * img, (kernel_size, kernel_size), sigma) - blurred_sq + 1e-10)
    mscn = (img - blurred) / sigma
    return mscn
            # NIQE (Natural Image Quality Evaluator)
            # NIQE is a no-reference metric that uses a collection of statistical features based on natural scene statistics to provide a measure of perceptual image quality.
def compute_niqe_features(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) / 255.0
    mu_param = np.mean(img)
    sigma_param = np.std(img)
    return mu_param, sigma_param
            # PIQE (Perception-based Image Quality Evaluator)
            # PIQE is another no-reference image quality metric that does not require any training or learning from a human-rated database. Instead, it relies on certain statistical tests.
def calculate_piqe_index(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) / 255.0
    local_variance = cv2.Laplacian(img, cv2.CV_64F).var()
    return local_variance
#JPEG Quality Evaluator (JPEG-Q)
#This method estimates the quality of JPEG images by analyzing compression artifacts. It typically involves examining the blockiness and frequency of quantization errors, which are common in JPEG compressed images.
def estimate_jpeg_quality(image):               
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    y_channel = ycrcb[:, :, 0]                
    dct = cv2.dct(np.float32(y_channel)/255.0)
    zeros = np.sum(dct < 0.01)
    quality_estimate = 100 - (zeros / np.size(dct) * 100)
    return quality_estimate
#BLIINDS-II (Blind Image Integrity Notator using DCT Statistics)
#BLIINDS-II uses discrete cosine transform (DCT) coefficients to model natural scene statistics for quality prediction.
def compute_bliinds_features(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_dct = cv2.dct(np.float32(img) / 255.0)
    block_size = 8
    blocks_variance = []
    for i in range(0, img.shape[0], block_size):
        for j in range(0, img.shape[1], block_size):
            block = img_dct[i:i+block_size, j:j+block_size]
            blocks_variance.append(np.var(block))
    bliinds_score = np.mean(blocks_variance)
    return bliinds_score
            # CORNIA (Cornell AnoTated Images for Blind Image Quality Assessment)
            # CORNIA is an NR-IQA method that uses unsupervised feature learning to predict image quality based on visual importance indicators derived from large-scale image datasets.
def extract_cornia_features(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    keypoints, descriptors = cv2.SIFT_create().detectAndCompute(img, None)
    return np.mean(descriptors, axis=0)
            # SSEQ (Spatial-Spectral Entropy-Based Quality)
            # SSEQ uses spatial and spectral entropy to measure the amount of perceived information in an image, which correlates with its visual quality.
def calculate_sseq(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
    hist_normalize = hist.ravel()/hist.sum()
    entropy = -1 * (hist_normalize[hist_normalize>0] * np.log2(hist_normalize[hist_normalize>0])).sum()
    img_dct = cv2.dct(np.float32(img_gray) / 255.0)
    dct_hist = cv2.calcHist([img_dct], [0], None, [256], [0, 256])
    dct_hist_normalize = dct_hist.ravel()/dct_hist.sum()
    spectral_entropy = -1 * (dct_hist_normalize[dct_hist_normalize>0] * np.log2(dct_hist_normalize[dct_hist_normalize>0])).sum()
    return entropy + spectral_entropy
            # FQADI (Feature-based Quality Assessment for Distorted Images)
            # FQADI utilizes machine learning techniques to analyze various image features that indicate distortions like blurring, blocking, and ringing, which are typical in compressed or poorly transmitted images.
def calculate_fqadi_features(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img, 100, 200)
    edge_density = np.sum(edges) / (img.shape[0] * img.shape[1])
    return edge_density

# Test
if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_dir, 'BI4CV.png')
    image = cv2.imread(config_file_path)
    if image is None:
        print('file not found')
        exit()
    #image = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
    print(' \n \n \n calculate_mscn_coefficients')
    print(calculate_mscn_coefficients(image))
    print(' \n \n \n compute_niqe_features')
    print(compute_niqe_features(image))
    print(' \n \n \n calculate_piqe_index')
    print(calculate_piqe_index(image))
    print(' \n \n \n estimate_jpeg_quality')
    print(estimate_jpeg_quality(image))
    print(' \n \n \n compute_bliinds_features')
    print(compute_bliinds_features(image))
    print(' \n \n \n extract_cornia_features')
    print(extract_cornia_features(image))
    print(' \n \n \n calculate_sseq')
    print(calculate_sseq(image))
    print(' \n \n \n calculate_fqadi_features')
    print(calculate_fqadi_features(image))




