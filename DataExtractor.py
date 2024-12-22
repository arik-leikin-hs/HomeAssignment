import json
from urllib.request import urlopen
from typing import List, Dict
import os


class DataExtractor:
    def __init__(self):
        pass

    def fetch_data_url(self, source: str) -> List[Dict]:
        try:
            with urlopen(source) as response:
                data = json.loads(response.read().decode())
            return data
        except Exception as e:
            raise ValueError(f"Failed to fetch data from URL: {e}")

    def fetch_data_json(self, source: str) -> List[Dict]:
        try:
            if os.path.exists(source):
                with open(source, "r") as file:
                    data = json.load(file)
            else:
                data = json.loads(source)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON string provided.")
        except FileNotFoundError:
            raise ValueError(f"File not found: {source}")
        except Exception as e:
            raise ValueError(f"Error processing the source: {e}")

        return data
