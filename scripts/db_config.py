import os

class DBConfig:
    def __init__(self):
        self.host = os.getenv('DB_HOST', 'localhost')
        self.port = os.getenv('DB_PORT', '5432')
        self.dbname = os.getenv('DB_NAME', 'airflow')
        self.user = os.getenv('DB_USER', 'airflow')
        self.password = os.getenv('DB_PASSWORD', 'airflow')

    def get_connection_string(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"

