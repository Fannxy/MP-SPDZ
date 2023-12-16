from Compiler.types import sfix
from Compiler.library import *


MAX_TREE_REDUCE = 2**28

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
    res = Array(n, sfix)
    @for_range_opt_multithread(min(parallel, n), n)
    def _(i):
        res[i] = sfix(0)
        
    tbl = Array(n*m, sfix)
    @for_range_opt_multithread(parallel, [n, m])
    def _(i, j):
        tbl[i*m+j] = (arr[j] * (indices[i] == j))
    if(n*m > MAX_TREE_REDUCE):
        for i in range(n):
            res[i] = tbl.get_vector(i*m, m).sum()
    else:
        for i in range(n):
            res[i] = tree_reduce_multithread(parallel, lambda x, y: x+y, tbl.get_vector(i*m, m))
        
    return res


def tgl_select_for_parallel(tars, keys, vals, parallel=1):
    
    m, n = len(keys), len(tars)
    res = Array(n, sfix)
    @for_range_opt_multithread(min(parallel, n), n)
    def _(i):
        res[i] = sfix(0)
        
    tbl = Array(n*m, sfix)
    @for_range_opt_multithread(parallel, [n, m])
    def _(i, j):
        tbl[i*m+j] = ((tars[i] == keys[j]) * vals[j])
        
    if(n*m > MAX_TREE_REDUCE):
        @for_range_opt_multithread(min(parallel, n), n)
        def _(i):
            res[i] = tbl.get_vector(i*m, m).sum()
    else:    
        for i in range(n):
            res[i] = tree_reduce_multithread(parallel, lambda x, y: x+y, tbl.get_vector(i*m, m))
        
    return res



def tgl_average_for_parallel(arr, parallel=1):
    
    m, n = len(arr)7, 1
    res = Array(n, sfix)
    res[0] = sfix(0)
        
    tbl = Array(m, sfix)
    @for_range_opt_multithread(parallel, [1, m])
    def _(i, j):
        tbl[i*m+j] = arr[j]
    
    if(n*m > MAX_TREE_REDUCE):
        res[0] = tbl.get_vector(0, m).sum()
    else:
        res = tree_reduce_multithread(parallel, lambda x, y: x+y, tbl)
        
    return res


def tgl_search_for_parallel(tars, keys, vals, parallel=1):
    
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
    
    if(n*m > 2**30):
        
        @for_range_opt_multithread(n, n)
        def _(i):
            res_val[i] = tbl[i*m]
            res_ind[i] = indtbl[i*m]
            
        @for_range_opt_multithread(min(parallel, n), [n, m-1])
        def _(i, j):
            comp = (res_val[i] < tbl[i*m+j+1])
            res_val[i] = comp.if_else(res_val, tbl[i*m+j+1])
            res_ind[i] = comp.if_else(res_ind, indtbl[i*m+j+1])
    else:        
        for i in range(n):
            res_val[i], res_ind[i] = tree_reduce_multithread_type(parallel, op1, tbl.get_vector(i*m, m), indtbl.get_vector(i*m, m), sfix)
            
    return res_val, res_ind


def tgl_max(X, parallel=1):
    
    m = len(X)
    n = m
    res = Array(m, sfix)
    @for_range_opt_multithread(min(parallel, m), m)
    def _(i):
        res[i] = sfix(0)
        
    tbl = Array(n*m, sfix)
    @print_ln('actual_size: %s', tbl.size())
    @for_range_opt_multithread(parallel, [n, m])
    def _(i, j):
        tbl[i*m+j] = X[i] > X[j]

    if(n*m > MAX_TREE_REDUCE):
        @for_range_opt_multithread(min(parallel, n), n)
        def _(i):
            res[i] = tbl.get_vector(i*m, m).sum()
    else:
        for i in range(n):
            res[i] = tree_reduce_multithread(parallel, lambda x, y: x+y, tbl.get_vector(i*m, m))
    
    # select the max val
    tars = Array(1, sfix)
    tars[0] = sfix(n-1)
    max_val = tgl_select_for_parallel(tars, res, X, parallel)
    
    return max_val

