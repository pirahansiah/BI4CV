import unittest
from unittest.mock import patch
import numpy as np
import cv2

# Import the functions to be tested from the image_score module
from BI4CV.image_score import (calculate_mscn_coefficients, compute_niqe_features, calculate_piqe_index, 
                               estimate_jpeg_quality, compute_bliinds_features, extract_cornia_features, 
                               calculate_sseq, calculate_fqadi_features)

class TestImageQualityFunctions(unittest.TestCase):

    @patch('cv2.imread')
    def setUp(self, mock_imread):
        # Mocking an image read
        self.image = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
        mock_imread.return_value = self.image

    def test_calculate_mscn_coefficients(self):
        result = calculate_mscn_coefficients(self.image)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, (256, 256))

    def test_compute_niqe_features(self):
        mu_param, sigma_param = compute_niqe_features(self.image)
        self.assertIsInstance(mu_param, float)
        self.assertIsInstance(sigma_param, float)
        self.assertGreaterEqual(mu_param, 0)
        self.assertLessEqual(mu_param, 1)
        self.assertGreaterEqual(sigma_param, 0)
        self.assertLessEqual(sigma_param, 1)

    def test_calculate_piqe_index(self):
        result = calculate_piqe_index(self.image)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)

    def test_estimate_jpeg_quality(self):
        result = estimate_jpeg_quality(self.image)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 100)

    def test_compute_bliinds_features(self):
        result = compute_bliinds_features(self.image)
        self.assertTrue(isinstance(result, (float, np.float32)))
        self.assertGreaterEqual(result, 0)

    def test_extract_cornia_features(self):
        result = extract_cornia_features(self.image)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape[0], 128)  # Assuming 128 features

    def test_calculate_sseq(self):
        result = calculate_sseq(self.image)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)

    def test_calculate_fqadi_features(self):
        result = calculate_fqadi_features(self.image)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
