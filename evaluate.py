import joblib
from sklearn.metrics import mean_squared_error, r2_score
from preprocess import load_data, preprocess_data

def evaluate_model(data_path):
    df = load_data(data_path)
    preprocessor, X_train, X_test, y_train, y_test = preprocess_data(df)

    model = joblib.load("models/best_model.pkl")
    preds = model.predict(X_test)

    mse = mean_squared_error(y_test, preds)
    rmse = mse ** 0.5  # Calculate RMSE from MSE
    r2 = r2_score(y_test, preds)

    print(f"Evaluation Results:\nRMSE: {rmse:.2f}\nR² Score: {r2:.2f}")

if __name__ == "__main__":
    evaluate_model("Data/house_prices.csv")
