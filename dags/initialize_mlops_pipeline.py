from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'initialize_mlops_pipeline',
    default_args=default_args,
    description='DAG to initialize MLOps pipeline',
    schedule_interval=None,  # Run manually
    start_date=days_ago(1),
    catchup=False,
) as dag:

    ingest_task = SparkSubmitOperator(
        task_id='ingest_data',
        application='/app/scripts/spark_data_ingestion.py',
        conn_id='spark_default',
        verbose=True
    )

    train_task = SparkSubmitOperator(
        task_id='train_model',
        application='/app/scripts/spark_model_training.py',
        conn_id='spark_default',
        verbose=True
    )


    ingest_task >> train_task

