"""building blocks for design patterns.
"""
from Compiler.types import *
from Compiler.library import *

def get_last_one(arr, type='quick'):
    """
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
        @for_range_opt(n-1)
        def _(i):
            last[i] = arr[i+regint(1)]
            arr[i] = arr[i]*(arr[i] - last[i])
        arr[n-1] = arr[n-1]*(arr[n-1] - sfix(1))
        return arr


def general_dot_product(arr1, arr2):
    """A general type of dot_product.
    """
    if isinstance(arr1, Array):
        assert isinstance(arr2, Array)
        assert arr1.length == arr2.length
        return arr1[0].type.dot_product(arr1, arr2)
    
    else:
        assert len(arr1.sizes) >= 2
        assert len(arr2.sizes) >= 2
        r1, c1 = arr1.sizes
        r2, c2 = arr2.sizes
        assert c1 == r2

        arr2 = arr2.transpose()
        res = arr1[0].value_type.Matrix(r1, c2)

        @for_range_opt_multithread(None, r1)
        def _(i):
            @for_range_opt_multithread(None, c2)
            def _(j):
                row = arr1[i]
                col = arr2[j]
                res[i][j] = row.value_type.dot_product(row, col)
        return res


def normed_bits(b, k):
    """find the bits index array of 2^m where 2^{m-1} <= x < 2^m.
    b: the integet value of x.
    k: bit-length of x.
    """
    x_order = b.bit_decompose(k) # require some bits operations.
    x = [0] * k
    # x i now inverted
    for i in range(k - 1, -1, -1):
        x[k - 1 - i] = x_order[i]
    # y is inverted for PReOR and then restored
    y_order = floatingpoint.PreOR(x)
    y = [0] * k
    for i in range(k - 1, -1, -1):
        y[k - 1 - i] = y_order[i]

    # obtain z
    norm = [0] * k
    for i in range(k - 1):
        norm[i] = y[i] - y[i + 1] # begin from the least meaning
    norm[k - 1] = y[k - 1] # the left bits is 0

    return norm



