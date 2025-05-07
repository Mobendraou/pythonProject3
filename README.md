# Waze User Behavior Analysis

This project analyzes user behavior data from the Waze app to understand patterns, identify outliers, and explore churn rates. The analysis includes visualizations like box plots, histograms, pie charts, and scatter plots to derive insights from the dataset.

## 📊 Features
- **Exploratory Data Analysis (EDA)**: Visualize distributions of key metrics (`sessions`, `drives`, `device` usage, etc.).
- **Outlier Handling**: Imputes extreme values using the 95th percentile threshold.
- **Churn Analysis**: Examines churn rates based on driving behavior (`km_per_driving_day`, `driving_days`).
- **Derived Metrics**: Computes ratios like `monthly_drives_per_session_ratio` and `percent_sessions_in_last_month`.

## 🛠️ Dependencies
- Python 3.x
- Libraries:
  ```bash
  pandas matplotlib seaborn
