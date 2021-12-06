"""Upper layer Non-linear functions.
"""
from Compiler.library import print_ln
from Compiler.types import floatingpoint, sfix
import Compiler.building_blocks as bb
import Compiler.ml as ml
from Compiler.mpc_math import sqrt, log_fx, pow_fx


DEBUG = True

PAI = 3.1415926
TAU_2 = 0.959502
E = 2.718281828459045

def general_non_linear(x, coeffA, breaks):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plainn-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res[i] = coeffA[i][0]
        for j in range(degree):
            poss_res[i] += coeffA[i][j+1] * pre_muls[j]

    comp = sfix.Array(m)
    for i in range(m):
        comp[i] = (x >= breaks[i])
    cipher_index = bb.get_last_one(comp)

    return sfix.dot_product(cipher_index, poss_res)

def mpc_sqrt(x):
    """[summary]

    Args:
        x ([type]): [description]

    Returns:
        [type]: [description]
    """
    if DEBUG:
        print("compile - sqrt")
        print_ln("execute - sqrt")
    return sqrt(x)


def mpc_reciprocal(x):
    """[summary]

    Args:
        x ([type]): [description]
    """
    if DEBUG:
        print("compile - reciprocal")
        print_ln("execute - reciprocal")
    return sfix(1) / x

def mpc_log(x):
    """[summary]

    Args:
        x ([type]): [description]
    """
    if DEBUG:
        print_ln("in log")
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
    if DEBUG:
        print_ln("in sigmoid")
    return ml.sigmoid(x)

def mpc_tanh(x):
    """[summary]

    Args:
        x ([type]): [description]
    """
    if DEBUG:
        print_ln("in tanh")
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
    if DEBUG:
        print_ln("in log dis")
    return mpc_exp(-(mpc_log(x)*mpc_log(x))/2) / (x * (2*PAI)**0.5)

