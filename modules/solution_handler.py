from modules.getter import *
from modules.solver import *


def solve_integral_handler(integral_choice, lower_limit, upper_limit, accuracy, method_choice):
    integral_func = get_integral_function(integral_choice)
    if not check_convergence(integral_func, lower_limit, upper_limit):
        return "Integral does not exist", 0

    try:
        if method_choice == "rectangle_left":
            result, divisions = rectangle_left_method(integral_func, lower_limit, upper_limit, accuracy)
        elif method_choice == "rectangle_right":
            result, divisions = rectangle_right_method(integral_func, lower_limit, upper_limit, accuracy)
        elif method_choice == "rectangle_middle":
            result, divisions = rectangle_middle_method(integral_func, lower_limit, upper_limit, accuracy)
        elif method_choice == "trapezoid":
            result, divisions = trapezoid_method(integral_func, lower_limit, upper_limit, accuracy)
        elif method_choice == "simpson":
            result, divisions = simpsons_method(integral_func, lower_limit, upper_limit, accuracy)
        else:
            result = "Invalid method selected."
            divisions = 0

        print("Integration result:", result)
        return result, divisions
    except Exception as e:
        print("Error during integration:", e)
        return f"Error occurred during integration: {str(e)}", 0


def check_convergence(integral_func, lower_limit, upper_limit):
    try:
        # Проверяем сходимость интеграла, вычисляя его значение на конечном отрезке
        value, _ = rectangle_middle_method(integral_func, lower_limit, upper_limit, accuracy=1e-6)
        return True  # Если удалось вычислить значение, считаем интеграл сходящимся
    except Exception:
        return False


def get_infinite_discontinuity_points(integral_func, lower_limit, upper_limit):
    points = []  # точки разрыва
    types = []  # типы разрыва (левый, правый, на отрезке)

    try:  # проверка разрыва на левом конце
        integral_func(lower_limit)
    except Exception:
        points.append(lower_limit)
        types.append("left")

    try:  # проверка разрыва на правом конце
        integral_func(upper_limit)
    except Exception:
        points.append(upper_limit)
        types.append("right")

    for x in range(lower_limit + 1, upper_limit):  # проверка разрыва в точке х
        try:
            integral_func(x)
        except Exception:
            points.append(x)
            types.append("inside")

    return points, types
