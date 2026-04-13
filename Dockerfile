# Dockerfile
# Author: Golla Nikhil - 2022BCS0077

FROM python:3.10-slim

LABEL maintainer="Golla Nikhil - 2022BCS0077"
LABEL description="ML Model Serving Container | Golla Nikhil | 2022BCS0077"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY model.pkl .
COPY train.py .

# Simple serve script
COPY serve.py .

EXPOSE 8080

CMD ["python", "serve.py"]
