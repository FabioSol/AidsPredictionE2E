from pyspark.sql import SparkSession
import pandas as pd
import joblib
from model.pipeline import create_pipeline
from db_config import DBConfig
import logging
import sys


def train_model():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger(__name__)

    spark = None

    try:
        spark = SparkSession.builder \
            .appName("Model Training") \
            .config("spark.jars.packages", "org.postgresql:postgresql:42.2.18") \
            .getOrCreate()

        logger.info("Spark session created")

        # Load training data from PostgreSQL
        db_config = DBConfig()
        connection_string = db_config.get_connection_string()

        # Read data from PostgreSQL into Spark DataFrame
        train_df = spark.read \
            .format("jdbc") \
            .option("url", connection_string) \
            .option("dbtable", "train_data") \
            .option("user", db_config.user) \
            .option("password", db_config.password) \
            .option("driver", "org.postgresql.Driver") \
            .load()

        logger.info("Training data loaded from PostgreSQL")

        # Convert Spark DataFrame to Pandas DataFrame
        train_pd_df = train_df.toPandas()
        logger.info("Converted Spark DataFrame to Pandas DataFrame")

        # Separate features and target
        X_train = train_pd_df.drop(columns=['target'])
        y_train = train_pd_df['target']

        # Create and train the pipeline
        pipeline = create_pipeline()
        pipeline.fit(X_train, y_train)
        logger.info("Model training completed")

        # Save the trained model
        joblib.dump(pipeline, f'/app/models/model_{1}.pkl')
        logger.info("Trained model saved")

    except Exception as e:
        logger.error(f"Error in model training: {e}")
    finally:
        if spark:
            spark.stop()
            logger.info("Spark session stopped")


if __name__ == "__main__":
    train_model()
