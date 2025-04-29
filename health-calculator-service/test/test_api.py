import json
import unittest

from app import app

class TestAPI(unittest.TestCase):
    def test_valid_bmi(self):
        with app.test_client() as client:
            response = client.post('/bmi', data={"height": 180, "weight": 80})
            data = json.loads(response.data)

            assert response.status_code == 200
            self.assertAlmostEqual(data["result"], 24.69, places=2)
            assert data["equation"] == "bmi"

    def test_valid_bmr(self):
        with app.test_client() as client:
            response = client.post('/bmr', data={"height": 180, "weight": 80, "age": 25, "gender": 'm'})
            data = json.loads(response.data)

            assert response.status_code == 200
            self.assertAlmostEqual(data["result"], 1882.02, places=2)
            assert data["equation"] == "bmr"

    def test_invalid_data_bmi(self):
        with app.test_client() as client:
            response = client.post('/bmi', data={"height": 180, "weight": -80})
            assert response.status_code == 400

    def test_invalid_data_bmr(self):
        with app.test_client() as client:
            response = client.post('/bmr', data={"height": 180, "weight": -80, "age": 25, "gender": 'm'})
            assert response.status_code == 400

    def test_invalid_schema_bmi(self):
        with app.test_client() as client:
            response = client.post('/bmi', data={"height": 180})
            assert response.status_code == 400

    def test_invalid_schema_bmr(self):
        with app.test_client() as client:
            response = client.post('/bmr', data={"height": 180})
            assert response.status_code == 400

    def test_invalid_path(self):
        with app.test_client() as client:
            response = client.post('/invalid', data={"height": 180, "weight": 80})
            assert response.status_code == 404