"""The functions in DESIGN-PATTERNS.
"""

from Compiler.types import *
from Compiler.library import *


# GET-LAST-ONE and ITERATIVE Based
def get_last_one(arr, type='quick'):
    """MP-SPDZ version get_last_one.

    arr: types.Array
    """
    n = arr.length
    if type == 'robust':
        x = sfix(1)
        for i in range(n):
            arr[i] *= x
            x *= arr[i]
        @for_range_opt(n-1)
        def _(i):
            arr[i] -= arr[i+regint(1)]
        return arr

    if type == 'quick':
        last = Array(n, sfix)
        cons_none = sfix(-1)
        @for_range_opt(n-1)
        def _(i):
            last[i] = arr[i+regint(1)]*cons_none
        last[n-1] = cons_none

        return arr * (arr + last)


def pp_reciprocal(x, times=12):
    """Using iteration method defined in "ITERATIVE Based". 
    f(x) = 1/x - A, to find the reciprocal of A.
    method: ``x_{n+1} = x_{n} + x_{n}*(1-Ax_{n}) + x_{n}*(1-Ax_{n})^2``
    """
    sfix.set_precision(16, 64)
    appro_list = Array.create_from([sfix(1e-8), sfix(1e-4), sfix(1), sfix(1e4), sfix(1e8)])
    appro_list_inv = Array.create_from([sfix(1e8), sfix(1e4), sfix(1), sfix(1e-4), sfix(1e-8)])

    comp = Array(len(appro_list_inv), sfix)

    @for_range_opt(len(appro_list_inv))
    def _(i):
        comp[i] = (x < appro_list_inv[i]) >= 1
    break_point()

    appro_index = get_last_one(comp)
    appro = sfix.dot_product(appro_index, appro_list)
    
    result = appro
    for _ in range(times):
        tmp1 = x*result
        tmp2 = sfix(1) - tmp1
        a_n = result
        s_n = result
        for _ in range(2):
            a_n = a_n * tmp2
            s_n = s_n + a_n
        result = s_n
    
    return result


def pp_sqrt(x, times=6):
    """Using iterations method.
    method: ``x_{n+1} = 1/2(x_{n})(3-Ax_{n}^2)``
    """
    sfix.set_precision(16, 64)
    APPRO = sfix(0.48)
    scaler_list = Array.create_from([sfix(10**i) for i in range(-10, 11)])
    scaler_inv_sqrt = Array.create_from([sfix((10**(-i))**0.5) for i in range(-10, 11)])
    
    comp = Array(len(scaler_list), sfix)
    @for_range_opt(len(scaler_list))
    def _(i):
        comp[i] = (x >= scaler_list[i]) >= 1
    break_point()

    scaler_index = get_last_one(comp)
    APPRO = APPRO*sfix.dot_product(scaler_index, scaler_inv_sqrt)

    result = APPRO
    for _ in range(times):
        result = sfix(0.5)*result*(3 - x*result*result)
    root = result * x
    return root


def pp_exp(x, times=4):
    """Taylors' $2^{times}$ items.
    """
    sfix.set_precision(16, 64)
    x_split = Array.create_from([sfix(3.0*i) for i in range(-8, 9)])
    ex_std = Array.create_from([sfix(math.exp(3.0*i)) for i in range(-8, 9)])

    comp = Array(len(x_split), sfix)
    @for_range_opt(len(x_split))
    def _(i):
        comp[i] = ((x - x_split[i]) >= -1)>=1
    break_point()
    exp_index = get_last_one(comp)
    
    # calculate exp value
    result = sfix(1)
    x = (x - sfix.dot_product(exp_index, x_split))
    tmp1 = x
    tmp2 = sfix(1)
    val = sfix(1)
    for i in range(2**times):
        result += tmp1 * pp_reciprocal(tmp2)
        tmp1 *= x 
        val += sfix(1)
        tmp2 *= val

    res = sfix.dot_product(exp_index, ex_std) * result
    return res


def pp_log(x, times=5):
    """Taylor's $2^{times}$ iterms.
    """
    sfix.set_precision(16, 64)
    x_split = Array.create_from([sfix(math.exp(-2*i)) for i in range(-9, 8, 1)])
    log_std = Array.create_from([sfix(2*i) for i in range(-9, 8, 1)])

    comp = Array(len(x_split), x_split.value_type) 
    @for_range_opt(len(x_split))
    def _(i):
        comp[i] = (x*x_split[i] >= 1) >= 1
    break_point()

    log_index = get_last_one(comp)
    
    # calculate the log value
    x = x*sfix.dot_product(log_index, x_split)
    x = (x-sfix(1)) * pp_reciprocal(x+sfix(1))
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

# CIPHER-INDEX
def cipher_index(arr, index):
    """Making use of the parallel optimization.
    """
    index_arr = Array(len(arr), sfix)
    @for_range_opt(len(arr))
    def _(i):
        index_arr[i] = (index == i)
    break_point()
    res = sfix.dot_product(arr, index_arr)

    return res


def shuffle_first(arr, index, flag='single'):
    """SHUFFLE First the array and then fetch elements with plain cipher index.
    """
    arr.shuffle() 
    index = index.reveal()
    if(flag == 'single'):
        return arr[index]
    if(flag == 'batch'):
        res = Array(len(index), arr.value_type)
        @for_range_opt(len(index))
        def _(i):
            res[i] = arr[index[i]]
        break_point()
        return res

