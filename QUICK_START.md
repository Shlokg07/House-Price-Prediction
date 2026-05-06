# 🚀 QUICK START GUIDE

## Step 1: Install Dependencies
Open terminal/command prompt in this directory and run:
```bash
pip install -r requirements.txt
```

## Step 2: Verify Installation (Optional)
Run the test script to ensure everything is set up correctly:
```bash
python test_project.py
```

## Step 3: Train the Model
```bash
python src/train.py
```
**Expected output:**
- LinearRegression RMSE: ...
- Ridge RMSE: ...
- Lasso RMSE: ...
- GradientBoosting RMSE: ...
- Best model saved!

## Step 4: Evaluate the Model
```bash
python src/evaluate.py
```
**Expected output:**
- Evaluation Results:
- RMSE: ...
- R² Score: ...

## Step 5: Run the Web App
```bash
streamlit run app/streamlit_app.py
```
A browser window will open at http://localhost:8501

## Optional: Explore Notebooks
Open these in Jupyter:
- `Notebooks/eda.ipynb` - Exploratory Data Analysis
- `Notebooks/model_training.ipynb` - Model Training & Predictions

## Troubleshooting

**Q: "ModuleNotFoundError: No module named..."**
A: Run `pip install -r requirements.txt` again

**Q: "FileNotFoundError: house_prices.csv"**
A: Make sure you're in the project root directory

**Q: Streamlit port 8501 is already in use**
A: Run `streamlit run app/streamlit_app.py --server.port 8502`

**Q: Permission denied when running python scripts (Linux/Mac)**
A: Run `chmod +x *.py` first, then `python src/train.py`

## Project Files Structure
```
├── Data/                    # Data folder
│   └── house_prices.csv    # Training data
├── Models/                  # Model folder (created after training)
│   └── best_model.pkl      # Saved trained model
├── Notebooks/               # Jupyter notebooks
│   ├── eda.ipynb           # Exploratory data analysis
│   └── model_training.ipynb# Model training notebook
├── src/                     # Source code
│   ├── train.py            # Training script
│   ├── preprocess.py       # Data preprocessing
│   └── evaluate.py         # Model evaluation
├── app/                     # Web app
│   └── streamlit_app.py    # Streamlit application
├── requirements.txt         # Package dependencies
├── README.md               # Full documentation
├── test_project.py         # Testing script
└── QUICK_START.md          # This file
```

---

**All set! Start with Step 1 above.**
