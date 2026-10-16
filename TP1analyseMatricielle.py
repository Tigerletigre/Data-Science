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
    T=np.copy(A) # pour ne pas modifier A
    for k in range(0,n-1):
        pivot=T[k,k] 
        for i in range(k+1,n):
            coef=-T[i,k]/pivot
            T[i,k]=coef
            T[i,k+1:m]=T[i,k+1:m]+coef*T[k,k+1:m]
            
    return T

A=np.array(([2.,1.,1.],[1.,2.,1.],[1.,1.,2]))
Gauss1bis(A)




def LU1(A) : # decomposition LU par Gauss (A=LU)
    (n,m)=np.shape(A)
    T=Gauss1bis(A) #le Gauss où on a stocké les m_i,k
    U=np.triu(T) #on extrait la partie triangulaire sup
    L=U-T+np.eye(n) 
    return [L,U] 
A=np.array([[2.,1.,1.,1.],[1.,2.,1.,1.],[1.,1.,2.,1.],[1.,1.,1.,2.]])
LU1(A)
#np.dot(LU1(A)[0],LU1(A)[1])

L,U=LU1(A);print(L);print(U)
print(np.dot(L,U))     
# A=np.array([[2,1,1],[1,2,1],[1,1,2]],dtype=float)     
A=np.array([[2.,1.,0.,0.,0.,0],
            [1.,2.,1.,0.,0.,0],
            [0.,1.,2.,1.,0.,0],
            [0.,0.,1.,2.,1.,0],
            [0.,0.,0.,1.,2.,1],
            [0.,0.,0.,0.,1.,2]])

LU1(A)
L,U=LU1(A);print(L);print(U)
print(np.dot(L,U))                

def tridiag(n,d,a):
    aa=np.ones(n-1)#matrice unidimentionnelle de 1
    A=d*np.eye(n)+a*np.diag(aa,-1)+a*np.diag(aa,1)
    return A

def tridiagbis(n,d,a):
    A=np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                A[i,j]=d
            else :
                if (abs(i-j)==1):
                    A[i,j]=a               
    return A


#def LU2(A):
 #   n,m = np.shape(A)
  #  L=np.eye(n)
   # U=np.eye(n)
    #for j in range (1,n):
     #   for k in range (j,n):
      #      U[j,k]=A[j,k] - np.dot(L[j,0:j],U[0:j,k])
       # for k in range(j+1,n):
        #    L[k,j]= (A[k,j] - np.dot(L[k,0:j],U[0:j,j]))/U[j,j]
    #return L,U
    

LU2(tridiagbis(6,2,1))
L,U=LU1(A);print(L);print(U)
print(np.dot(L,U))  


P,L,U =lg.lu(A)



    
A=np.array([[2.,1.,1.],[1.,2.,1.],[1.,1.,2.]]);print(A)
b=np.ones([3,1]);print(b)
L,U=LU1(A)
y=descente(L,b)# resolution de Ly=b
x=remontee(U,y)# resolution de Ux=y
np.allclose(np.dot(A,x),b)
