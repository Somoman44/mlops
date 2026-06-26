# MLOps End-to-End: Car Price Prediction Pipeline

## 🎯 Project Overview
The main goal of this project is to explore how a data science and machine learning project should be structured and deployed in a real-world production environment. It transitions away from standard Jupyter Notebook experimentation into a fully automated, containerized workflow. 

The project answers two primary questions:
1. How to create a clean, robust API to serve a machine learning model.
2. How to automate the build and push deployment lifecycle.

## 🛠️ Key Technologies
* **scikit-learn:** For data preprocessing, pipeline construction, and model training.
* **MLflow:** For tracking experiments and model selection.
* **FastAPI:** For building a high-performance web API.
* **Pydantic:** For strict data validation and typing of API requests.
* **Docker:** For containerizing the application to ensure consistency across environments.
* **GitHub Actions:** For implementing continuous integration and continuous deployment (CI/CD).
* **Render:** For cloud hosting and deploying the containerized API.

---

## 🚀 Project Lifecycle & Methodology

### 1. Model Experimentation & Tracking
The project began by testing various machine learning models using `scikit-learn`. To ensure a structured approach to experimentation, **MLflow** was integrated to track hyperparameters, metrics, and model artifacts across different runs.

![MLflow Model Comparison](./images/mlflow.png)

### 2. Model Selection
By analyzing the metrics logged in MLflow, the **Random Forest** algorithm seemed the simplest, yet best in performance. The best-performing Random Forest model was registered and extracted for production use.

### 3. Pipeline Construction
To ensure that data preprocessing (handling categorical variables, scaling, etc.) and model prediction happen seamlessly, a clean scikit-learn `Pipeline` was constructed. This prevents data leakage and ensures the incoming API data is transformed exactly as the training data was.

![Sklearn Pipeline](./images/pipeline.png)

### 4. API Development
A robust API was developed using **FastAPI** to serve the saved model (`model.pkl`). **Pydantic** was utilized to enforce strict data validation on incoming requests, ensuring the model only receives the exact data types and categories it expects (e.g., specific fuel types, transmission, and owner histories).

### 5. Containerization
To eliminate the "it works on my machine" problem, the FastAPI application was containerized using **Docker**. A slim Python 3.13 image was used to keep the container lightweight, installing dependencies via `requirements.txt` and exposing port 8000 for the `uvicorn` server.

### 6. Cloud Deployment
The Docker image was published to DockerHub. From there, a container was spun up and hosted on **Render**, making the `/predict` API accessible over the public internet.

### 7. CI/CD Pipeline Automation
To automate the deployment process, a CI/CD pipeline was established using **GitHub Actions**. Whenever new code is pushed to the `main` branch, the workflow automatically:
1. Checks out the code.
2. Logs into Docker Hub using encrypted repository secrets.
3. Builds the updated Docker image using Docker Buildx.
4. Pushes the new `latest` tag to the Docker Hub registry.

![CI/CD Pipeline Flowchart](./images/actions.png)

---

## 💻 API Usage

The application exposes a `/predict` endpoint that accepts a POST request with car details to predict its selling price.

**Endpoint:** `POST /predict`

**Request Body (JSON):**
```json
{
  "name": "Maruti Swift Dzire VDI",
  "year": 2014,
  "km_driven": 45000,
  "fuel": "Diesel",
  "seller_type": "Individual",
  "transmission": "Manual",
  "owner": "First OWner"
}
```

**Response (JSON):**
```json
{
  "price": 450000.0
}
```