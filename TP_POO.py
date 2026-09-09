# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def mot_avec_plus_de_a(texte:str) -> str:

    texte = texte.lower()
    mots=[]
    mots = texte.split(texte)
    cpt=0
    mot_avec_plus_de_a = []
    for i in  range (0,len(mots)-1):
        nbr_a = mots[i].count("a")
        if nbr_a > cpt :
            mot_avec_plus_de_a = mots[i]
            cpt = nbr_a
        elif nbr_a == cpt :
            mot_avec_plus_de_a.append(mots[i])
    print(mot_avec_plus_de_a)
mot_avec_plus_de_a('Bonjour comment allez vous aujourdhui bAnAna')
    #CORRECTION

def mot_avec_plus_de_a(texte:str) -> str:
    mots = texte.split()
    plus_a = mots[0]
    for mot in mots:
        if mot.lower().count('a') > plus_a.lower().count('a'):
            plus_a = mot
    return plus_a
print(mot_avec_plus_de_a("Anaconda avale une banane"))            
            
            

class Point:
    pass
class Segment:
    pass
    
a = Point()
a.x = 1
a.y = 2
print(type(a))
b = Point()
b.x = 2
b.y = 1
print(type(b))

ab = Segment()
ab.e1 = a #extremité 
ab.e2 = b
print(type(ab))
print(type(ab.e1))
print(type(ab.e2))

#correction
import math
class Point:
    def __init__(self, x : float = 0,y : float = 0)-> None:
        self.x:float = x
        self.y:float = y
        
class Segment:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1:Point = p1
        self.p2:Point = p2
    def longueur(self) -> float:
        return math.hypot(self.p2.x - self.p1.x, self.p2.y - self.p1.y)
    def deplacer(self,dx: float, dy:float) -> None:
        self.p1.x += dx
        self.p1.y += dy
        self.p2.x += dx
        self.p2.y += dy
    def milieu(self) -> Point:
        return Point((self.p1.x + self.p2.x)/2, (self.p1.y + self.p2.y)/2)
Point1 = Point(3,5)



#NON Segment accède directement aux attributs de point,Segment est un  utlisateur de Point























