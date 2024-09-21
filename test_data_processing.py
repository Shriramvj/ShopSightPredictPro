# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:26:54 2023

@author: shrir
"""

import unittest
import pandas as pd
from shop_sight_predict_pro.data_processing import load_data, preprocess_data

class TestDataProcessing(unittest.TestCase):

    def test_load_data(self):
        """Test that the load_data function correctly loads data."""
        file_path = 'C:/Users/shrir/Downloads/online+shoppers+purchasing+intention+dataset/online_shoppers_intention.csv'
        data = load_data(file_path)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertFalse(data.empty)

    def test_preprocess_data(self):
        """Test that the preprocess_data function correctly preprocesses the data."""
        # Create a sample DataFrame
        sample_data = pd.DataFrame({
            'numeric_feature': [1, 2, 3],
            'categorical_feature': ['A', 'B', 'A']
        })

        processed_data = preprocess_data(sample_data)

        # Check if processed_data is a DataFrame
        self.assertIsInstance(processed_data, pd.DataFrame)

        # Add more assertions depending on your preprocessing steps
        # For example, if you've encoded categorical features, check if the original feature is replaced or not
        # If you've scaled numerical features, you can check if they are scaled correctly

if __name__ == '__main__':
    unittest.main()
