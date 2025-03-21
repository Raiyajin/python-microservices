import unittest

from src.health_utils import calculate_bmi
from src.health_exceptions import BMIException

class TestBMI(unittest.TestCase):
    def test_bmi_weight_greater_than_height(self):
        weight: float = 100.0
        height: float = 80.0

        result = calculate_bmi(weight=weight, height=height)
        self.assertAlmostEqual(result, 156.25, places=2)

    def test_bmi_weight_lower_than_height(self):
        weight: float = 80.0
        height: float = 100.0

        result = calculate_bmi(weight=weight, height=height)
        self.assertAlmostEqual(result, 80.0, places=2)

    def test_negative_weight(self):
        weight: float = -80.0
        height: float = 100.0

        self.assertRaises(BMIException, calculate_bmi, weight=weight, height=height)

    def test_negative_height(self):
        weight: float = 80.0
        height: float = -100.0

        self.assertRaises(BMIException, calculate_bmi, weight=weight, height=height)

    def test_null_weight(self):
        weight: float = 0
        height: float = 100.0

        self.assertRaises(BMIException, calculate_bmi, weight=weight, height=height)

    def test_null_height(self):
        weight: float = 80.0
        height: float = 0

        self.assertRaises(BMIException, calculate_bmi, weight=weight, height=height)


if __name__ == '__main__':
    unittest.main()
