#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 08:28:13 2026

@author: lopercher
"""


import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d

def f(x): return (x[0]-1)**2 + 10*(x[0]**2 - x[1])**2
def df(x):
    dfx = 2*(x[0]-1) + 40*x[0]*(x[0]**2 -x[1])
    dfy = -20*(x[0]**2 -x[1])
    return np.array([dfx,dfy])

def g(x):
    return x[0]**2 + 2*x[1]**2 + 2*x[0]*x[1]

def dg(x):
    dgx = 2*x[0] + 2*x[1]
    dgy = 4*x[1] + 2*x[0]
    return np.array([dgx,dgy])
    
def d2g(x):
    return np.array([[2,2],[4,2]])


    

X=np.linspace(-1,2,500)
Y=np.linspace(-1,2,500)
XX,YY =np.meshgrid(X,Y)
ZZ=f(np.array([XX,YY]))
contour = plt.contour(XX,YY,ZZ,levels=np.logspace(-1,3.5,20,base=10),colors='grey')
plt.title('Courbes de niveau de f sur [-1,2]')
plt.xlabel('x')
plt.ylabel('y')

print(ZZ.min(), ZZ.max())
#Exercice 2

def descente_fixe(f,df,x0,h,tol):
    x = x0
    X = [x]
    while np.linalg.norm(df(x)) >= tol:
        x = x - h*df(x)
        X.append(x)
    return np.array(X)

X,n = descente_fixe(f,df,np.array([0.5,1]),0.01,10**-6)
X
#ou
def descente_fixebis(f,df,x0,h,tol):
    x,k = x0,0
    T=np.array([x])
    gx=df(x)
    while np.linalg.norm(gx) > tol and k < 1000:
        gx=df(x)
        x,k = x - h*gx,k+1
        T=np.append(T,[x],axis=0)   #axis = 0 pour les lignes et axis = 1 pour les colonnes
    return T,k
descente_fixebis(f,df,np.array([0.5,1]),0.01,10**-6)

#quadratique
x0,h,tol=np.array([0,1]),0.02,0.001
X=np.linspace(-1,1,500)
Y=np.linspace(-1,1,500)
XX,YY =np.meshgrid(X,Y)
ZZ=f(np.array([XX,YY]))
contour = plt.contour(XX,YY,ZZ,levels=np.logspace(-1,3.5,20,base=10),colors='grey')
plt.title('Courbes de niveau de f sur [-1,2]')
plt.xlabel('x')
plt.ylabel('y')
h,tol=0.01,0.01
T = descente_fixe(f,df,x0,h,tol)
plt.plot(T[:,0],T[:,1],'-r')
plt.axis('equal')
plt.title('f')
print(df(x0))





#Version avec descente_fix 
#Peut boucler à l'infini
x0 = np.array([0.5, 1])
tol = 10**-6

liste_h = np.linspace(0.0005, 0.004, 25)
nb_iterations = []

for h_val in liste_h:
    X_traj = descente_fixe(f, df, x0, h_val, tol)
    k = len(X_traj)-1
    nb_iterations.append(k)


plt.figure(figsize=(8, 5))
plt.plot(liste_h, nb_iterations, 'o-b', linewidth=2, markersize=5)
plt.title("Nombre d'itérations {k} en fonction du pas {h}")
plt.xlabel("Valeur du pas {h}")
plt.ylabel("Nombre d'itérations {k}")
plt.grid(True)
plt.show()

#Version avec descente_fixbis pour k < 1000 pour eviter la boucle infini 
#Avec la fonction g
x0 = np.array([0.5, 1])
tol = 10**-6

liste_h = np.linspace(0.0005, 0.09, 20)
nb_iterations = []

for h_val in liste_h:
    T,k = descente_fixebis(g, dg, x0, h_val, tol)
    nb_iterations.append(k)


plt.figure(figsize=(8, 5))
plt.plot(liste_h, nb_iterations, 'o-b', linewidth=2, markersize=5)
plt.title("Nombre d'itérations {k} en fonction du pas {h}")
plt.xlabel("Valeur du pas {h}")
plt.ylabel("Nombre d'itérations {k}")
plt.grid(True)
plt.show()

#Exerice 3
from scipy.optimize import minimize_scalar

#pas optimale
def descente_optimal(f, df, x0, tol):
    x=x0
    T=np.array([x])
    k=0
    gx=df(x)
    while np.linalg.norm(gx) > tol and k < 1000:
        gx=df(x)
        def g(s):
            return f(x-s*gx)
        s=minimize_scalar(g).x
        x=x-s*gx
        T= np.append(T,[x], axis=0)
        k+=1
    return T,k
T,k = descente_optimal(f,df,np.array([0.,0.]),0.1)
print(T)
print(k)

# Tracé graphique
X = np.linspace(-1, 2, 500)
Y = np.linspace(-1, 2, 500)
XX, YY = np.meshgrid(X, Y)
ZZ = f(np.array([XX, YY]))

plt.contour(XX, YY, ZZ, levels=np.logspace(-1, 3.5, 20, base=10), colors='grey')
plt.plot(T[:, 0], T[:, 1], '-r', marker='o', markersize=3)
plt.title('Descente à pas optimal')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.show()

#Exercice 4
def armijo(f, df, d, x, L=10, c1=0.1, beta=0.5):
    gx = df(x)
    denom = L * np.linalg.norm(d)**2
    if denom == 0:
        return 0.01
    delta = - np.dot(gx, d) / denom
    if delta <= 0:
        delta = 1.0
        
    while f(x + delta * d) > f(x) + c1 * delta * np.dot(gx, d):
        delta = beta * delta
    return delta

def descente_armijo(f, df, x0, tol, L=10, c1=0.1, beta=0.5, max_iter=1000):
    x, k = x0, 0
    T = np.array([x])
    gx = df(x)
    while np.linalg.norm(gx) > tol and k < max_iter:
        d = -gx
        delta = armijo(f, df, d, x, L, c1, beta)
        x = x + delta * d
        k += 1
        T = np.append(T, [x], axis=0)
        gx = df(x)
    return T, k

T,k = descente_armijo(f,df,np.array([0.,0.]),0.1)
print(T)
print(k)

# Tracé graphique
X = np.linspace(-1, 1, 500)
Y = np.linspace(-1, 1, 500)
XX, YY = np.meshgrid(X, Y)
ZZ = f(np.array([XX, YY]))

plt.contour(XX, YY, ZZ, levels=np.logspace(-3, 3.5, 20, base=10), colors='grey')
plt.plot(T[:, 0], T[:, 1], '-r', marker='o', markersize=3)
plt.title("Descente avec la règle d'Armijo ")
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.show()

def wolfe(f, df, d, x, L=10, c1=0.1, c2=0.9):
    gx = df(x)
    denom = L * np.linalg.norm(d)**2
    if denom == 0:
        return 0.01
    delta = - np.dot(gx, d) / denom
    if delta <= 0:
        delta = 1.0
        
    m = 0.0
    M = np.inf
    
    cond1 = f(x + delta * d) > f(x) + c1 * delta * np.dot(gx, d)
    cond2 = np.dot(df(x + delta * d), d) < c2 * np.dot(gx, d)
    
    while cond1 or cond2:
        if cond1:
            M = delta
            delta = (m + M) / 2
        else:
            m = delta
            if M == np.inf:
                delta = 10 * delta
            else:
                delta = (m + M) / 2
        cond1 = f(x + delta * d) > f(x) + c1 * delta * np.dot(gx, d)
        cond2 = np.dot(df(x + delta * d), d) < c2 * np.dot(gx, d)
    return delta

def descente_wolfe(f, df, x0, tol, L=10, c1=0.1, c2=0.9, max_iter=1000):
    x, k = x0, 0
    T = np.array([x])
    gx = df(x)
    while np.linalg.norm(gx) > tol and k < max_iter:
        d = -gx
        delta = wolfe(f, df, d, x, L, c1, c2)
        x = x + delta * d
        k += 1
        T = np.append(T, [x], axis=0)
        gx = df(x)
    return T, k

T,k = descente_wolfe(f,df,np.array([0.,0.]),0.1)
print(T)
print(k)

# Tracé graphique
X = np.linspace(-1, 1, 500)
Y = np.linspace(-1, 1, 500)
XX, YY = np.meshgrid(X, Y)
ZZ = f(np.array([XX, YY]))

plt.contour(XX, YY, ZZ, levels=np.logspace(-3, 3.5, 20, base=10), colors='grey')
plt.plot(T[:, 0], T[:, 1], '-r', marker='o', markersize=3)
plt.title('Descente avec les règles de Wolfe')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.show()

