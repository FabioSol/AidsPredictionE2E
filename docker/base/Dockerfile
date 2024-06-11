FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install common dependencies
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
# --no-cache-dir -r
# Copy common files
RUN git clone https://github.com/FabioSol/AidsModel.git /app/model

COPY . /app

# Set environment variables (if any)
ENV PYTHONUNBUFFERED=1
