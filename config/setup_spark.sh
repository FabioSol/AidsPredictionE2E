#!/bin/bash

# Create necessary directories
mkdir -p /var/lib/apt/lists

# Update package list and install wget
apt-get update && apt-get install -y wget

# Download PostgreSQL JDBC driver
wget https://jdbc.postgresql.org/download/postgresql-42.7.3.jar -P /opt/bitnami/spark/jars/

# Clean up apt cache to reduce image size
apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables
export SPARK_HOME=/opt/bitnami/spark
export PATH=$SPARK_HOME/bin:$PATH

# Set Spark Master and Worker Web UI ports
export SPARK_MASTER_WEBUI_PORT=8081
export SPARK_WORKER_WEBUI_PORT=8082
