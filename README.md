# 🚗 Car Mileage Prediction System (End-to-End Data Science Project)

## 📌 Project Overview

This project demonstrates a complete **End-to-End Data Science Lifecycle**, from data analysis to model deployment.
It predicts the **fuel efficiency (KMPL)** of a car based on various input features such as cylinders, horsepower, weight, etc.

The project also includes a **Django Web Application** with a modern UI for real-time predictions.

---

## 🎯 Features

* 📊 Exploratory Data Analysis (EDA)
* 🧹 Data Cleaning & Feature Engineering
* 🤖 Machine Learning Model (Random Forest Regressor)
* 🌐 Django Web Application
* 🎨 Modern Glassmorphic UI Design
* ⚡ Real-time Mileage Prediction

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-Learn
* Joblib
* Django
* HTML, CSS

---

## 📂 Project Structure

```
car-mileage-prediction/
│
├── data/                 # Dataset (auto-mpg.data)
├── notebooks/            # Jupyter Notebook (EDA + Training)
├── models/               # Trained ML Model (.joblib)
├── webapp/               # Django Web Application
├── train_model.py        # Script to train model
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone Repository

```
git clone https://github.com/harshi0958/car-mileage-prediction.git
cd car-mileage-prediction
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install django pandas numpy scikit-learn joblib matplotlib seaborn
```

### 4️⃣ Run Django Server

```
cd webapp
python manage.py runserver
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:8000/
```

---

## 📸 Output Screenshots
* Home Page UI
  <img width="1919" height="974" alt="image" src="https://github.com/user-attachments/assets/b83754c8-dc66-47cd-b8b8-2ac5399b02e7" />

* Prediction Result
<img width="1918" height="954" alt="image" src="https://github.com/user-attachments/assets/4897ed96-6407-4935-aeec-f43124e8acd3" />

---

## 📈 Model Details

* Algorithm: **Random Forest Regressor**
* Target: **KMPL (Kilometers Per Liter)**
* Input Features:

  * Cylinders
  * Displacement
  * Horsepower
  * Weight
  * Acceleration
  * Model Year
  * Origin

---

## 🚀 Future Improvements

* Deploy on cloud (Render / Railway)
* Add user authentication
* Improve model accuracy
* Add more datasets

---

## 👨‍💻 Author

**Harshit Jariwala**
MCA Student | Aspiring Software Engineer

🔗 GitHub: https://github.com/harshi0958

---

## ⭐ Conclusion

This project showcases the integration of **Machine Learning + Web Development**, making it a complete real-world application.

If you like this project, give it a ⭐ on GitHub!
