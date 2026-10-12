#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:56:19 2026

@author: lopercher
"""
class Bibliotheque:
    def __init__(self):
        
        self._catalogues:list[Livre]= []
        self._utilisateurs:list[Utilisateur] = []
        
    def ajouter_utilisateur(self,nom:str,prenom:str):
        for i in self.utilisateurs :
            if i.nom == self._nom and i.prenom == self._prenom:
                raise ValueError (f"L'utilisateur {nom} {prenom} existe déjà")   
            else:
                self._utilisateurs.append(Utilisateur(nom,prenom))
                
    def enregistrer_livre(self,titre:str,auteur:str):
        self._catalogues.append(Livre(titre,auteur))
        
        
            
 class Livre:
     ide=0
     def __init__(self,titre:str,auteur:str):
         self._titre:str = titre
         self._auteur:str = auteur
         Livre.ide +=1
         self._id_livre = Livre.ide
         self._dispo = True
         
         
     @property
     def titre(self):
         return self._titre
     
     @property
     def auteur(self):
         return self._auteur
     
     @property
     def id_livre(self):
         return self._id_livre
     
     
     

class Utilisateur:
    def __init__(self,nom:str,prenom:str):
        self._nom:str=nom
        self._prenom:str=prenom
        
    
    @property
    def nom(self):
        return self._nom
    @property
    def prenom(self):
        return self._prenom
    
    
    
    def emprunter(self,nom:str,prenom:str,titre:str):
        
        
    
    def rendre(self,nom:str,prenom:str,titre:str):
        
        
        
        
    
        
        

        
        