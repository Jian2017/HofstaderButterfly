# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:19:40 2017

@author: jian
"""

from numpy import linalg as LA
import numpy as np

a = np.array([[1, 1j], [-1j, 1]])


w, v = LA.eig(a)
