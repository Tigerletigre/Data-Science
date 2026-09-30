#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:40:06 2026

@author: lopercher
"""
import numpy as np
import scipy.linalg as lg
#from time import time
#import matplotlib.pyplot as plt
def remontee(A,b):
    (n,m) = np.shape(A)
    x = np.zeros(n)
    for i in range (n-1,-1,-1): #depart = n-1 ; ou on va -1 de base;
        x[i] = b[i] - sum(A[i,j]*x[j] for j in range (i+1,n))  #n est un indice colonne
        x[i]=x[i]/A[i,i]
    return x

A=np.array([[1.,2.,3.],[0,1.,2.],[0,0,2.]])
b=np.array([1.,3.,5.])
#b=np.reshape(b,(3,1))
x=remontee(A,b)
x
#print(A.shape)

    
def descente(A,b):
    n = A.shape[0]
    x = np.zeros(n)
    for i in range(0,n):
        x[i] = b[i] - np.dot(A[i,0:i],x[0:i])  #n est un indice colonne
        x[i]=x[i]/A[i,i]
    return x

A=np.array([[1.,0,0],[1.,2.,0],[1.,2.,1.]])
b=np.array([1.,3.,5.])        
x=descente(A,b)
x
