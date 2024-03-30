from Compiler.types import sfix
from Compiler.library import *

MAX_TREE_REDUCE = 2**28

def tgl_cipher_index(arr, indices, parallel=1):
    
    m, n = len(arr), len(indices)
    res = Array(n, sfix)
    @for_range_opt_multithread(min(parallel, n), n)
    def _(i):
        res[i] = sfix(0)
        
    tbl = Array(n*m, sfix)
    @for_range_opt_multithread(parallel, [n, m])
    def _(i, j):
        tbl[i*m+j] = (arr[j] * (indices[i] == j))
    
    for i in range(n):
        target_vector = tbl.get_vector(i*m, m)
        res[i] = tree_reduce_multithread(parallel, lambda x, y: x+y, target_vector)
        
    return res


def tgl_select(tars, keys, vals, parallel=1):
    
    m, n = len(keys), len(tars)
    res = Array(n, sfix)
    @for_range_opt_multithread(min(parallel, n), n)
    def _(i):
        res[i] = sfix(0)
        
    tbl = Array(n*m, sfix)
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
    res = Array(n, sfix)
    # res = tree_reduce_multithread(parallel, lambda x, y: x+y, arr.get_vector(0, m))
    return tree_reduce_multithread(parallel, lambda x, y: x+y, arr.get_vector(0, m))


def tgl_search(tars, keys, vals, parallel=1):
    
    m, n = len(keys), len(tars)
    res = Array(n, sfix)
    @for_range_opt_multithread(min(parallel, n), n)
    def _(i):
        res[i] = sfix(0)
        
    extend_keys = Array(m, sfix)
    tbl = Array(n*m, sfix)
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
    res_val = Array(n, sfix)
    res_ind = Array(n, sfix)
    
    @for_range_opt_multithread(min(parallel, n), n)
    def _(i):
        res_val[i] = sfix(0)
        res_ind[i] = sfix(0)
        
    tbl = Array(n*m, sfix)
    indtbl = Array(n*m, sfix)
    
    @for_range_opt_multithread(parallel, [n, m])
    def _(i, j):
        tbl[i*m+j] = (X[i] - Y[j]) * (X[i] - Y[j])
        indtbl[i*m+j] = sfix(j)
    
    def op1(a, b, c, d):
        comp = (a < b)
        return comp.if_else(a, b), comp.if_else(c, d)
    
    for i in range(n):
        target_vector_x = tbl.get_vector(i*m, m)
        target_vector_ind = indtbl.get_vector(i*m, m)
        res_val[i], res_ind[i] = tree_reduce_multithread_type(parallel, op1, target_vector_x, target_vector_ind, sfix)
            
    return res_val, res_ind


def tgl_max(X, parallel=1):
    m = len(X)
    n = 1
    return tree_reduce_multithread(parallel, lambda x, y: x.max(y), X)


def tgl_rank(X, parallel=1):
    m = len(X)
    n = m
    tbl = Array(n*m, sfix)
    
    @for_range_opt_multithread(parallel, [n, m])
    def _(i, j):
        tbl[i*m+j] = (X[i] > X[j])
    
    res = Array(n, sfix)
    @for_range_opt(n)
    def _(i):
        res[i] = tree_reduce_multithread(parallel, lambda x, y: x+y, tbl.get_vector(i*m, m))
    
    return res
    

def tgl_sort(X, parallel=1):
    m = len(X)
    n = m
    
    rank_val = tgl_rank(X, parallel)
    target_val = Array(m, sfix)
    @for_range_opt_multithread(min(parallel, m), m)
    def _(i):
        target_val[i] = sfix(i)
    sorted_val = tgl_select(target_val, rank_val, X, parallel)
    
    return sorted_val