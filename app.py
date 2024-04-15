from flask import Flask, render_template, request
from modules.functions import *
from modules.solution_handler import *
from modules.validator import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', integrals=integrals)


@app.route('/solve', methods=['POST'])
def solve():
    integral_choice = int(request.form.get('integral'))
    lower_limit = replace_comma_with_dot(request.form.get('lower_limit'))
    upper_limit = replace_comma_with_dot(request.form.get('upper_limit'))
    accuracy = replace_comma_with_dot(request.form.get('accuracy'))
    method_choice = request.form.get('method')

    if not (integral_choice and method_choice):
        return render_template('index.html', integrals=integrals, error_message="All fields must be filled")

    if not (lower_limit and upper_limit and accuracy):
        return render_template('index.html', integrals=integrals, error_message="All fields must be filled")

    try:
        lower_limit = float(lower_limit)
        upper_limit = float(upper_limit)
        accuracy = float(accuracy)
    except ValueError:
        return render_template('index.html', integrals=integrals,
                               error_message="Invalid input. Please enter valid numbers.")

    valid, message = validate_input_data(lower_limit, upper_limit, accuracy, method_choice)
    if not valid:
        return render_template('index.html', integrals=integrals, error_message=message)

    result = solve_integral_handler(integral_choice, lower_limit, upper_limit, accuracy, method_choice)

    if isinstance(result, float):
        return render_template('index.html', integrals=integrals, result=result)
    else:
        return render_template('index.html', integrals=integrals, result=str(result))


if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(debug=True)
