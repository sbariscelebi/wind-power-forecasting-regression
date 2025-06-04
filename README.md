# Wind Power Forecasting using Regression Models

This repository contains a modular implementation of a short-term wind power forecasting pipeline based on SCADA data.  
The models include **Support Vector Regression (SVR)**, **k-Nearest Neighbors (KNN)**, and **Linear Regression**, evaluated on high-resolution operational wind turbine data.

## 📊 Features
- Time-series aware model training and testing
- Automated hyperparameter tuning using GridSearchCV
- Detailed performance evaluation (MAE, RMSE, R², MAPE, MdAE)
- Visual outputs: error plots, scatter plots, and prediction time series
- Modular Python codebase with reusable components

## 🗂 Project Structure
```
├── main.py                      # Main execution script
├── requirements.txt             # Python package dependencies
├── models/
│   ├── linear_regression.py     # Linear Regression model and param grid
│   ├── knn.py                   # KNN model and param grid
│   └── svr.py                   # SVR model and param grid
├── utils/
│   ├── preprocessing.py         # Data imputation & scaling pipeline
│   └── plot_utils.py            # Graph saving utilities
├── data/
│   └── T1.csv                   # (Place your SCADA dataset here)
```

## 📥 Dataset
The project uses the **Nordex N117 SCADA dataset**, publicly available on Kaggle:  
🔗 [Wind Turbine SCADA Dataset](https://www.kaggle.com/datasets/berkerisen/wind-turbine-scada-dataset)

Download `T1.csv` and place it inside the `data/` directory.

## 🚀 How to Run

1. Clone the repository or download it as a ZIP.
2. Ensure Python ≥3.7 is installed.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the main script:
   ```bash
   python main.py
   ```
5. The script will generate evaluation plots and a CSV file:  
   `model_performance_comparison.csv`

## 📈 Example Output
- Prediction vs Actual Line Plots
- Error Time Series
- Residual Histograms
- Scatter Plots

All plots are saved as `.png` and `.svg` files for publication use.

## 📄 License
This project is shared under the MIT License.

## ✍️ Authors
Developed by Barış Çelebi, 2025  
For academic inquiries: [GitHub Profile](https://github.com/sbariscelebi)
