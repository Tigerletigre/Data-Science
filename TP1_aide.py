# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 09:51:31 2021

@author: utilisateur
"""

#### EX 1

import numpy as np
import matplotlib.pyplot as plt
#1
def f(x) : return np.sin(x[0])**10+np.cos(x[0]*x[1])*np.cos(x[0])

#2
X=np.linspace(0,5,500)  #500 valeurs entre 0 et 5
Y=np.linspace(0,5,500)  #500 valeurs entre 0 et 5
XX=np.meshgrid(X,Y) #construit la grille

#np.meshgrid(np.array((0,1,2)),np.array((0,1,2)))
#3
ZZ=f(XX)
#4
np.shape(XX[1])
contour=plt.contour(XX[0],XX[1],ZZ,colors='black')
#5
plt.clabel(contour,inline=True, fontsize=8)  #affiche ligne de niveau
plt.imshow(ZZ, extent=[0, 5, 0, 5], origin="lower",cmap="RdGy", alpha=0.5)#met de la couleur dans le graphique
plt.colorbar() #affiche la légende des couleurs
#6
def niveau(f,a,b,c,d,ortho=True,valeur=True):
    X=np.linspace(a,b,500)
    Y=np.linspace(c,d,500)
    XX=np.meshgrid(X,Y)
    ZZ=f(XX)
    contour=plt.contour(XX[0],XX[1],ZZ,colors='grey')
    if valeur==True : plt.clabel(contour,inline=True, fontsize=8)
    if ortho==True : plt.axis("equal")
    xlabel('x')
    ylabel('y')

niveau(f,0,5,0,5)


### Ex 2

import numpy as np
import matplotlib.pyplot as plt

# 1

def f(x): return np.sin(np.sqrt(x[0]**2+x[1]**2))

plt.axis('equal')

#2
from mpl_toolkits import mplot3d
ax=plt.axes(projection='3d')
X=np.linspace(-6,6,500)
Y=np.linspace(-6,6,500)
XX=np.meshgrid(X,Y)
ZZ=f(XX)
ax.plot_wireframe(XX[0], XX[1], ZZ, linewidth=0.5,color="grey")

ax=plt.axes(projection='3d')
ax.plot_surface(XX[0], XX[1], ZZ, cmap="viridis")
ax.plot_surface(XX[0], XX[1], ZZ, alpha=0.25,edgecolor="k", linewidth=0.1)
ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('z')
ax.contour(XX[0], XX[1], ZZ, zdir="x", offset=+7) #♠courbe de niveau de x
ax.contour(XX[0], XX[1], ZZ, zdir="y", offset=-7)
ax.contour(XX[0], XX[1], ZZ, zdir="z", offset=+1)


def surface(f,a,b,c,d):
    ax=plt.axes(projection='3d')
    X=np.linspace(a,b,500)
    Y=np.linspace(c,d,500)
    XX=np.meshgrid(X,Y)
    ZZ=f(XX)
    ax.plot_wireframe(XX[0], XX[1], ZZ, linewidth=0.5,color="grey")
    ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('z')

surface(f,-6,6,-6,6)

#### EX 3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
#1
Z = np.linspace(0,15,1000)
X = np.cos(Z)
Y = np.sin(Z)

#2
ax=plt.axes(projection='3d') #Toujours le mettre pour avoir le graph 3d
ax.plot3D(X,Y,Z, "grey")
ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('z')

#3
Z= np.linspace(0,15,100) #
X= np.cos(Z)+np.random.randn(100)*0.1  #
Y= np.sin(Z)+np.random.randn(100)*0.1
ax.scatter3D(X,Y,Z,c=Z)




#Ex 4
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
#1
#composition de fonction de classse C infini

#2
def f(x): return np.log(1+x[0]**2+x[1]**2)
X=np.linspace(-1.5,1.5,500)
Y=np.linspace(-1.5,1.5,500)
XX=np.meshgrid(X,Y)
ZZ=f(XX)
contour=plt.contour(XX[0],XX[1],ZZ,colors='grey')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
# courbe de niveau log(2)
contour=plt.contour(XX[0],XX[1],ZZ,levels=[np.log(2)],colors="red")

#tangente
a=1/2**0.5
plt.arrow(a,a,a/2,-a/2,width = 0.005,head_width=0.05, head_length=0.05)

plt.arrow(a,a,-a/2,a/2,width = 0.005,head_width=0.05, head_length=0.05)

#gradient
plt.arrow(a,a,a/2,a/2         ,width = 0.05,head_width=0.1, head_length=0.1)

#3 


X=np.linspace(-1.5,1.5,500)
Y=X
XX=np.meshgrid(X,Y)
ax.plot_wireframe(XX[0],XX[1], f(XX), linewidth=0.5,color="grey")
#courbe de niveau
plt.contour(XX[0],XX[1],ZZ,levels=[np.log(2)],colors='red')
#point (a,a)
ax.scatter3D(0.5**0.5,0.5**0.5,np.log(2),color='red')
#plan tangent
def g(x,y): return 0.5**0.5*((x-0.5**0.5)+(y-0.5**0.5))+np.log(2)
ax.plot_wireframe(XX[0],XX[1], g(XX),linewidth=0.5,color="red")


#4
ax=plt.axes(projection='3d')
#la surface
ax.plot_wireframe(            , linewidth=0.5,color="grey")

#le plan tangent en (0,0)
ax.plot_wireframe(           , linewidth=0.5,color="red")

#L'approximation qudratique en (0,0)

ax.plot_wireframe(           , linewidth=0.5,color="blue")




#Ex 5
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def f1(x): return x[0]**2-x[0]*x[1]+x[1]**2
def f2(x): return x[0]**2-2*x[0]*x[1]+x[1]**2
def f3(x): return -x[0]**2-x[0]*x[1]-x[1]**2
def f4(x): return x[0]**2+2*x[0]*x[1]-x[1]**2+1


plt.subplot(2,2,1)
niveau(f1,-2,2,-2,2,valeur=True)
plt.title('f1')
plt.subplot(2,2,2)
niveau(f2,-2,2,-2,2,valeur=True)
plt.title('f2')    
plt.subplot(2,2,3)
niveau(f3,-2,2,-2,2,valeur=True)
plt.title('f3')  
plt.subplot(2,2,4)
niveau(f4,-2,2,-2,2,valeur=True)
plt.title('f4')    

ax=plt.axes(projection='3d')
surface(f1,-2,2,-2,2)    
surface(f2,-2,2,-2,2)  
surface(f3,-2,2,-2,2)  
surface(f4,-2,2,-2,2)  
