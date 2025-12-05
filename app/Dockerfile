FROM python:3.12-alpine

WORKDIR /app

copy . .
RUN pip install --no-cache-dir -r requirements.txt


cmd ["python", "main.py"]