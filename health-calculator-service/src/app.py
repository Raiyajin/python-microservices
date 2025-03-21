import os

from flask import Flask, request, jsonify

from health_utils import calculate_bmi, calculate_bmr
from health_exceptions import BMIException, BMRException

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    height: float = float(request.form['height'])
    weight: float = float(request.form['weight'])

    try:
        result = calculate_bmi(height=height, weight=weight)
    except BMIException as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"equation": "bmi", "result": result}), 200

@app.route('/bmr', methods=['POST'])
def bmr():
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
