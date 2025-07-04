# internship-pw
Internship Physics Wallah --- Mushroom Prediction

# Mushroom Classification - Edible or Poisonous?

This project uses machine learning techniques to classify mushrooms as **edible** or **poisonous** based on their physical characteristics. It is based on the [UCI Mushroom Dataset](https://www.kaggle.com/datasets/uciml/mushroom-classification) and was completed as part of an internship project in the Agriculture domain.

---

## Problem Statement

The Audubon Society Field Guide to North American Mushrooms states that there is no simple rule for determining mushroom edibility. This project builds a machine learning model that predicts whether a mushroom is edible or poisonous using its 22 categorical attributes (like odor, gill color, habitat, etc.).

---

## Tech Stack

- **Language**: Python
- **ML Libraries**: scikit-learn, XGBoost
- **EDA & Plotting**: pandas, seaborn, matplotlib
- **Model Deployment**: Streamlit
- **Model Saving**: joblib
- **Logging**: loguru

---

## ML Workflow

1. **Exploratory Data Analysis (EDA)**
2. **Data Preprocessing**
   - Label encoding of categorical variables
   - Train/Test split
3. **Model Training**
   - Decision Tree, Random Forest, XGBoost
4. **Model Evaluation**
   - Accuracy, Confusion Matrix, Classification Report
5. **Model Exporting**
   - Using `joblib` for saving best model
6. **Frontend Interface**
   - Streamlit app for user-friendly interaction

This project is an end-to-end machine learning pipeline that classifies mushrooms as either edible or poisonous based on 22 physical characteristics. The system integrates all standard stages of ML development — from data ingestion and preprocessing to model training, evaluation, and real-time prediction — while incorporating MLOps tools for reproducibility and traceability.
---

## Dataset

The dataset is sourced from the UCI Mushroom Classification dataset via Kaggle. It contains 8124 rows and 22 categorical input features such as cap shape, cap color, odor, gill attachment, and habitat. The target label is whether the mushroom is edible or poisonous.
---

## Pipeline Overview

- Data Ingestion: Downloads and stores the dataset using KaggleHub.

- Data Validation: Checks for schema mismatches, missing values, and class imbalance.

- Data Transformation: Encodes categorical features using OrdinalEncoder; label encodes the target.

- Model Training: Trains Logistic Regression, Random Forest, and XGBoost models.

- Evaluation: Computes accuracy, precision, recall, and F1-score.

- Prediction Pipeline: Accepts user inputs and returns edible or poisonous.

- MLflow: Tracks metrics, models, and experiments.

- DVC: Tracks data versions and pipeline outputs.
---

## Deployed Frontend

The user interface for real-time prediction is deployed at:
[Click Here](https://mushroom-frontend-bay.vercel.app/)
You can select feature values through dropdowns and get an instant classification.
---

## To Try the Project Locally

Clone the repository

`git clone https://github.com/Agam-Patel-DS/internship-pw.git`
`cd internship-pw`

Create a virtual environment and install dependencies

`python -m venv venv`
`source venv/bin/activate   # On Windows: venv\Scripts\activate`
`pip install -r requirements.txt`

Run the full pipeline

`python main.py`

This will:

- Download the dataset

- Validate and transform data

- Train three models (Logistic Regression, Random Forest, XGBoost)

- Select and save the best model

- Generate evaluation report

- Log metrics and models in MLflow

- Store all outputs in the artifacts/ directory
---


## Contributor

Agam Patel
---
