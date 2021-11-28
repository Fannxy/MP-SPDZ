"""Generate the correspondidng ranodm arrays.
"""
import random
from Compiler.types import *
from Compiler.library import *

def create_random_array(n, type):
    """ Used to create an random array with length n.
    """
    if type == 'sfix':
        arr = Array(n, sfix)
        @for_range(n)
        def _(i):
            arr[i] = sfix(random.randint(0, 5))
    elif type == 'sint':
        arr = Array(n, sint)
        @for_range(n)
        def _(i):
            arr[i] = sint(random.randint(0, 5))
    return arr


def create_random_matrix(m, n, type):
    """Used to create random matrix in shape (m, n) for tests.
    """
    if type == 'sfix':
        r_matrix = sfix.Matrix(m, n)
        @for_range_opt(m)
        def _(i):
            @for_range_opt(n)
            def _(j):
                r_matrix[i][j] = sfix(random.randint(0, 5))
        break_point()

    elif type == 'sint':
        r_matrix = sfix.Matrix(m, n)
        @for_range_opt(m)
        def _(i):
            @for_range_opt(n)
            def _(j):
                r_matrix[i][j] = sfix(random.randint(0, 5))
        break_point()
    
    return r_matrix


def create_arrays_get_last_one(n, type, version='quick'):
    """ Used to generate 0, 1 arrays for get-last-one.
    """
    if type == 'sfix':
        tmp_arr = [sfix(0) for i in range(n)]
        arr = Array.create_from(tmp_arr)
        t_point = random.randint(1, n)
        @for_range_opt(t_point)
        def _(i):
            arr[i] = sfix(1)
    
    elif type == 'sint':
        arr = Array([sint(0) for i in range(n)])
        t_point = random.randint(1, n)
        @for_range_opt(t_point)
        def _(i):
            arr[i] = sint(1)

    return arr
