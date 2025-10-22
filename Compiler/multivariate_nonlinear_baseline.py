from mpc_math import *
import math

def func1(x):
    # f(x1, x2) = 1 / (2π * x2) * e^{-(x1^2)/(2x2)}
    x1, x2 = x[0], x[1]
    return 1 / (2 * math.pi * x2) * exp2_fx(- (x1 ** 2) / (2 * x2) / math.log(2))


def func2(x):
    # sqrt(1 + x1^2 + 2x1 cos x2)
    x1, x2 = x[0], x[1]
    return sqrt(1 + x1 ** 2 + 2 * x1 * cos(x2))

def func3(x):
    # e^{x1} * cos(x2)
    x1, x2 = x[0], x[1]
    return exp2_fx(x1 / math.log(2)) * cos(x2)

def func4(x):
    # e^{sin(x1)} * cos(x2)
    x1, x2 = x[0], x[1]
    return exp2_fx(sin(x1) / math.log(2)) * cos(x2)

def func5(x):
    # 1 / (2πx3) * e^{-((x1 - x2)^2)/(2x3)}
    x1, x2, x3 = x[0], x[1], x[2]
    exponent = -((x1 - x2) ** 2) / (2 * x3)
    return 1 / (2 * math.pi * x3) * exp2_fx(exponent / math.log(2))

def func6(x):
    # sqrt(1 + x1^2 + 2x1 cos(x2 - x3))
    x1, x2, x3 = x[0], x[1], x[2]
    return sqrt(1 + x1 ** 2 + 2 * x1 * cos(x2 - x3))

def func7(x):
    # x1 * sin^2((x2 - x3)/2) / ((x2 - x3)/2)^2
    x1, x2, x3 = x[0], x[1], x[2]
    diff = (x2 - x3) / 2
    numerator = sin(diff) ** 2
    denominator = diff ** 2
    # MP-SPDZ 没有 torch.where，可以用 if_else 替代
    is_zero = (diff == 0)
    safe_denominator = is_zero.if_else(types.sfix(1.0), denominator)
    return x1 * numerator / safe_denominator

def func8(x):
    # x1(1 + x2 cos x3)
    x1, x2, x3 = x[0], x[1], x[2]
    return x1 * (1 + x2 * cos(x3))


def func9(x):
    # x1 / ((x2-1)^2 + (x3-x4)^2 + (x5-x6)^2)
    x1, x2, x3, x4, x5, x6 = x[0], x[1], x[2], x[3], x[4], x[5]
    denominator = (x2 - 1) ** 2 + (x3 - x4) ** 2 + (x5 - x6) ** 2
    return x1 / denominator


def func15(x):
    # x1 / (exp(x2/x3) + exp(-x2/x3))
    x1, x2, x3 = x[0], x[1], x[2]
    term = x2 / x3
    exp_pos = exp2_fx(term / math.log(2))
    exp_neg = exp2_fx(-term / math.log(2))
    return x1 / (exp_pos + exp_neg)


benchmark_dict = {
    "func1":  {"func": func1,  "n_vars": 2, "domain": [(0.1, 2), (0.1, 2)]},
    "func2":  {"func": func2,  "n_vars": 2, "domain": [(-2, 2), (-math.pi, math.pi)]},
    "func3":  {"func": func3,  "n_vars": 2, "domain": [(-2, 2), (-math.pi, math.pi)]},
    "func4":  {"func": func4,  "n_vars": 2, "domain": [(-math.pi, math.pi), (-math.pi, math.pi)]},
    "func5":  {"func": func5,  "n_vars": 3, "domain": [(0, 2), (0, 2), (0.1, 2)]},
    "func6":  {"func": func6,  "n_vars": 3, "domain": [(0.1, 1.5), (0, math.pi / 2), (-math.pi / 2, 0)]},
    "func7":  {"func": func7,  "n_vars": 3, "domain": [(0, 2), (-math.pi, 0), (0, math.pi)]},
    "func8":  {"func": func8,  "n_vars": 3, "domain": [(0, 1), (0, 1), (0, math.pi)]},
    "func9":  {"func": func9,  "n_vars": 6, "domain": [(0, 1), (-1, 0), (-1, 0), (0, 1), (-1, 0), (0, 1)]},
    # "func10": {"func": func10, "n_vars": 2, "domain": [(0, 1), (0, 1)]},
    # "func11": {"func": func11, "n_vars": 2, "domain": [(0.1, 5), (0.1, 5)]},
    # "func12": {"func": func12, "n_vars": 3, "domain": [(0.1, 5), (0.1, 5), (0.1, 5)]},
    # "func13": {"func": func13, "n_vars": 4, "domain": [(0.1, 2), (0.1, 2), (0.1, 2), (0.1, 2)]},
    # "func14": {"func": func14, "n_vars": 5, "domain": [(0, 2), (0, 2), (0, 2), (0, 2), (0, 2)]},
    "func15": {"func": func15, "n_vars": 3, "domain": [(0, 1), (0, 1), (0.2, 2)]},
}
