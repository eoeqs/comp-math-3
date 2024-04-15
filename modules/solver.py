def rectangle_left_method(integral_func, lower_limit, upper_limit, accuracy):
    n = 4
    k = 2
    prev_result = 0
    while True:
        result = 0
        width = (upper_limit - lower_limit) / n
        for i in range(n):
            result += integral_func(lower_limit + i * width)
        result *= width
        if abs(result - prev_result) < accuracy:
            return result
        prev_result = result
        n *= 2
        half_result = 0
        half_width = width / 2
        for i in range(n):
            half_result += integral_func(lower_limit + i * half_width)
        half_result *= half_width
        error = abs(half_result - result) / (2 ** k - 1)
        if error < accuracy:
            return half_result


def rectangle_right_method(integral_func, lower_limit, upper_limit, accuracy):
    n = 4
    k = 2
    prev_result = 0
    while True:
        result = 0
        width = (upper_limit - lower_limit) / n
        for i in range(1, n + 1):
            result += integral_func(lower_limit + i * width)
        result *= width
        if abs(result - prev_result) < accuracy:
            return result
        prev_result = result
        n *= 2
        half_result = 0
        half_width = width / 2
        for i in range(n):
            half_result += integral_func(lower_limit + i * half_width)
        half_result *= half_width
        error = abs(half_result - result) / (2 ** k - 1)
        if error < accuracy:
            return half_result


def rectangle_middle_method(integral_func, lower_limit, upper_limit, accuracy):
    n = 4
    k = 2
    prev_result = 0
    while True:
        result = 0
        width = (upper_limit - lower_limit) / n
        for i in range(n):
            result += integral_func(lower_limit + (i + 0.5) * width)
        result *= width
        if abs(result - prev_result) < accuracy:
            return result
        prev_result = result
        n *= 2
        half_result = 0
        half_width = width / 2
        for i in range(n):
            half_result += integral_func(lower_limit + i * half_width)
        half_result *= half_width
        error = abs(half_result - result) / (2 ** k - 1)
        if error < accuracy:
            return half_result


def trapezoid_method(integral_func, lower_limit, upper_limit, accuracy):
    n = 4
    k = 2
    prev_result = 0
    while True:
        result = 0
        width = (upper_limit - lower_limit) / n
        result += (integral_func(lower_limit) + integral_func(upper_limit)) / 2
        for i in range(1, n):
            result += integral_func(lower_limit + i * width)
        result *= width
        if abs(result - prev_result) < accuracy:
            return result
        prev_result = result
        n *= 2
        half_result = 0
        half_width = width / 2
        for i in range(n):
            half_result += integral_func(lower_limit + i * half_width)
        half_result *= half_width
        error = abs(half_result - result) / (2 ** k - 1)
        if error < accuracy:
            return half_result


def simpsons_method(integral_func, lower_limit, upper_limit, accuracy):
    n = 4
    k = 4
    prev_result = 0
    while True:
        result = 0
        width = (upper_limit - lower_limit) / n
        result += integral_func(lower_limit) + integral_func(upper_limit)
        for i in range(1, n):
            if i % 2 == 0:
                result += 2 * integral_func(lower_limit + i * width)
            else:
                result += 4 * integral_func(lower_limit + i * width)
        result *= width / 3
        if abs(result - prev_result) < accuracy:
            return result
        prev_result = result
        n *= 2
        half_result = 0
        half_width = width / 2
        for i in range(n):
            half_result += integral_func(lower_limit + i * half_width)
        half_result *= half_width
        error = abs(half_result - result) / (2 ** k - 1)
        if error < accuracy:
            return half_result


