FROM bitnami/spark:latest

# Switch to root to perform privileged tasks
USER root

# Set working directory
WORKDIR /app

# Copy setup script
COPY config/setup_spark.sh /app/setup_spark.sh

# Run setup script
RUN chmod +x /app/setup_spark.sh && /app/setup_spark.sh

# Switch back to the non-root user
USER 1001

# Copy additional scripts if needed
COPY scripts/ /app/scripts/
