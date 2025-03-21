from src.health_exceptions import BMIException, BMRException

def calculate_bmi(height: float, weight: float) -> float:
    """
    Calculate Body Mass Index (BMI) given height in meters and weight in kilograms.

    :param height: height in centimeters
    :param weight: weight in kilograms
    :return:
    """
    if height <= 0 or weight <= 0:
        raise BMIException("Invalid height or weight")

    # Convert height to meters
    height = height / 100

    return weight/(height**2)

def calculate_bmr(height: float, weight: float, age: int, gender: str) -> float:
    """
    Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation.

    :param height: height in centimeters
    :param weight: weight in kilograms
    :param age: age in years
    :param gender: gender can be 'male', 'm' or 'female', 'f'. Is not case-sensitive
    :return:
    """
    if height <= 0 or weight <= 0 or age <= 0:
        raise BMRException("Invalid height, weight, or age")

    match gender.lower():
        case "male" | "m":
            return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        case "female" | "f":
            return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        case _:
            raise BMRException("Invalid gender")
