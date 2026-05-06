# 🏠 House Price Prediction Capstone Project

## Overview
This project predicts house prices using regression models with feature engineering, preprocessing, and deployment via Streamlit.

## Steps
1. Data preprocessing (`src/preprocess.py`)
2. Model training (`src/train.py`)
3. Evaluation (`src/evaluate.py`)
4. Deployment (`app/streamlit_app.py`)

## Run
```bash
pip install -r requirements.txt
python src/train.py
python src/evaluate.py
streamlit run app/streamlit_app.py
