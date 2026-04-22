import os
import joblib
import pandas as pd
from django.shortcuts import render
from django.conf import settings

# Load model globally to avoid loading on each request
MODEL_PATH = os.path.join(settings.BASE_DIR, '..', 'models', 'car_mileage_rf_model.joblib')
try:
    rf_model = joblib.load(MODEL_PATH)
except Exception as e:
    print("Warning: Could not load model. Error:", e)
    rf_model = None

def index(request):
    prediction = None
    if request.method == 'POST':
        if not rf_model:
            prediction = "Error: Model not found."
            return render(request, 'predictor/index.html', {'prediction': prediction})
            
        try:
            # Extract features from form
            cylinders = int(request.POST['cylinders'])
            displacement = float(request.POST['displacement'])
            horsepower = float(request.POST['horsepower'])
            weight = float(request.POST['weight'])
            acceleration = float(request.POST['acceleration'])
            model_year = int(request.POST['model_year'])
            origin = int(request.POST['origin'])
            
            # Create DataFrame exactly as model expects
            input_data = pd.DataFrame([{
                'cylinders': cylinders,
                'displacement': displacement,
                'horsepower': horsepower,
                'weight': weight,
                'acceleration': acceleration,
                'model_year': model_year,
                'origin': origin
            }])
            
            # Predict
            pred = rf_model.predict(input_data)[0]
            prediction = round(pred, 2)
            
        except Exception as e:
            prediction = f"Error computing prediction: {e}"
            
    return render(request, 'predictor/index.html', {'prediction': prediction})
