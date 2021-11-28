"""Iteratieve functions.
"""
import random
import pickle

from math import *
from mpc_math import *
from Compiler.types import *
from Compiler.library import *
import Compiler.building_blocks as bb
import Compiler.ml as ml
from Compiler import comparison, instructions, instructions_base


def general_non_linear(x, coeffA, breaks):
    """The general non-linear function, defined by coeffA and breaks.

    x: sfix number.
    coeffA: sfixed matrix, in shape (m, k).
    breaks: m break_points.
    """
    m = coeffA.sizes[0]
    k = coeffA.sizes[1]

    # locate the initial bin.
    comp = sfix.Array(m)
    @for_range_opt(m)
    def _(i):
        comp[i] = x >= breaks[i]
    break_point()

    tmp = bb.get_last_one(comp)
    cipher_index = sfix.Matrix(1, m)
    @for_range_opt(m)
    def _(i):
        cipher_index[0][i] = tmp[i]

    coeffs = bb.general_dot_product(cipher_index, coeffA)
    coeffs = coeffs.transpose()

    # expansion.
    v = sfix(0)
    for i in range(k-1, -1, -1):
        v = v * x + coeffs[i]
    return v


def general_non_linear_v2(x, coeffA, breaks):
    """version 2 general noon-linear computation.
    Here coeffA is plain-text python list.
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


def general_non_linear_v3(x, coeffA, breaks):
    """version 2 general noon-linear computation.
    Here coeffA is plain-text python list.
    """
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        poss_res[i] = coeffA[i][0]
        for j in range(degree):
            poss_res[i] += pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
        poss_res[i] = poss_res[i].reduce_after_mul()

    comp = sfix.Array(m)
    @for_range_opt(m)
    def _(i):
        comp[i] = x >= breaks[i]
    cipher_index = bb.get_last_one(comp)

    return sfix.dot_product(cipher_index, poss_res)



def general_updated_non_linear(x, coeffA, breaks):
    """Using the p_eval optimizaton.

    coeffA: (k, m) matrix, each line stroes the kth order of each breaks, here coeffA is plain-text.
    """
    m = len(coeffA[0])
    k = len(coeffA)
    degree = k-1
    pre_mults = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    local_aggregation = [0]*m
    for coeffs, pre_mults in zip(coeffA[1:], pre_mults):
        for i in range(m):
            local_aggregation[i] += pre_mults.mul_no_reduce(x.coerce(coeffs[i]))
    for i in range(m):
        local_aggregation[i] = local_aggregation[i].reduce_after_mul() + coeffA[0][i]

    comp = sfix.Array(m)
    @for_range_opt(m)
    def _(i):
        comp[i] = x >= breaks[i]
    break_point()
    cipher_index = bb.get_last_one(comp)

    local_aggregation = Array.create_from(local_aggregation)
    res = sfix.dot_product(cipher_index, local_aggregation)
    
    return res


def vec_general_non_linear(x, coeffA, breaks):
    """General non-linear optimized for mp-spdz.
    """
    m = coeffA.sizes[0]
    k = coeffA.sizes[1]

    # locate the initial bin.
    comp = sfix.Array(m)
    @for_range_opt(m)
    def _(i):
        comp[i] = x >= breaks[i]
    break_point()

    tmp = bb.get_last_one(comp)
    cipher_index = sfix.Matrix(1, m)
    @for_range_opt(m)
    def _(i):
        cipher_index[0][i] = tmp[i]

    arr_list = [x]*(k-1)
    arr_list.insert(0, sfix(1))
    arr = Array.create_from(arr_list)

    arr_tmp = copy.copy(arr)
    @for_range_opt(k-1)
    def _(i):
        arr[i+regint(1)] *= arr_tmp[i]
    
    coeffs = bb.general_dot_product(cipher_index, coeffA)
    coeffs = coeffs.transpose()

    res = MemValue(sfix(0))
    @for_range_opt(k)
    def _(i):
        arr[i] *= coeffs[i]
        res.iadd(arr[i])
    
    return res


def sqrt_initial_from_bits(x):
    """get the initial guess of sqrt.
    """
    b = x.v
    k = x.k

    norm = bb.normed_bits(b, k)
    if(k%2 == 0):
        norm.insert(-1, 0)
    
    # define whether the MSB is in the odd location.
    flag_odd = 0
    for i in range(k):
        if(i%2 == 0):
            flag_odd += norm[i]

    # combine to find the initial value.
    k_over_2 = k // 2 + 1
    norm_index = [0]*k_over_2
    norm_index[0] = norm[0]
    for i in range(1, k_over_2):
        norm_index[i] = norm[2*i-1] + norm[2*i]
    init = b.bit_compose(norm_index)

    if x.f % 2 == 1:
        flag_odd =  (1 - 2 * flag_odd) + flag_odd
        init = flag_odd.if_else(init, 2*init)
    init = x._new(init << ((x.f - (x.f%2)) // 2), k=x.k, f=x.f)
    init = (init * (2**(1/2)) - init) * flag_odd + init

    return mpc_reci(init, 'from_bits')


def sqrt_initial_from_comp(x):
    """Using get_last_one
    """
    sfix.set_precision(16, 64)
    APPRO = 0.48
    scaler_list = Array.create_from([sfix(10**i) for i in range(-10, 11)])
    scaler_inv_sqrt = Array.create_from([sfix((10**(-i))**0.5) for i in range(-10, 11)])

    comp = Array(len(scaler_list), sfix)
    @for_range_opt(len(scaler_list))
    def _(i):
        comp[i] = x >= scaler_list[i]
    break_point()
    scaler_index = bb.get_last_one(comp)
    init = APPRO*sfix.dot_product(scaler_index, scaler_inv_sqrt)

    return init


def sqrt_iterative(x, init, k):
    """using privpy's method for final result.

    for initial value form bit, we set k=4.
    for initial value from comp, we set k=7.
    """
    for _ in range(k):
        init = 0.5*init*(3 - x*init*init)
    return init * x


def reci_init_from_comp(x):
    """Find the appro init from comp.
    """
    scaler_list = Array.create_from([sfix(1e-8), sfix(1e-4), sfix(1), sfix(1e4), sfix(1e8)])
    scaler_list_inv = Array.create_from([sfix(1e8), sfix(1e4), sfix(1), sfix(1e-4), sfix(1e-8)])

    comp = Array(len(scaler_list), sfix)
    @for_range_opt(len(scaler_list))
    def _(i):
        comp[i] = x < scaler_list_inv[i]
    break_point()

    scaler_index = bb.get_last_one(comp)
    init = sfix.dot_product(scaler_index, scaler_list)
    return init


def divide_iterative_newton(x, y, times = 10):
    """Using newton method for the divison of x/y.
    """
    init = reci_init_from_comp(y)

    for _ in range(times):
        tmp1 = y * init
        tmp2 = 1 - tmp1
        a = init
        s = init
        for _ in range(2):
            a = a * tmp2
            s = s + a
        init = s

    return x * init


def reci_init_from_bits(b, k, f, kappa, nearest):
    """Find the appro init from bits construction.
    """

    temp = comparison.LessThanZero(b, k, kappa)
    sign = 1 - 2 * temp
    b = sign * b

    norm = bb.normed_bits(b, k)
    scaler = sint.bit_compose(reversed(norm)) # don't have the meaning for f.
    scaled_init = b * scaler # value with the first bits be 1.
    scaled_sign = sign * scaler

    alpha = b.get_type(2 * k)(int(2.9142 * 2**k)) # <2k, k> sfixed 2.9142
    d = alpha - 2 * scaled_init
    w = d * scaled_sign
    w = w.round(2 * k + 1, 2 * (k - f), kappa, nearest, signed=True)

    return w.extend(2 * k)


def dvide_goldschmidt(x, y):
    """calculate secret x/y.
    """
    k = x.k
    f = x.f
    res_f = f
    kappa = x.kappa
    nearest = sfix.round_nearest
    f = max((k - nearest) // 2 + 1, f) # adjuest f.

    a, b = x.v, y.v
    times = int(ceil(log(k/3.5) / log(2)))

    init = reci_init_from_bits(b, k, f, kappa, nearest)
    alpha =b.get_type(2 * k).two_power(2*f)
    x = alpha - b.extend(2 * k) * init

    y = a.extend(2 * k) * init
    y = y.round(2*k, f, kappa, nearest, signed=True)

    for i in range(times - 1):
        x = x.extend(2 * k)
        y = y.extend(2 * k) * (alpha + x).extend(2 * k)
        x = x * x
        y = y.round(2*k, 2*f, kappa, nearest, signed=True)
        x = x.round(2*k, 2*f, kappa, nearest, signed=True)

    x = x.extend(2 * k)
    y = y.extend(2 * k) * (alpha + x).extend(2 * k)

    y = y.round(k + 3 * f - res_f, 3 * f - res_f, kappa, nearest, signed=True)
    y = sfix._new(y, k, res_f)
    return y


def pp_exp(x, times=4):
    """Taylors' $2^{times}$ items.
    """
    x_split = Array.create_from([sfix(3.0*i) for i in range(-8, 9)])
    ex_std = Array.create_from([sfix(math.exp(3.0*i)) for i in range(-8, 9)])

    comp = Array(len(x_split), sfix)
    @for_range_opt(len(x_split))
    def _(i):
        comp[i] = ((x - x_split[i]) >= -1)>=1
    break_point()
    exp_index = bb.get_last_one(comp)
    
    # calculate exp value
    result = sfix(1)
    x = (x - sfix.dot_product(exp_index, x_split))
    tmp1 = x
    tmp2 = sfix(1)
    val = sfix(1)
    for i in range(2**times):
        result += tmp1 * mpc_reci(tmp2)
        tmp1 *= x 
        val += sfix(1)
        tmp2 *= val

    res = sfix.dot_product(exp_index, ex_std) * result
    return res


def pp_log(x, times=5):
    """Taylor's $2^{times}$ iterms.
    """
    x_split = Array.create_from([sfix(math.exp(-2*i)) for i in range(-9, 8, 1)])
    log_std = Array.create_from([sfix(2*i) for i in range(-9, 8, 1)])

    comp = Array(len(x_split), x_split.value_type) 
    @for_range_opt(len(x_split))
    def _(i):
        comp[i] = (x*x_split[i] >= 1) >= 1
    break_point()

    log_index = bb.get_last_one(comp)
    
    # calculate the log value
    x = x*sfix.dot_product(log_index, x_split)
    x = (x-sfix(1)) * mpc_reci(x+sfix(1))
    x_sq = x*x
    tmp1 = x
    tmp2 = sfix(1)
    result = sfix(0)
    
    for i in range(1, 2**times+1):
        result += 2*tmp1*tmp2
        tmp1 *= x_sq
        tmp2 = sfix(1/(2*i+1)) 
    
    res = sfix.dot_product(log_index, log_std) + result

    return res



def mpc_sqrt(x, strategy='from_bits', coeffA=None, breaks=None):
    """sqrt functions in MPC.
    """
    if strategy not in ['from_bits', 'from_comp', 'general']:
        raise TypeError("The strategy of sqrt is not supported yet.")
    
    if strategy == 'from_bits':
        iters = 4
        init = sqrt_initial_from_bits(x)
        return sqrt_iterative(x, init, iters)
    
    if strategy == 'from_comp':
        iters = 7
        init = sqrt_initial_from_comp(x)
        return sqrt_iterative(x, init, iters)
    
    if strategy == 'general':
        return general_non_linear(x, coeffA, breaks)


def mpc_reci(x, strategy='from_bits', coeffA=None, breaks=None):
    """sqrt functions in MPC.
    """
    if strategy not in ['from_bits', 'from_comp', 'general']:
        raise TypeError("The strategy of reci is not supported yet.")
    
    if strategy == 'from_bits':
        return dvide_goldschmidt(sfix(1), x)
    
    if strategy == 'from_comp':
        return divide_iterative_newton(sfix(1), x)
    
    if strategy == 'general':
        return general_non_linear(x, coeffA, breaks)


def mpc_log(x, strategy='from_bits', coeffA=None, breaks=None):
    """log function in MPC.
    """
    if strategy not in ['from_bits', 'from_comp', 'general']:
        raise TypeError("The strategy of log is not supported yet.")
    
    if strategy == 'from_bits':
        return log_fx(x, e)
    if strategy == 'from_comp':
        return pp_log(x)
    if strategy == 'general':
        return general_non_linear(x, coeffA, breaks)


def mpc_exp(x, strategy='from_bits', coeffA=None, breaks=None):
    """exp function in MPC.
    """
    if strategy not in ['from_bits', 'from_comp', 'general']:
        raise TypeError("The strategy of log is not supported yet.")
    if strategy == 'from_bits':
        return pow_fx(sfix(e), x)
    if strategy == 'from_comp':
        return pp_exp(x)
    if strategy == 'general':
        return general_non_linear(x, coeffA, breaks)



def mpc_sigmoid(x, strategy='from_bits', coeffA=None, breaks=None):
    """Sigmoid funciton in MPC
    """
    if strategy not in ['from_bits', 'general']:
        print_ln("Not support %s yet", strategy)
        return

    # invoke mp-spdz func directly.
    if strategy == 'from_bits':
        return ml.sigmoid(x)
    
    if strategy == 'general':
        return general_non_linear(x, coeffA, breaks)

