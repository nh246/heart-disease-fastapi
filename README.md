# Heart Disease Prediction API  
**FastAPI + Docker + Render Deployment**

A production-ready machine learning API that predicts heart disease using a **Random Forest Classifier** trained on the UCI Heart Disease dataset.

---

## Live Deployment
- **Render URL**: https://heart-disease-fastapi.onrender.com  
- **Swagger UI**: https://heart-disease-fastapi.onrender.com/docs

> Note: Free tier may take 30–60 seconds to wake up on first visit.

---

## Features
- **FastAPI** with Pydantic input validation
- **Random Forest Model** (saved as `model/heart_model.joblib`)
- Fully **Dockerized** with `Dockerfile` and `docker-compose.yml`
- Interactive **Swagger UI** (`/docs`)
- Health check & model info endpoints
- Deployed on **Render** (Docker runtime)

---

## API Endpoints

| Method | Endpoint     | Description |
|--------|--------------|-----------|
| `GET`  | `/health`    | Returns `{"status": "healthy"}` |
| `GET`  | `/info`      | Returns model type and feature list |
| `POST` | `/predict`   | Predicts heart disease + probability |

---

## Project Structure

heart-disease-fastapi/
├── app/
│   ├── main.py      → FastAPI app with endpoints
│   └── schemas.py   → Pydantic input model
├── model/
│   └── heart_model.joblib → Trained ML model
├── train.py         → Script to train and save model
├── heart.csv        → Dataset (source: Kaggle)
├── Dockerfile       → Docker image build
├── docker-compose.yml → Local Docker run
├── requirements.txt → Python dependencies
├── .gitignore       → Excludes venv, cache
└── README.md        → This file


---

## Local Development

### 1. Clone the Repository
```bash
git clone https://github.com/nh246/heart-disease-fastapi.git
cd heart-disease-fastapi

2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

3. Install Dependencies

pip install -r requirements.txt

4. Train the Model

python train.py

5. Run the API
python -m uvicorn app.main:app --reload --port 5000

## Run with Docker
docker-compose up --build