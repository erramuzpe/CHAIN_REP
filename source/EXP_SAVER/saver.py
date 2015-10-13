# -*- coding: utf-8 -*-


import numpy as np
import pylab as pl

# https://math.stackexchange.com/questions/920351/selecting-at-least-one-ball-of-each-color
# https://en.wikipedia.org/wiki/Hypergeometric_distribution


# Example. From the example given on the web Wikipedia: The Free 
#  Encyclopedia [http://en.wikipedia.org/wiki/Hypergeometric_distribution].
#  Suppose there are 5 black, 10 white, and 15 red marbles in an urn. You
#  reach in and randomly select six marbles without replacement. What is 
#  the probability that you pick exactly two of each color?
#
#              ele_set = [2,2,2]; comb = [5,10,15];
#
# Calling the function: 
#             x = multivariate_hypergeometric_like(comb, ele_set)
#
# Answer is: (in format long)
#
# x =
#
#   0.07957559681698



from pymc import multivariate_hypergeometric_like

def multichoose(n,k):
    if k < 0 or n < 0: return "Error"
    if not k: return []
    if not n: return []
    if n == 1: return [[k]]
    return [[0]+val for val in multichoose(n-1,k)] + \
        [[val[0]+1]+val[1:] for val in multichoose(n,k-1)]

def remove_comb(list_):
    
    x2 = list_[:]

    for m in list_:
        for z in m:
            if z == 0:
                x2.remove(m)
                break
    return x2

#main
 
p = input('Tell me the probability you want to ensure (0.95?): \n')
x = input('Tell me the number of mutations (classes): \n')
n = input('Tell me the number of elements in total (1000?): \n')

for x in range(2,7):
    num_ele = np.floor((n/x)) #number of elements x set
    ele_set  = np.ones(x)*num_ele #elements x set fixed
    
    a=0 # unknown - starts in x
    cum_prob = 0
    vector_a= np.zeros(1)
    vector_cum_prob= np.zeros(1)
    
    while cum_prob<p:
        a += 1
        all_comb = multichoose(x,a)
        our_comb=remove_comb(all_comb)
        cum_prob = 0
        for comb in our_comb:
            if not comb:
                break
            
            log_like=multivariate_hypergeometric_like(comb, ele_set)
            prob_one_comb=np.e**log_like
            
            cum_prob += prob_one_comb
        
        print "Number of experiments:", a ,"\n" ,"Prob:", cum_prob ,"\n"
        vector_a = np.append(vector_a,[a])
        vector_cum_prob = np.append(vector_cum_prob, [cum_prob])
        
    print "Number of experiments:", a ,"\n" ,"Prob:", cum_prob ,"\n"

pl.plot(vector_a, vector_cum_prob)
