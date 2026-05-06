#!/usr/bin/env python
"""
Test script to verify the House Price Prediction project is working correctly.
Run this after installing dependencies to ensure all components work.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test if all required packages can be imported."""
    print("=" * 60)
    print("TESTING IMPORTS...")
    print("=" * 60)
    
    try:
        import pandas
        print("✓ pandas")
    except ImportError as e:
        print(f"✗ pandas: {e}")
        return False
    
    try:
        import sklearn
        print("✓ scikit-learn")
    except ImportError as e:
        print(f"✗ scikit-learn: {e}")
        return False
    
    try:
        import joblib
        print("✓ joblib")
    except ImportError as e:
        print(f"✗ joblib: {e}")
        return False
    
    try:
        import streamlit
        print("✓ streamlit")
    except ImportError as e:
        print(f"✗ streamlit: {e}")
        return False
    
    print("\n✓ All imports successful!\n")
    return True


def test_data_loading():
    """Test if data can be loaded."""
    print("=" * 60)
    print("TESTING DATA LOADING...")
    print("=" * 60)
    
    try:
        from preprocess import load_data
        df = load_data("Data/house_prices.csv")
        print(f"✓ Data loaded successfully!")
        print(f"  - Rows: {len(df)}")
        print(f"  - Columns: {list(df.columns)}\n")
        return True
    except Exception as e:
        print(f"✗ Failed to load data: {e}\n")
        return False


def test_preprocessing():
    """Test if preprocessing works."""
    print("=" * 60)
    print("TESTING PREPROCESSING...")
    print("=" * 60)
    
    try:
        from preprocess import load_data, preprocess_data
        df = load_data("Data/house_prices.csv")
        preprocessor, X_train, X_test, y_train, y_test = preprocess_data(df)
        
        print(f"✓ Preprocessing successful!")
        print(f"  - X_train shape: {X_train.shape}")
        print(f"  - X_test shape: {X_test.shape}")
        print(f"  - y_train shape: {y_train.shape}")
        print(f"  - y_test shape: {y_test.shape}\n")
        return True
    except Exception as e:
        print(f"✗ Preprocessing failed: {e}\n")
        return False


def test_project_structure():
    """Test if all necessary directories and files exist."""
    print("=" * 60)
    print("TESTING PROJECT STRUCTURE...")
    print("=" * 60)
    
    required_files = [
        "Data/house_prices.csv",
        "Models",
        "src/train.py",
        "src/preprocess.py",
        "src/evaluate.py",
        "app/streamlit_app.py",
        "Notebooks/eda.ipynb",
        "Notebooks/model_training.ipynb",
        "requirements.txt",
        "README.md"
    ]
    
    all_exist = True
    for item in required_files:
        if os.path.exists(item):
            print(f"✓ {item}")
        else:
            print(f"✗ {item} - MISSING")
            all_exist = False
    
    print()
    return all_exist


def main():
    """Run all tests."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + " House Price Prediction - Project Verification ".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    print("\n")
    
    tests = [
        ("Project Structure", test_project_structure),
        ("Imports", test_imports),
        ("Data Loading", test_data_loading),
        ("Preprocessing", test_preprocessing),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"ERROR in {test_name}: {e}\n")
            results.append((test_name, False))
    
    # Summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    print()
    
    all_passed = all(result for _, result in results)
    if all_passed:
        print("✓ All tests passed! Project is ready to use.")
        print("\nNext steps:")
        print("  1. Run: python src/train.py")
        print("  2. Run: python src/evaluate.py")
        print("  3. Run: streamlit run app/streamlit_app.py")
    else:
        print("✗ Some tests failed. Please check the errors above.")
        print("\nTroubleshooting:")
        print("  - Make sure you've installed dependencies: pip install -r requirements.txt")
        print("  - Make sure you're running from the project root directory")
        print("  - Check that Python 3.8+ is installed")
    
    print("\n")
    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
