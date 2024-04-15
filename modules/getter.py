from modules.functions import *


def get_value():
    value = input().strip()
    value = value.replace(',', '.')
    return value


def get_integral_function(choice):
    integrals = {
        1: integral1,
        2: integral2,
        3: integral3,
        4: integral4,
        5: integral5,
    }
    return integrals.get(choice)
