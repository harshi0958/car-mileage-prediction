import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

print("Starting training script...")

# 1. Load Data
file_path = 'data/auto-mpg.data'
column_names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']
df = pd.read_csv(file_path, names=column_names, delim_whitespace=True, na_values="?")

# 2. Clean Data
df = df.dropna()
df = df.drop(columns=['car_name'])

# 3. Feature Engineer
df['kmpl'] = df['mpg'] * 0.425144
df = df.drop(columns=['mpg'])

# 4. Prepare for Modeling
X = df.drop(columns=['kmpl'])
y = df['kmpl']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

numeric_features = ['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year']
numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())])

categorical_features = ['origin']
categorical_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

rf_model = Pipeline(steps=[('preprocessor', preprocessor),
                           ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))])

# 5. Train
rf_model.fit(X_train, y_train)

# 6. Evaluate
y_pred = rf_model.predict(X_test)
from sklearn.metrics import mean_squared_error, r2_score
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")
print(f"R2: {r2_score(y_test, y_pred):.2f}")

# 7. Save model
os.makedirs('models', exist_ok=True)
joblib.dump(rf_model, 'models/car_mileage_rf_model.joblib')
print("Model created successfully at models/car_mileage_rf_model.joblib")
