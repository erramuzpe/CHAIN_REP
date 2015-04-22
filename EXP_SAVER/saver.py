# -*- coding: utf-8 -*-


import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

#clear(all)
#plt.close(all)
#clc


th0 = 0.95
Nmax = 15.
index = np.zeros(Nmax, 1.)
ratio = np.zeros(Nmax, 1.)
for N in np.arange(1., (Nmax)+1):
    zmax = 1000.*Nmax
    #% max number of tries
    th = np.dot(th0, zmax)
    output = np.zeros(zmax, 1.)
    for z in np.arange(1., (zmax)+1):
        counter = np.ones(N, 1.)
        cont = 0.
        I = 1.
        while I != 0.:
            i = np.floor((np.random.rand(1., 1.)*N+1.))
            #% choose one ball
            cont = cont+1.
            counter[int(i)-1] = 0.
            I = nonzero(counter)
            
        output[int(z)-1,0] = cont
        
    [freq, X] = plt.hist(output, matcompat.max(output))
    c = np.cumsum(freq)
    maxc = matcompat.max(c)
    probs.cell[int(N)-1] = c/matcompat.max(c)
    aux = nonzero((c > th))
    index[int(N)-1] = aux[0]+np.floor((X[0]-1.))
    ratio[int(N)-1] = matdiv(aux[0], N)
    
plt.figure
plt.plot(index)
plt.figure
plt.plot(ratio)