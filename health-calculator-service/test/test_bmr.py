import unittest

from src.health_utils import calculate_bmr
from src.health_exceptions import BMRException

class TestBMR(unittest.TestCase):
    def test_bmr_weight_greater_than_height(self):
        weight: float = 100.0
        height: float = 80.0
        age: int = 25
        gender: str = "male"

        result = calculate_bmr(weight=weight, height=height, age=age, gender=gender)
        self.assertAlmostEqual(result, 1670.06, places=2)

    def test_bmr_weight_lower_than_height(self):
        weight: float = 80.0
        height: float = 100.0
        age: int = 25
        gender: str = "male"

        result = calculate_bmr(weight=weight, height=height, age=age, gender=gender)
        self.assertAlmostEqual(result, 1498.10, places=2)

    def test_negative_weight(self):
        weight: float = -80.0
        height: float = 100.0
        age: int = 25
        gender: str = "male"

        self.assertRaises(BMRException, calculate_bmr, weight=weight, height=height, age=age, gender=gender)

    def test_negative_height(self):
        weight: float = 80.0
        height: float = -100.0
        age: int = 25
        gender: str = "male"

        self.assertRaises(BMRException, calculate_bmr, weight=weight, height=height, age=age, gender=gender)

    def test_null_weight(self):
        weight: float = 0
        height: float = 100.0
        age: int = 25
        gender: str = "male"

        self.assertRaises(BMRException, calculate_bmr, weight=weight, height=height, age=age, gender=gender)

    def test_null_height(self):
        weight: float = 80.0
        height: float = 0
        age: int = 25
        gender: str = "male"

        self.assertRaises(BMRException, calculate_bmr, weight=weight, height=height, age=age, gender=gender)

    def test_elderly_male_bmr(self):
        weight: float = 80.0
        height: float = 100.0
        age: int = 80
        gender: str = "male"

        result = calculate_bmr(weight=weight, height=height, age=age, gender=gender)
        self.assertAlmostEqual(result, 1185.86, places=2)

    def test_elderly_female_bmr(self):
        weight: float = 80.0
        height: float = 100.0
        age: int = 80
        gender: str = "female"

        result = calculate_bmr(weight=weight, height=height, age=age, gender=gender)
        self.assertAlmostEqual(result, 1150.75, places=2)

    def test_young_male_bmr(self):
        weight: float = 80.0
        height: float = 100.0
        age: int = 15
        gender: str = "male"

        result = calculate_bmr(weight=weight, height=height, age=age, gender=gender)
        self.assertAlmostEqual(result, 1554.87, places=2)

    def test_young_female_bmr(self):
        weight: float = 80.0
        height: float = 100.0
        age: int = 15
        gender: str = "female"

        result = calculate_bmr(weight=weight, height=height, age=age, gender=gender)
        self.assertAlmostEqual(result, 1432.20, places=2)

    def test_invalid_age(self):
        weight: float = 80.0
        height: float = 100.0
        age: int = -15
        gender: str = "male"

        self.assertRaises(BMRException, calculate_bmr, weight=weight, height=height, age=age, gender=gender)

    def test_invalid_gender(self):
        weight: float = 80.0
        height: float = 100.0
        age: int = -15
        gender: str = "invalid"

        self.assertRaises(BMRException, calculate_bmr, weight=weight, height=height, age=age, gender=gender)

if __name__ == '__main__':
    unittest.main()
