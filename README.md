# 🩺 Heart Disease Prediction API  
**FastAPI + Docker + Render Deployment**

A production-ready **machine learning API** that predicts the likelihood of heart disease using a **Random Forest Classifier** trained on the UCI Heart Disease dataset.

---

## 🌐 Live Deployment
- **API Base URL:** https://heart-disease-fastapi-1.onrender.com  
- **Swagger UI:** https://heart-disease-fastapi-1.onrender.com/docs  

> ⚠️ *Note:* On Render’s free tier, the service may take **30–60 seconds** to wake up after inactivity.

---

## 🚀 Features
✅ **FastAPI** – High-performance async web framework  
✅ **Random Forest Model** trained with scikit-learn  
✅ **Pydantic** – Strict input validation  
✅ **Swagger UI** at `/docs`  
✅ **Health check & model info endpoints**  
✅ **Fully Dockerized** with Dockerfile & docker-compose  
✅ **Deployed on Render (Docker runtime)**  

---

## 🧠 API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `GET`  | `/health` | Returns API health status |
| `GET`  | `/info` | Returns model info and feature list |
| `POST` | `/predict` | Predicts heart disease + probability |

### Example Request
**POST** → `/predict`  
```json
{
  "age": 55,
  "sex": 1,
  "cp": 0,
  "trestbps": 130,
  "chol": 250,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 0,
  "thal": 2
}

## Response:

{
  "heart_disease": true,
  "probability": 0.865
}


## 📁 Project Structure

heart-disease-fastapi/
├── app/
│   ├── main.py                # FastAPI app & routes
│   └── schemas.py             # Pydantic models for validation
├── model/
│   └── heart_model.joblib     # Trained Random Forest model
├── train.py                   # Script to train and save model
├── heart.csv                  # Dataset (from Kaggle)
├── Dockerfile                 # Docker build configuration
├── docker-compose.yml         # Local Docker run setup
├── requirements.txt           # Dependencies
├── .gitignore                 # Ignore cache, venv, etc.
└── README.md                  # Project documentation


🧩 Local Development Setup
# 1️⃣ Clone the Repository

git clone https://github.com/nh246/heart-disease-fastapi.git
cd heart-disease-fastapi


# 2️ Create a Virtual Environment

python -m venv venv
# Activate it
venv\Scripts\activate     # On Windows
# source venv/bin/activate   # On macOS/Linux


# 3️⃣ Install Dependencies

pip install -r requirements.txt

# 4️⃣ Train the Model

python train.py

This will create a trained model at:

model/heart_model.joblib

# 5️⃣ Run the API Locally

 python -m uvicorn app.main:app --reload --port 5000
Then open your browser at:
👉 http://127.0.0.1:5000/docs

🐳 Run with Docker
1️⃣ Build & Run the Container

docker-compose up --build

2️⃣ Access the API


Check the API Base URL → https://heart-disease-fastapi-1.onrender.com
Swagger UI → https://heart-disease-fastapi-1.onrender.com/docs


