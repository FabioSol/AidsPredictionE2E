import os
import yaml


class ConfigReader:
    def __init__(self, config_file_path=None):
        self.config_file_path = config_file_path or 'config/config.yaml'
        self.config = self._read_config_file()

    def _read_config_file(self):
        if not os.path.exists(self.config_file_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_file_path}")

        with open(self.config_file_path, 'r') as file:
            config = yaml.safe_load(file)

        return config

    def get(self, section, key, default=None):
        return self.config.get(section, {}).get(key, default)


# Example usage
if __name__ == "__main__":
    config_reader = ConfigReader()
    db_host = config_reader.get('database', 'host', 'localhost')
    print(f"Database Host: {db_host}")
