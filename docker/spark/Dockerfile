# Download PostgreSQL driver
FROM bitnami/spark:latest
# Switch to root to perform privileged tasks
USER root

# Set working directory
WORKDIR /app

# Create necessary directories, update, install wget, download JDBC driver
RUN mkdir -p /var/lib/apt/lists && \
    apt-get update && \
    apt-get install -y wget && \
    wget https://jdbc.postgresql.org/download/postgresql-42.7.3.jar -P /opt/bitnami/spark/jars/ && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Switch back to the non-root user
USER 1001

# Copy scripts
COPY scripts/ /app/scripts/
# Set environment variables
ENV SPARK_HOME=/opt/bitnami/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Set Spark Master and Worker Web UI ports
ENV SPARK_MASTER_WEBUI_PORT=8081
ENV SPARK_WORKER_WEBUI_PORT=8082
