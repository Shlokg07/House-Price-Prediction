# 🏠 House Price Prediction Capstone Project

A complete machine learning project for predicting house prices using regression models, feature engineering, and Streamlit deployment.

## 📁 Project Structure

```
House Price Prediction/
├── app/
│   ├── README.md              # App documentation
│   └── streamlit_app.py       # Streamlit web interface
├── Data/
│   └── house_prices.csv       # Training dataset
├── Models/
│   └── best_model.pkl         # Trained model (generated after training)
├── Notebooks/
│   ├── eda.ipynb              # Exploratory Data Analysis
│   └── model_training.ipynb   # Model training notebook
├── src/
│   ├── preprocess.py          # Data preprocessing
│   ├── train.py               # Model training
│   └── evaluate.py            # Model evaluation
└── requirements.txt           # Project dependencies
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Model
```bash
python src/train.py
```
This will:
- Load and preprocess the data from `Data/house_prices.csv`
- Train 4 different regression models
- Save the best model to `Models/best_model.pkl`

### 3. Evaluate the Model
```bash
python src/evaluate.py
```
This will display:
- RMSE (Root Mean Squared Error)
- R² Score

### 4. Run the Streamlit App
```bash
streamlit run app/streamlit_app.py
```
Then open your browser to `http://localhost:8501`

## 📊 Models Trained

- **Linear Regression**: Baseline model
- **Ridge Regression**: L2 regularization (alpha=1.0)
- **Lasso Regression**: L1 regularization (alpha=0.01)
- **Gradient Boosting**: Ensemble method (200 estimators, 0.1 learning rate)

## 📈 Dataset Features

- **Area**: Square footage of the house
- **Rooms**: Number of rooms
- **Location**: Urban, Suburban, or Rural
- **SalePrice**: Target variable (house price)

## 🔍 Exploratory Data Analysis (EDA)

Open `Notebooks/eda.ipynb` in Jupyter to:
- View dataset statistics
- Check for missing values
- Visualize price distribution
- Analyze feature correlations

## 🧠 Model Training Notebook

Open `Notebooks/model_training.ipynb` in Jupyter to:
- Run model training interactively
- Evaluate model performance
- Make sample predictions

## 📝 Files Overview

### `src/preprocess.py`
Handles data loading and preprocessing:
- Loads CSV data
- Separates features and target
- Handles numeric and categorical features
- Applies StandardScaler and OneHotEncoder
- Splits data (80/20 train-test)

### `src/train.py`
Trains multiple models:
- Compares 4 regression models
- Selects best model based on RMSE
- Saves best model as pickle file

### `src/evaluate.py`
Evaluates the trained model:
- Loads the best model
- Computes RMSE and R² Score
- Prints evaluation metrics

### `app/streamlit_app.py`
Web interface for predictions:
- Input features via sidebar
- Real-time price predictions
- User-friendly interface

## ⚙️ Configuration

Default parameters can be modified in:
- **train.py**: Model hyperparameters
- **preprocess.py**: Train-test split ratio, target column name
- **streamlit_app.py**: Input ranges and options

## 🐛 Troubleshooting

### Issue: `FileNotFoundError: house_prices.csv`
- Ensure you're running scripts from the project root directory
- Check that `Data/house_prices.csv` exists

### Issue: `ModuleNotFoundError`
- Reinstall dependencies: `pip install -r requirements.txt`
- Ensure you have Python 3.8+

### Issue: Streamlit port already in use
- Kill the process or use: `streamlit run app/streamlit_app.py --server.port 8502`

## 📚 Dependencies

- **pandas**: Data manipulation
- **scikit-learn**: Machine learning models
- **numpy**: Numerical computing
- **joblib**: Model serialization
- **streamlit**: Web app framework
- **matplotlib**: Visualization
- **seaborn**: Statistical visualization

## 🎯 Next Steps

1. Improve the model with feature engineering
2. Collect more real estate data
3. Implement cross-validation
4. Add more models (XGBoost, LightGBM)
5. Deploy to production (Heroku, AWS, Azure)

## 📄 License

This project is open source and available for educational purposes.
