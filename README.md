# 🛡️ Insurance Premium Prediction App

A machine learning web application to predict **insurance premium categories** (Low, Medium, High)  
based on user details like age, BMI, income, occupation, and lifestyle.  
It features a **FastAPI backend** for inference and a **Streamlit frontend** for user interaction.

---

## 🚀 Features

- 🔮 Predicts premium category using a trained ML model.
- 🧠 Model enhanced with BMI, city tier, age group, and lifestyle risk.
- 🖥️ Backend API powered by **FastAPI**.
- 🌐 User-friendly interface built with **Streamlit**.
- 📦 Fully **Dockerized** for streamlined deployment.

---

## 🏗️ Tech Stack

- Python 3.10+
- FastAPI
- Streamlit
- scikit-learn
- pandas, numpy, seaborn, matplotlib
- Docker

---

## 🧪 How to Run Locally

### Create virtual env
python -m venv myenv
myenv\Scripts\activate   # On Windows
source myenv/bin/activate  # On Linux/macOS

pip install -r requirements.txt
uvicorn app:app --reload
This will start the API at: http://127.0.0.1:8000
You can test it at: http://127.0.0.1:8000/docs
streamlit run frontend/app1.py

## run on docker
docker build -t insurance-prediction .
docker run -p 8000:8000 -p 8501:8501 insurance-prediction
### 1. Clone the repository
```bash
git clone https://github.com/your-username/insurance-prediction-app.git
cd insurance-prediction-app
