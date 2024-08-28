from pymongo import MongoClient
import os

CONNECTION_STRING = os.environ.get("ME_CONFIG_MONGODB_URL")


class MongoDB:
    def __init__(self, db_name: str = None, collection: str = None):
        self._client = MongoClient(CONNECTION_STRING)
        self._collection = self._client[db_name][collection]

    def get_scan_results(self):
        try:
            data = self._collection.find()
            return data
        except Exception as e:
            print(f'Exception: {e}')

    def add_scan_results(self, data: dict):
        try:
            self._collection.insert_one(data)
            return 'Scan added'
        except Exception as e:
            print(f'Exception: {e}')