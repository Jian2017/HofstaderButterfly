# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:54:26 2017

@author: jian
"""

import numpy as np

def getH(L,t,B):
    H=np.zeros((L**2,L**2),dtype=complex)
    
    for i in range(L):
        for j in range(L):
            if (j+1)<L:
                H[i*L+j][i*L+j+1]=-t;
                H[i*L+j+1][i*L+j]=-t;
            if (j-1)>(-1):
                H[i*L+j][i*L+j-1]=-t;
                H[i*L+j-1][i*L+j]=-t;
            if (i+1)<(L):
                H[(i+1)*L+j][i*L+j]=-t*np.exp(-1j*B*j)
                H[i*L+j][(i+1)*L+j]=-t*np.exp(1j*B*j)
            if (i-1)>(-1):
                H[(i-1)*L+j][i*L+j]=-t*np.exp(1j*B*j)
                H[i*L+j][(i-1)*L+j]=-t*np.exp(-1j*B*j)
    
    return H