FROM apache/airflow:2.9.1-python3.11

# Install PostgreSQL driver
USER root

# Set environment variables
ENV AIRFLOW_HOME=/usr/local/airflow
# Set working directory
WORKDIR $AIRFLOW_HOME

# Copy DAGs and configuration files
COPY dags/ /usr/local/airflow/dags/
COPY config/airflow.cfg /usr/local/airflow/airflow.cfg

# Switch to airflow user
USER airflow


RUN pip install --upgrade pip

RUN pip install apache-airflow psycopg2-binary

USER root
# Expose the web server port
EXPOSE 8080