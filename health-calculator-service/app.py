import os

from flask import Flask, request, jsonify
from flasgger import Swagger

from src.health_utils import calculate_bmi, calculate_bmr
from src.health_exceptions import BMIException, BMRException

from config import SWAGGER_CONFIG

app = Flask(__name__)
swagger = Swagger(app, config=SWAGGER_CONFIG)

@app.route('/bmi', methods=['POST'])
def bmi():
    """
    Calculate Body Mass Index (BMI)
    ---
    parameters:
      - name: height
        in: formData
        type: number
        required: true
        description: Height in meters
      - name: weight
        in: formData
        type: number
        required: true
        description: Weight in kilograms
    responses:
      200:
        description: BMI calculation successful
        schema:
          type: object
          properties:
            equation:
              type: string
              example: bmi
            result:
              type: number
              format: float
      400:
        description: Invalid input or calculation error
        schema:
          type: object
          properties:
            error:
              type: string
    """
    height: float = float(request.form['height'])
    weight: float = float(request.form['weight'])

    try:
        result = calculate_bmi(height=height, weight=weight)
    except BMIException as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"equation": "bmi", "result": result}), 200

@app.route('/bmr', methods=['POST'])
def bmr():
    """
    Calculate Basal Metabolic Rate (BMR)
    ---
    parameters:
      - name: height
        in: formData
        type: number
        required: true
        description: Height in centimeters
      - name: weight
        in: formData
        type: number
        required: true
        description: Weight in kilograms
      - name: age
        in: formData
        type: integer
        required: true
        description: Age in years
      - name: gender
        in: formData
        type: string
        required: true
        description: Gender (male or female)
        enum: ['male', 'female']
    responses:
      200:
        description: BMR calculation successful
        schema:
          type: object
          properties:
            equation:
              type: string
              example: bmr
            result:
              type: number
              format: float
      400:
        description: Invalid input or calculation error
        schema:
          type: object
          properties:
            error:
              type: string
    """
    height: float = float(request.form['height'])
    weight: float = float(request.form['weight'])
    age: int = int(request.form['age'])
    gender: str = str(request.form['gender'])

    try:
        result = calculate_bmr(height=height, weight=weight, age=age, gender=gender)
    except BMRException as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"equation": "bmr", "result": result}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000), debug=os.environ.get("DEBUG", False))
