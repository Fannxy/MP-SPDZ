"""Upper layer Non-linear functions.
"""
from Compiler.library import print_ln
from Compiler.types import floatingpoint, sfix
import Compiler.building_blocks as bb
import Compiler.ml as ml
from Compiler.mpc_math import sqrt, log_fx, pow_fx
import math

from Compiler import types

DEBUG = False

PAI = 3.1415926
TAU_2 = 0.959502
E = 2.718281828459045

@types.vectorize
def general_non_linear(x, coeffA, breaks, scaler):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res[i] = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j+1] * pre_muls[j] * scaler[i][j+1]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = (x >= breaks[i])
    cipher_index = bb.get_last_one(comp) 

    return sfix.dot_product(cipher_index, poss_res)


# benchmark mpc function.
def mpc_sqrt(x):
    """[summary]

    Args:
        x ([type]): [description]

    Returns:
        [type]: [description]
    """
    return sqrt(x)


def mpc_reciprocal(x):
    """[summary]

    Args:
        x ([type]): [description]
    """
    return sfix(1) / x

def mpc_log(x):
    """[summary]

    Args:
        x ([type]): [description]
    """

    return log_fx(x, E)

def mpc_exp(x):
    """[summary]

    Args:
        x ([type]): [description]
    """
    return pow_fx(sfix(E), x)

def mpc_sigmoid(x):
    """[summary]

    Args:
        x ([type]): [description]
    """
    return ml.sigmoid(x)

def mpc_tanh(x):
    """[summary]

    Args:
        x ([type]): [description]
    """
    return (mpc_exp(x) - mpc_exp(-x)) / (mpc_exp(x) + mpc_exp(-x))


def mpc_soft_plus(x):
    """[summary]

    Args:
        x ([type]): [description]
    """
    return mpc_log(1 + mpc_exp(x))


def mpc_snormal_dis(x):
    return mpc_exp((-x*x)/2) / (2*PAI)**0.5

def mpc_scauchy_dis(x):
    """[summary]

    Args:
        x ([type]): [description]
    """
    return 1 / (PAI * (1 + x*x))

def mpc_gamma_dis(x):
    return x * mpc_exp(x) / TAU_2

def mpc_chi_square(x):
    return (mpc_exp(-x/2)*x) / (4*TAU_2)

def mpc_sexp_dis(x):
    return mpc_exp(-x)

def mpc_slog_dis(x):
    return mpc_exp(-(mpc_log(x)*mpc_log(x))/2) / (x * (2*PAI)**0.5)

# benchmark plain-text function.
def snormal_dis(x):
    """https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
    """
    x = round(x, 14)
    res = round(math.exp((-x**2)/2) / math.sqrt(2*PAI), 14)
    return res


def scauchy_dis(x):
    """https://www.itl.nist.gov/div898/handbook/eda/section3/eda3663.htm
    """
    x = round(x, 14)
    res = round(1 / (PAI * (1 + x**2)), 14)
    return res


def gamma_dis(x):
    """fix gamma = 2
    https://www.itl.nist.gov/div898/handbook/eda/section3/eda366b.htm
    """
    x = round(x, 14)
    res = round(x*math.exp(-x) / TAU_2, 14)
    return res


def chi_square(x):
    """fix v = 4.
    """
    x = round(x, 14)
    res = round((math.exp(-x/2)*x) / (4*TAU_2), 14)
    return res


def sexp_dis(x):
    """https://www.itl.nist.gov/div898/handbook/eda/section3/eda3667.htm
    """
    x = round(x, 14)
    res = round(2.718281**(-x), 14)
    return res


def slog_dis(x):
    x = round(x, 14)
    res = round((math.exp(-(math.ln(x)**2)/2)) / (x*math.sqrt(2*PAI)), 14)
    return res


def sigmoid(x):
    x = round(14)
    res = round(1 / (1 + math.exp(-x)), 14)
    return res

def reciprocal(x):
    x = round(14)
    res = round(1/x, 14)
    return res

def func_exp(x):
    x = round(x, 14)
    return round(math.exp(x), 14)

def func_sqrt(x):
    x = round(x, 14)
    return round(math.sqrt(x), 14) 

def func_log(x):
    x = round(x, 14)
    return round(math.log(x), 14)