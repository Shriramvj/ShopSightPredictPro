# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:03:24 2023

@author: shrir
"""

from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):
    """Train a logistic regression model."""
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model
