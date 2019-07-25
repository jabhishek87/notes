import os
import unittest
import json

from faker import Faker

import main
from api.db import init_db

os.environ['DB_NAME'] = 'test.db'
init_db()

BASE_URL = 'http://127.0.0.1:5000/notes'

NUM_REC = 10
fake = Faker()
RECORDS = [(fake.name(), fake.text()) for i in range(NUM_REC)]


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True
        self.create_test_data()

    def create_test_data(self):
        for rec in RECORDS:
            payload = {"name": rec[0], "data": rec[1]}
            response = self.app.post(
                BASE_URL, data=json.dumps(payload)
            )
            self.assertEqual(response.status_code, 201)

    def test_get_all(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), NUM_REC)

    def _delete_all_test_data(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        for rec in data:
            url = BASE_URL + '/' + rec["uuid"]
            response = self.app.delete(url)
            self.assertEqual(response.status_code, 204)

    def tearDown(self):
        self._delete_all_test_data()


if __name__ == '__main__':
    unittest.main()
