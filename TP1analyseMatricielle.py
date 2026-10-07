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

#Exercice 2
#Par hypohtèse les pivots sont non nuls
#1)
def Gauss1(A):
    (n,m)=np.shape(A)
    T=np.copy(A)  #A.copy
    for k in range(0,n-1): #1 a n-1
        for i in range(k+1,n): #k+1 a n
            T[i,k]= -T[i,k]/T[k,k]
            T[i,:] = T[i,:] + T[i,k]*T[:,k]
    return T
A=np.array([[2.,1.,1.,1.],[1.,2.,1.,1.],[1.,1.,2.,1.],[1.,1.,1.,2.]])
Gauss1(A)

def Gauss1bis(A):
    (n,m)=np.shape(A)
    T=np.copy(A)  #A.copy
    for k in range(0,n-1): #1 a n-1
        pivot = T[k,k]
        for i in range(k+1,n): #k+1 a n
            coef = -T[i,k]/pivot
            T[i,k] = coef
            T[i,k+1:m] = T[i,k+1:m] + coef*T[k,k+1:m]
    return T
A=np.array([[2.,1.,1.,1.],[1.,2.,1.,1.],[1.,1.,2.,1.],[1.,1.,1.,2.]])
Gauss1bis(A)

#2

def Gauss2(A,b):
    (n,m)=np.shape(A) 
    B=np.concatenate((A, b), axis=0) # la meme chose B=np.hstack((A,b))
    B=Gauss1bis(B) 
    bprime=B[:,n]; # extraction du b transforme bprime derniere colonne
    U=np.triu(B[:,0:n]); # extraction de la matrice carree uper U
    x=remontee(U,bprime);
    return (U,x)  

A=np.array([[2,1,1],[1,2,1],[1,1,2]])
b=np.array([[4],[4],[4]])
Gauss2(A,b)   
            
            
            
            
            