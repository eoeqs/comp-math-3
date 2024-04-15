import sympy as sp

integrals = {
    1: r"-x^{3} - x^{2} - 2x + 1",
    2: r"-3x^{3} - 5x^{2} + 4x - 2",
    3: r"-x^{3} - x^{2} + x + 3"
}


def integral1(x):
    return -x ** 3 - x ** 2 - 2 * x + 1


def integral2(x):
    return -3 * x ** 3 - 5 * x ** 2 + 4 * x - 2


def integral3(x):
    return -x ** 3 - x ** 2 + x + 3


integral_latex_1 = sp.latex(sp.sympify(integral1(sp.symbols('x'))))
integral_latex_2 = sp.latex(sp.sympify(integral2(sp.symbols('x'))))
integral_latex_3 = sp.latex(sp.sympify(integral3(sp.symbols('x'))))

integral_latex = {
    1: integral_latex_1,
    2: integral_latex_2,
    3: integral_latex_3,
}
