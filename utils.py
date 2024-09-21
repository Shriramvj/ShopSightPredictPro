# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:03:48 2023

@author: shrir
"""

def split_data(X, y, test_size=0.3, random_state=42):
    """Split the dataset into training and testing sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
