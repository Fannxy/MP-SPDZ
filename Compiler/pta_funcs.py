from Compiler.types import sfix
from Compiler.library import *

def tgl_cipher_index_for(arr, indices):
    m, n = len(arr), len(indices)
    res = sfix.Array(n)
    @for_range_opt(n)
    def _(i):
        res[i] = sfix(0)
        @for_range_opt(m)
        def _(j):
            res[i] = res[i] + (arr[j] * (indices[i] == j))
    return res


def tgl_cipher_index_for_parallel(arr, indices, parallel=1):
    
    m, n = len(arr), len(indices)
    
    res = Array.create_from([sfix(0) for i in range(n)])
    tbl = Array(n*m, sfix)
    
    @for_range_opt_multithread(parallel, [n, m])
    def _(i, j):
        tbl[i*m+j] = (arr[j] * (indices[i] == j))
        
    @for_range_opt_multithread(min(parallel, n), n*m)
    def _(i):
        res[i//m] = res[i//m] + tbl[i]
        
    return res