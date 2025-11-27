# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
# Pythondontwritebytecode: Prevents Python from writing pyc files to disc
# Pythonunbuffered: Prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory in the container
WORKDIR /app

# Install system dependencies
# We need default-libmysqlclient-dev and build-essential for mysqlclient
RUN apt-get update && apt-get install -y \
    pkg-config \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8080

# Default command (can be overridden by App Platform settings)
CMD ["gunicorn", "applaude_backend.wsgi:application", "--bind", "0.0.0.0:8080"]
