#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:41:07 2026

@author: lopercher
"""

class Utilisateur:
    def __init__(self,nom:str)->None:
        self._nom:str = nom
    @property
    def nom(self)->str:
        return self._nom
        
        
class Reservation:
    def __init__(self,utilisateur:Utilisateur,debut:int,fin:int)->None:
        self._debut:int = debut
        self._fin:int = fin
        self._utilisateur = utilisateur
        
    @property
    def debut(self):
        return self._debut
    
    @property
    def fin(self):
        return self._fin
    
    @property
    def utilisateur(self):
        return self._utilisateur
        
    def chevauche(self,debut:int,fin:int)->bool:
        if self._debut < fin and self._fin > debut:
            return True
        else:
            return False
        
                    
class Salle:
    def __init__(self,numero:str,capacite:int):
        self._numero:str = numero
        self._capacite:int = capacite
        self._reservations:list[Reservation] = []
        
    @property
    def numero(self)->str:
        return self._numero
    
    @property
    def capacite(self)-> int:
        return self._capacite
    
    @property
    def reservations(self)->list[Reservation]:
        return self._reservations
    
    def est_libre(self,debut:int,fin:int)->bool:
        for i in self.reservations:
            if not i.chevauche(debut,fin):
                return True
        return False
        
    def reserver(self,u:Utilisateur,debut:int,fin:int)-> bool:
        if self.est_libre(debut,fin) == True:
            self._reservation.append(Reservation(u,debut,fin))
        else:
            return False
            
    def supprimer_reservation(self,u:Utilisateur)->bool:
        for i in self._reservation:
            if i.utilisateur == u:
                self._reservation.remove(i)
            return True
        return False
    
    
class Batiment:
    def __init__(self,nom:str)->None:
        self._nom:str = nom
        self._salles:list[Salle] = []
        
    @property   
    def nom(self)  -> str:
        return self._nom
    
    def rechercher_salle_libre(self,debut:int,fin:int,capacite:int)->list[Salle]:
        for i in self._salles:
            if i.capacite >= capacite and i.est_libre(debut,fin) == True:
                return True
        return False
    
    def ajouter_salle(self,capacite:int):
        
        numero = str(len(self._salles) + 1)
        self._salles.append(Salle(numero,capacite))

A = Batiment('Alpha')
A.ajouter_salle(capacite=20)
B = Batiment('Beta')
B.ajouter_salle(10)   

   
    