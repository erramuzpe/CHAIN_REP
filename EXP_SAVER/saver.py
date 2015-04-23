# -*- coding: utf-8 -*-


import numpy as np
import matplotlib as mp
import math

# https://math.stackexchange.com/questions/920351/selecting-at-least-one-ball-of-each-color
 
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
 
#main
 
p = input('Tell me the probability you want to ensure in %: \n')
x = input('Tell me the number of mutations: \n')
n = input('Tell me the number of choices: \n')

p = 0.95
prob = 0
x = 3
n = 50
a = x #unknown

num_ele = np.floor((n/x))


while prob<p:
  
    # total number of combinations
    comb_tot = nCr(num_ele*x,a)
    # combinations without 1 ball
    comb_sum = nCr(num_ele,a)*x
    # combinations without 2 ball
    comb_min = nCr(np.floor((n/(x-2))),a)*x
    
    prob = 1 - (comb_sum - comb_min)/comb_tot
    a += 1
    
print a
   
   
import pymc
from pymc import multivariate_hypergeometric_like

pymc.distributions.multivariate_hypergeometric_like

a=multivariate_hypergeometric_like([2, 2], [3,3])
e**a
 
 
 