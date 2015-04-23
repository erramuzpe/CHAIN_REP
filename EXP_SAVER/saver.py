# -*- coding: utf-8 -*-


import numpy as np

# https://math.stackexchange.com/questions/920351/selecting-at-least-one-ball-of-each-color
# https://en.wikipedia.org/wiki/Hypergeometric_distribution
from pymc import multivariate_hypergeometric_like

def multichoose(n,k):
    if k < 0 or n < 0: return "Error"
    if not k: return [[0]*n]
    if not n: return []
    if n == 1: return [[k]]
    return [[0]+val for val in multichoose(n-1,k)] + \
        [[val[0]+1]+val[1:] for val in multichoose(n,k-1)]

def remove_comb(list_):
    
    x2 = list_[:]

    for m in list_:
        for z in m:
            if z == 0 or (1 not in m):
                x2.remove(m)
                break
    return x2

#main
 
p = input('Tell me the probability you want to ensure in %: \n')
x = input('Tell me the number of mutations: \n')
n = input('Tell me the number of elements in total (1000?): \n')

num_ele = np.floor((n/x)) #number of elements x set

ele_set  = np.ones(x)*num_ele #elements x set fixed
unk_set = np.ones(x) #unknown set start

a=0 # unknown - starts in x
cum_prob = 0


while cum_prob<p:
    
    all_comb = multichoose(x,a)
    our_comb=remove_comb(all_comb)

    for comb in our_comb:
        if not comb:
            break
        
        log_like=multivariate_hypergeometric_like(comb, ele_set)
        prob_one_comb=np.e**log_like
        
        cum_prob += prob_one_comb
    
    
    a += 1
    print a, cum_prob
  

  
print a

