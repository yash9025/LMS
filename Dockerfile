FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

# Install dependencies first for layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code into container
COPY . .

# Expose application port
EXPOSE 5000

# Start the Library Management System app
CMD ["python", "app.py"]

