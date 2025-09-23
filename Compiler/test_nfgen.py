from Compiler import types
from Compiler import instructions_base
# from Compiler import floatingpoint, sfix
from Compiler.types import floatingpoint, sfix


# @types.vectorize
# @instructions_base.sfix_cisc
def sigmoid(x):
    """Version2 of general non linear function.

    Args:
        x (Sfixed): the input secret value.
        coeffA (plain-text 2d python list): The plain-text coefficient of specific non-linear functions.
        breaks (plain-text 1d python list): The plain-rext break points of specific functions.

    Returns:
        Sfixed: f(x) value of specific non-lnear function f.
    """
    breaks = [-10.0, -7.5, -5.0, -2.5, -1.25, 0.0, 1.25]
    coeffA = [[2327623.5660347347, 1135624.4320527615, 225130.4859415218, 22606.56532047838, 1147.23732883095, 23.49474098284], [6840626.696839859, 4260240.813423073, 1095826.6954651054, 144624.14700706804, 9742.75732944222, 266.87962077513], [10039104.799352674, 7246826.702489181, 2211700.750823196, 352899.0235916331, 29129.89500094546, 985.28010485623], [8397728.574712092, 4172356.768375992, -133657.26629443915, -558978.6751765517, -151630.61555578973, -13622.66763747881], [8389261.744966444, 4219387.952647449, 117270.78788820832, -224418.3553327628, 0.0, 0.0], [8389261.744966444, 4219387.952647456, -117270.7878882195, -224418.35533275924, 0.0, 0.0], [7429368.452834341, 6328811.362667653, -1749559.3147501764, 243146.5265198356, -16814.98608190532, 460.19545475451]]
    scaler = [[5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 1.0, 1.0], [5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08, 5.96e-08]]
    
    m = len(coeffA)
    k = len(coeffA[0])
    degree = k-1
    
    pre_muls = floatingpoint.PreOpL(lambda a,b,_: a * b, [x] * degree)

    poss_res = [0]*m
    for i in range(m):
        # poss_res[i] = coeffA[i][0] * scaler[i][0]
        poss_res0 = coeffA[i][0] * scaler[i][0]
        for j in range(degree):
            # poss_res[i] += coeffA[i][j+1] * pre_muls[j] * scaler[i][j+1]
            tmp = pre_muls[j].mul_no_reduce(x.coerce(coeffA[i][j+1]))
            poss_res[i] += tmp.mul_no_reduce(x.coerce(scaler[i][j+1]))
        poss_res[i].reduce_after_mul() + poss_res0
    # return

    # comp = sbit.Array(m)
    # for i in range(m):
    #     comp[i] = (x >= breaks[i])
    # # return
    # cipher_index = sbit.Array(m)
    # for i in range(m-1):
    #     cipher_index[i] = (comp[i] ^ comp[i+1])
    # cipher_index[m-1] = comp[m-1]
    comp = [x >= breaks[i] for i in range(m)]
    # return
    cipher_index = [comp[i] ^ comp[i+1] for i in range(m-1)] + [comp[m-1]]
    # return 
    
    # cipher_index = Array(m, sfix)
    # @for_range_opt(m-1)
    # def _(i):
    #     cipher_index[i] = comp[i+regint(1)]
    #     cipher_index[i] = comp[i]*(comp[i] ^ cipher_index[i])

    return sfix.dot_product(cipher_index, poss_res)