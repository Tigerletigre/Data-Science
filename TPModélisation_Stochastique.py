#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:57:16 2026

@author: lopercher
"""

import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

"npr.rand() renvoie un nbr aléatoire uniformément entre 0 et 1"
"npr.randint(a,b)  a < b renvoie un entier uniforme aléatoire dans {a,a+1,...,b-1}"

#1
def simulation_chaine(X0,N):
    trajectoire = [X0]
    k = X0
    while k != N:
        k = npr.randint(k,N+1)
        trajectoire.append(k)
    return trajectoire  #on peut le faire sans le k et directement avce X
        
simulation_chaine(1,4)
simulation_chaine(1,100)

nbr_simulation =5
for i in range(nbr_simulation):
    trajectoire = simulation_chaine(1,10)
    plt.plot(trajectoire)

#2
def estimation(X0,N,nbr_simu):
    T=0  #somme de nbr_simu simulation de tau, independantes
    for i in range(nbr_simu):
       T += len(simulation_chaine(X0,N))-1
    return T/nbr_simu
a = estimation(1,3,10000)
print(f"Le temps moyen et {a}")       


#Exercice2

def marche_aléatoire(x,p,n):
    chemin=[]
    cpt=0
    for i in range(n):
        if npr.rand() <= p:
            x=x+1
            chemin.append(x)
        else:
            x=x-1
            chemin.append(x)
        if chemin[i]==0:
            cpt+=1
    return chemin,cpt


    
m=marche_aléatoire(0,1/2,10000) #46
m2=marche_aléatoire(0,3/4,10000) #0,1 ou 2 mais très rarement plus
m  
m2
plt.stairs(m[0])
plt.stairs(m2[0])


#ou correction
def trajmarche(x,n,p):
    traj=[x]
    for i in range(n):
        x+=2*(npr.rand()<p)-1
        traj.append(x)
    return traj

n=10000
x=0
p=[1/4,1/2,3/4]
abs=np.arange(0,n+1)
for i in range(3):
    plt.step(abs,trajmarche(x,n,p[i]),label=p[i])
    #plt.plot(abs,abs*(2*p[i]-1),'--',label = f'comp. asymp., 'f'p={p[i]}')
#plt.legend()

def nbpassages(x,N,p):
    z=x
    compt=x
    for i in range(N):
        z+=2*(npr.rand()< p)-1
        compt+=(z==x)
    return compt

nbpassages(0,10000,11/20)    
#mouvement bronien theorie processus stochastique
    
