def validate_input_data(lower_limit, upper_limit, accuracy, method):
    if lower_limit >= upper_limit:
        return False, "Lower limit should be less than upper limit."
    if accuracy <= 0:
        return False, "Accuracy should be greater than zero."
    if method not in ["rectangle_left", "rectangle_right", "rectangle_middle", "trapezoid", "simpson"]:
        return False, "Invalid integration method selected."
    return True, None


def replace_comma_with_dot(value):
    return value.replace(',', '.')
