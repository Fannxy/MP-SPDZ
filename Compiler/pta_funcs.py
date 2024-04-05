from Compiler.types import sfix, sint, MultiArray
from Compiler.library import *

MAX_TREE_REDUCE = 2**28

def tgl_cipher_index(arr, indices, parallel=1):
    
    m, n = len(arr), len(indices)
    res = Array(n, sint)
    @for_range_opt_multithread(min(parallel, n), n)
    def _(i):
        res[i] = sint(0)
        
    tbl = Array(n*m, sint)
    @for_range_opt_multithread(parallel, [n, m])
    def _(i, j):
        tbl[i*m+j] = (arr[j] * (indices[i] == j))
    
    for i in range(n):
        target_vector = tbl.get_vector(i*m, m)
        res[i] = tree_reduce_multithread(parallel, lambda x, y: x+y, target_vector)
        
    return res


def tgl_select(tars, keys, vals, parallel=1):
    
    m, n = len(keys), len(tars)
    res = Array(n, sint)
    @for_range_opt_multithread(min(parallel, n), n)
    def _(i):
        res[i] = sint(0)
        
    tbl = Array(n*m, sint)
    @for_range_opt_multithread(parallel, [n, m])
    def _(i, j):
        tbl[i*m+j] = ((tars[i] == keys[j]) * vals[j])
    
    # for i in range(n):
    @for_range_opt(n)
    def _(i):
        target_vector = tbl.get_vector(i*m, m)
        res[i] = tree_reduce_multithread(parallel, lambda x, y: x+y, target_vector)
        
    return res


def tgl_average(arr, parallel=1):
    
    m, n = len(arr), 1
    res = Array(n, sint)
    # res = tree_reduce_multithread(parallel, lambda x, y: x+y, arr.get_vector(0, m))
    return tree_reduce_multithread(parallel, lambda x, y: x+y, arr.get_vector(0, m))


def tgl_search(tars, keys, vals, parallel=1):
    
    m, n = len(keys), len(tars)
    res = Array(n, sint)
    @for_range_opt_multithread(min(parallel, n), n)
    def _(i):
        res[i] = sint(0)
        
    extend_keys = Array(m, sint)
    tbl = Array(n*m, sint)
    @for_range_opt_multithread(parallel, [n, m-1])
    def _(i, j):
        key = (tars[i] >= keys[j]) ^ (tars[i] >= keys[j+1])
        tbl[i*m+j] = key * vals[j]
        
    @for_range_opt_multithread(parallel, n)
    def _(i):
        tbl[i*m + (m-1)] = (tars[i] >= keys[m-1])
    
    if(n*m > MAX_TREE_REDUCE):
        @for_range_opt_multithread(min(parallel, n), n)
        def _(i):
            res[i] = tbl.get_vector(i*m, m).sum()
        # def _(i, j):
        #     res[i] += tbl[i*m+j]
    else:        
        for i in range(n):
            res[i] = tree_reduce_multithread(parallel, lambda x, y: x+y, tbl.get_vector(i*m, m))
        
    return res


def tgl_bio_metric(X, Y, parallel=1):
    
    m, n = len(Y), len(X)
    res_val = Array(n, sint)
    res_ind = Array(n, sint)
    
    @for_range_opt_multithread(min(parallel, n), n)
    def _(i):
        res_val[i] = sint(0)
        res_ind[i] = sint(0)
        
    tbl = Array(n*m, sint)
    
    @for_range_opt_multithread(parallel, [n, m])
    def _(i, j):
        tbl[i*m+j] = (X[i] - Y[j]) * (X[i] - Y[j])
    
    for i in range(n):
        target_vector_x = tbl.get_vector(i*m, m)
        res_val[i] = tree_reduce_multithread(parallel, lambda x, y: x.min(y), target_vector_x)
            
    return res_val, res_ind


def tgl_max(X, parallel=1):
    m = len(X)
    n = 1
    return tree_reduce_multithread(parallel, lambda x, y: x.max(y), X)


def tgl_rank(X, parallel=1):
    m = len(X)
    n = m
    tbl = Array(n*m, sint)
    
    @for_range_opt_multithread(parallel, [n, m])
    def _(i, j):
        tbl[i*m+j] = (X[i] > X[j])
    
    res = Array(n, sint)
    @for_range_opt(n)
    def _(i):
        res[i] = tree_reduce_multithread(parallel, lambda x, y: x+y, tbl.get_vector(i*m, m))
    
    return res
    

def tgl_sort(X, parallel=1):
    m = len(X)
    n = m
    
    rank_val = tgl_rank(X, parallel)
    target_val = Array(m, sint)
    @for_range_opt_multithread(min(parallel, m), m)
    def _(i):
        target_val[i] = sint(i)
    sorted_val = tgl_select(target_val, rank_val, X, parallel)
    
    return sorted_val

def bio_metric(X, Y, n_parallel=256):
    
    m = len(X)
    n = 1
    parallel = min(n_parallel, m)
    
    db = MultiArray([m, 1], sint, address=X)
    sample = Y

    def match(db_entry, sample):
        return sum(x * x for x in (a - b for a, b in zip(db_entry, sample)))
    
    tmp = sint.Array(parallel)
    
    @multithread(parallel, m)
    def _(base, size):
        tmp[get_arg()] = util.tree_reduce(lambda x, y: x.min(y),
                                          (match(db[base + i], sample)
                                           for i in range(size)))
    
    res = util.tree_reduce(lambda x, y: x.min(y), tmp)
    
    return res

    