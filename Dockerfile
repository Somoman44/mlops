from python:3.13-slim
workdir /workspace
copy requirements.txt .
run pip install --no-cache-dir -r requirements.txt
copy . .
expose 8000
env MODEL_PATH=/workspace/saved_pipeline/model.pkl
cmd ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]