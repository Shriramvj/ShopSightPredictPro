# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:57:57 2023

@author: shrir
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split




def load_data(file_path):
    """Load dataset from a given file path."""
    # Your code to load the data
    pass  # Replace with actual code to load data
    
file_path = r"C:\Users\shrir\Downloads\online+shoppers+purchasing+intention+dataset\online_shoppers_intention.csv"
data = load_data(file_path)


def preprocess_data(data):
    """Preprocess the data: fill missing values, encode categorical variables, etc."""
    # Example: One-hot encoding for categorical columns and Min-Max scaling for numerical columns
    data_encoded = pd.get_dummies(data)
    scaler = MinMaxScaler()
    numerical_features = data_encoded.select_dtypes(include=['int64', 'float64']).columns
    data_encoded[numerical_features] = scaler.fit_transform(data_encoded[numerical_features])
    return data_encoded
