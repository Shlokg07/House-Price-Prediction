import joblib
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from preprocess import preprocess_data, load_data

def train_models(data_path):
    df = load_data(data_path)
    preprocessor, X_train, X_test, y_train, y_test = preprocess_data(df)

    models = {
        "LinearRegression": LinearRegression(),
        "Ridge": Ridge(alpha=1.0),
        "Lasso": Lasso(alpha=0.01),
        "GradientBoosting": GradientBoostingRegressor(n_estimators=200, learning_rate=0.1)
    }

    best_model = None
    best_score = float("inf")

    for name, model in models.items():
        pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])
        pipeline.fit(X_train, y_train)
        preds = pipeline.predict(X_test)
        mse = mean_squared_error(y_test, preds)
        rmse = mse ** 0.5  # Calculate RMSE by taking square root of MSE
        print(f"{name} RMSE: {rmse:.2f}")

        if rmse < best_score:
            best_score = rmse
            best_model = pipeline

    joblib.dump(best_model, "models/best_model.pkl")
    print("Best model saved!")

if __name__ == "__main__":
    train_models("Data/house_prices.csv")
