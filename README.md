# # 🛒 Online Shoppers Purchasing Intention Prediction

## 📋 Project Overview
This project focuses on predicting the purchasing intentions of online shoppers using a dataset of various user behaviors on an e-commerce website. By analyzing user activities, such as page views and visit duration, the goal is to identify whether a user is likely to complete a purchase or not. The project uses machine learning models, specifically logistic regression, to perform this classification task.

The project includes:
- Data processing and feature engineering to clean and transform the raw data.
- Building and training machine learning models to predict purchasing intentions.
- Model evaluation and testing to ensure performance and accuracy.

## 💡 Key Questions Answered
1. **Can we predict whether an online shopper will complete a purchase?**
   - By analyzing key features such as the duration of the visit, number of product pages viewed, and user behaviors, the model predicts whether a user is likely to make a purchase.
   
2. **What are the key features driving purchase decisions?**
   - This project helps identify which user behaviors, such as time spent on product pages or type of referral source, significantly impact the likelihood of a purchase.

3. **How can we preprocess data to improve model performance?**
   - We explore the use of data preprocessing techniques, such as one-hot encoding for categorical features and scaling for numerical data, to enhance the model's predictive power.

## 📁 Project Structure

```plaintext
├── data_processing.py          # Script to load and preprocess data
├── model_training.py           # Script for training the logistic regression model
├── test_data_processing.py     # Unit tests for data processing steps
├── utils.py                    # Helper functions for data splitting and other utilities
