# End-to-End Data Science: Car Mileage Prediction (Regression)

Welcome to the **Car Mileage Prediction** project! In this module, you'll walk through the complete data science lifecycle—from raw data to a deployed web application.

## Learning Objectives
1. Perform Exploratory Data Analysis (EDA) on real-world car specifications.
2. Clean data and engineer features (e.g., converting MPG to KMPL).
3. Build and evaluate a Random Forest Regressor model using Scikit-Learn.
4. Deploy the trained model using a full-stack Django web application with a sleek, modern, glassmorphic UI.

---

## 📂 Project Structure
- `data/`: Contains the raw dataset `auto-mpg.data`.
- `notebooks/`: Contains the Jupyter notebook `car_mileage_prediction.ipynb` where all the analysis and modeling happens.
- `models/`: Where your exported `.joblib` ML model resides.
- `webapp/`: The complete Django project that loads your model and provides a user interface.
- `requirements.txt`: Python package dependencies.
- `.gitignore`: Instructions for git properly ignore environment specifics.

---

## 🚀 Phase 1: The Data Science Lifecycle
In this phase, we analyze the data and generate our model.

### 1. Setup the Environment

It is best practice to run this project in a Python virtual environment. Here is how you can set it up from scratch depending on your operating system:

**For Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**For macOS and Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

*(Note: Ensure your virtual environment is activated before proceeding! Your terminal prompt will usually be prefixed with `(venv)`)*

### 2. Run the Notebook
Launch Jupyter Notebook to explore the steps.
```bash
jupyter notebook notebooks/car_mileage_prediction.ipynb
```
Follow the cells to watch the data transform and train the `RandomForestRegressor`. Upon successful execution of the final cell, your model will be saved to `models/car_mileage_rf_model.joblib`. 

> **Note:** If you want to bypass the notebook step and just quickly train the model to start the web app, you can run the provided python script instead: `python train_model.py`.

---

## 🌐 Phase 2: Deploying with Django
Once your model is saved, you can deploy it through the sleek Web Application built with Django.

### 1. Run the Django Server
Navigate into the `webapp` folder, make sure your virtual environment is still active, and start the python server.
```bash
cd webapp
python manage.py runserver
```

### 2. View the App
Open your web browser and go to:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Enter any vehicle's specifications (e.g., Cylinders, Weight, Horsepower, etc.) and the application will instantly predict its equivalent Kilometers Per Liter (KMPL) using your trained model in the backend!
