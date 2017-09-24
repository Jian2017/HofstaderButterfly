# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:54:15 2017

@author: jian
"""

from getM import getH
import matplotlib.pyplot as plt

import numpy as np


from tempfile import TemporaryFile

L=8
BBins=64

butterfly=np.zeros((L**2,BBins))

i=0
for B in np.nditer(np.linspace(0,1,num=BBins)):
    print(B)
    H=getH(L,.5,B*2*np.pi)
    e,v=np.linalg.eig(H)
    butterfly[:,i]=e.real
    i=i+1
    
    

np.save("plotdata",butterfly)


for i in range(BBins):
    plt.scatter([i]*(L**2),butterfly[:,i],s=0.2)
    
plt.show()
plt.savefig('plot.png')