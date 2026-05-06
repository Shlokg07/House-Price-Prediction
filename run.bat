@echo off
REM House Price Prediction - Setup and Run Script

cd /d "D:\Installers\VS Codes\House Price Prediction"

echo.
echo ========================================
echo House Price Prediction Project
echo ========================================
echo.
echo 1. Train Model
echo 2. Evaluate Model
echo 3. Run Streamlit App
echo 4. Exit
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Training model...
    D:\Installers\Anaconda\python.exe src\train.py
    pause
) else if "%choice%"=="2" (
    echo.
    echo Evaluating model...
    D:\Installers\Anaconda\python.exe src\evaluate.py
    pause
) else if "%choice%"=="3" (
    echo.
    echo Starting Streamlit app...
    echo Open your browser to http://localhost:8501
    echo.
    D:\Installers\Anaconda\python.exe -m streamlit run app/streamlit_app.py
) else if "%choice%"=="4" (
    exit
) else (
    echo Invalid choice!
    pause
)
