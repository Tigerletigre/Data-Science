#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:07:42 2026

@author: lopercher
"""
import math
class CarnetNote:
    #_attribut_classe:float=[]
    def __init__(self, nom : str) -> None:
        self._nom:str = nom
        self.notes:float = []
    #@property
    def nom(self) -> str:
        return self._nom
    
    def ajouter_note(self,notes):
        if notes < 0 or notes > 20 :
            raise ValueError("Vous devez entrer une notes entre 0 et 20")
        else:
            self.notes.append(notes)
    def getter_notes(self) ->list[float]:
        return (self.notes)
         
    def moyenne(self):
        if len(self.notes) == 0 :
            raise ValueError("Il n'y a pas de notes dans las liste")
        return sum(self.notes)/len(self.notes)
    
    def mention(self):
        
        if (len(self.notes) < 5) :
            raise ValueError("Il n'y a pas assez de notes pour avoir une mention")
        m=self.moyenne()
        if m >= 18:
            return ("Tu as les félicitations du jury")
        elif m >= 16:
            return("Tu as la mention trés bien")
        elif m >= 14:
            return ("Tu as la mention bien")
        elif m >=12:
            return ("Tu as la mention assez bien")
        else :
            if m>=10:
                return ("Tu n'as pas de mention")
    
    def reset(self):
        self.notes = []
        print("Toutes les notes ont été effacés")
        return self.notes
        
            
a=CarnetNote('Louis')

a.ajouter_note(14)
a.ajouter_note(16)
a.ajouter_note(20)
a.ajouter_note(16)
a.ajouter_note(16)
print(a.nom())
print(a.moyenne())  
print(a.notes)
print(a.mention())
print(a.reset())


#Exercice 2
#partie 1
class CompteBancaire:
    _cpt_id:int =0
    def __init__(self,nom_proprietaire : str):
        self._nom_proprietaire:str = nom_proprietaire
        self._solde:float = 0
        
        CompteBancaire._cpt_id +=1
        self._identifiant = CompteBancaire._cpt_id
        
    @property    
    def nom_proprietaire(self)->str:
        return self._nom_proprietaire
    
    @property
    def solde(self)->float:
        return self._solde
    
    @property
    def identifiant(self)->int:
        return self._identifiant
    
    def deposer(self,montant:float)->None:
        if montant <0.0:
            raise ValueError("Le montant déposé doit être positif")
        self._solde += montant
    
    def retirer(self,montant)-> bool:
        if montant < 0.0:
            raise ValueError("Le montant retiré doit être positif")
        if montant > self._solde:
            return False
        self._solde -= montant
        return True
     
    def transferer(self, autre_compte:"CompteBancaire", montant:float)->bool:       
        if(self.retirer(montant)):
            autre_compte.deposer(montant)
            return True
        return False           
        
        

a=CompteBancaire('Louis')        
print(a.nom_proprietaire)  
print(a.identifiant)      
b=CompteBancaire('Arthur')
print(b.nom_proprietaire)  
print(b.identifiant) 
print(b.solde)
b.deposer(100)
print(b.solde)
b.retirer(30)
print(b.solde)
b.transferer(a,18.6)
print(a.solde)

#partie 2
class Banque:
    def __init__(self)->None:
        self._comptes: dict[str, CompteBancaire] = {}
        
    def ajouter_compte(self,nom:str)->None:
        if nom in self._comptes:
            raise ValueError(f"{nom} possède déjà un compte.")
        self._comptes[nom] = CompteBancaire(nom)
    
    def get_compte(self,nom:str)-> CompteBancaire|None:
        #for i in range (0,len(self._comptes)):
         #   if self._comptes[i] == nom:
          #      return self._comptes[i]
          #  else:
           #     return None
        if nom not in self._comptes:
            return None
        return self._comptes[nom]            
            
            
    def transferer(self, nom1:str, nom2:str , montant:float)-> bool:
        compte1=self.get_compte(nom1)
        if not compte1:
            raise ValueError(f"{nom1} ne possède pas de compte.")
        compte2=self.get_compte(nom2)
        if not compte2:
            raise ValueError(f"{nom2} ne possède pas de compte.")
        return compte1.transferer(compte2,montant)



Bq = Banque()
Bq.ajouter_compte('Louis') 
Bq.ajouter_compte('Pa')    
Bq.get_compte('Louis').deposer(100)
Bq.get_compte('Pa')
Bq.transferer('Louis','Pa',5)


#partie 3

class CompteSecurise:
    def __init(self,c:CompteBancaire):
        self._compte:CompteBancaire=c
        
    @property
    def solde(self)->float:
        return self._compte.solde
    @property
    def nom_proprietaire(self)->str:
        return self._compte.nom
    
    def deposer(self,montant:int)->None:
        self._comptes.deposer(montant)
    
    
        
        
        
        
   
    




