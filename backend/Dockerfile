FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

# Add to your backend Dockerfile temporarily for testing
RUN pip install pytest
CMD ["pytest"]
