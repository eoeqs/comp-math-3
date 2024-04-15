from modules.getter import *
from modules.solver import *


def solve_integral_handler(integral_choice, lower_limit, upper_limit, accuracy, method_choice):
    integral_func = get_integral_function(integral_choice)
    try:
        if method_choice == "rectangle_left":
            result = rectangle_left_method(integral_func, lower_limit, upper_limit, accuracy)
        elif method_choice == "rectangle_right":
            result = rectangle_right_method(integral_func, lower_limit, upper_limit, accuracy)
        elif method_choice == "rectangle_middle":
            result = rectangle_middle_method(integral_func, lower_limit, upper_limit, accuracy)
        elif method_choice == "trapezoid":
            result = trapezoid_method(integral_func, lower_limit, upper_limit, accuracy)
        elif method_choice == "simpson":
            result = simpsons_method(integral_func, lower_limit, upper_limit, accuracy)
        else:
            result = "Invalid method selected."
        print("Integration result:", result)
        return str(result)
    except Exception as e:
        print("Error during integration:", e)
        return f"Error occurred during integration: {str(e)}"
