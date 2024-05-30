FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install common dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
# --no-cache-dir -r
# Copy common files
COPY . /app

# Set environment variables (if any)
ENV PYTHONUNBUFFERED=1
