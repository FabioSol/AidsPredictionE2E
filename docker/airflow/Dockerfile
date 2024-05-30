FROM apache/airflow:2.1.2

# Set working directory
WORKDIR /usr/local/airflow

# Copy DAGs
COPY dags/ /usr/local/airflow/dags/

# Copy configuration files if needed
COPY config/airflow.cfg /usr/local/airflow/airflow.cfg

# Expose the web server port
EXPOSE 8080

