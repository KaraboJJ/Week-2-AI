# Crop Yield Prediction with Machine Learning (SDG 2: Zero Hunger)

This project uses **machine learning** to predict crop yields based on environmental and agricultural inputs, directly supporting the **United Nations Sustainable Development Goal 2 – Zero Hunger**. By offering accurate predictions, the tool helps farmers, NGOs, and governments make better decisions about food production and distribution.

---

## Project Highlights

- **SDG Focus**: SDG 2 – Zero Hunger
- **ML Technique**: Supervised Learning (Random Forest Regressor)
- **Goal**: Predict crop yield (in tons per hectare) using data like rainfall, temperature, fertilizer use, crop type, soil type, and region
- **Interface**: Streamlit web app for real-time user interaction

---

## Quick Start

### 1. Clone the Repository

git clone https://github.com/KaraboJJ/Week-2-AI.git
cd crop-yield-predictor

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Train the Model (optional)

To train the model using synthetic or real data, run the Python training script or notebook:

jupyter notebook crop_yield_prediction.ipynb
This will generate a file: crop_yield_model.pkl

### 4. Run the Streamlit App

streamlit run app.py

### Tools Used

Python, Pandas, Scikit-learn
RandomForestRegressor for supervised regression
Joblib for model serialization
Streamlit for building a web interface

### Input Features

| Feature          | Type        | Description                     |
| ---------------- | ----------- | ------------------------------- |
| Crop             | Categorical | Wheat, Rice, Maize              |
| Region           | Categorical | Asia, Africa, Europe            |
| Soil\_Type       | Categorical | Sandy, Loamy, Clay              |
| Rainfall (mm)    | Numerical   | Total rainfall                  |
| Temperature (°C) | Numerical   | Average temperature             |
| Fertilizer\_Used | Numerical   | Fertilizer applied (kg/hectare) |

Output: Predicted Yield in tons/hectare.

### Model Performance (Sample Data)

R² Score: ~0.87
MAE: ~0.85 tons/ha
RMSE: ~1.1 tons/ha

### SDG Impact

By accurately predicting crop yields:

Farmers can optimize resource use and increase output
Governments & NGOs can plan food distribution more effectively
Waste and food insecurity can be reduced

### Ethical Considerations

Data Bias: Model performance may drop for underrepresented regions
Sustainability: Encourages efficient fertilizer use and climate-aware planning
Accessibility: Plans to extend model access to mobile and offline users

### File Structure

├── app.py                    # Streamlit app
├── crop_yield_model.pkl      # Saved ML model
├── crop_yield_prediction.ipynb # Model training & evaluation notebook
├── requirements.txt          # Required packages
└── README.md                 # Project overview



