from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import logging
import sys
from db_config import DBConfig

def ingest_data():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger(__name__)
    spark = None
    try:
        spark = SparkSession.builder \
            .appName("Data Ingestion") \
            .config("spark.jars.packages", "org.postgresql:postgresql:42.2.18") \
            .getOrCreate()

        logger.info("Spark session created")

        # Read the CSV file from the URL
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00222/data.csv'
        df = spark.read.csv(url, header=True, inferSchema=True)
        logger.info("Data read from URL")

        # Rename columns to match database schema
        df = df.withColumnRenamed("time", "time_feature")
        df.drop("pidnum")
        logger.info("Columns renamed")

        # Get the database connection string
        db_config = DBConfig()
        connection_string = db_config.get_connection_string()

        # Write DataFrame to PostgreSQL
        df.write \
            .format("jdbc") \
            .option("url", connection_string) \
            .option("dbtable", "train_data") \
            .option("user", db_config.user) \
            .option("password", db_config.password) \
            .option("driver", "org.postgresql.Driver") \
            .mode("append") \
            .save()

        logger.info("Data written to PostgreSQL")
    except Exception as e:
        logger.error(f"Error in data ingestion: {e}")
    finally:
        spark.stop()
        logger.info("Spark session stopped")

if __name__ == "__main__":
    ingest_data()
