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

#Exercice 2

class Adherent:
    def __init__(self,discipline:str,nom:str,email:str,tel:str,nom_urgence:str,email_urgence:str,tel_urgence:str)->None:
        cpt = 0
        for i in email:
            if i == '@' :
                cpt+=1
        if cpt != 1:
            raise ValueError ('Votre adresse mail doit contenir un seul @')
        if len(tel)!=10 or not tel.isdigit():
            raise ValueError('Votre numero de telephone doit contenir 10 chiffre')
        cpt=0    
        for i in email_urgence:
            if i == '@' :
                cpt+=1
        if cpt != 1:
            raise ValueError ('Votre adresse mail urgence doit contenir un seul @')
        if len(tel_urgence)!=10 or not tel_urgence.isdigit():
            raise ValueError('Votre numero de telephone urgence doit contenir 10 chiffre')
  
        self._discipline:str = discipline
        self._nom:str = nom
        self._email:str = email
        self._tel:str= tel
        self._nom_urgence:str = nom_urgence
        self._email_urgence:str = email_urgence
        self._tel_urgence:str= tel_urgence
        
    def coordonnees(self)->str:
        return f'nom:{self._nom} ,email:{self._email},tel:{self._tel}'
    def coordonnees_urgence(self)->str:
        return f'nom_urgence:{self._nom_urgence} ,email_urgence:{self._email_urgence},tel_urgence:{self._tel_urgence}'
   
a = Adherent('badminton','Louis','lo@g','0123456789','raphael','po@m','9876543210')
a.coordonnees
class entraineur:
    def __init__(self,nom:str,email:str,tel:int,discipline:str,jour_presence:str,heure_debut:int,heure_fin:int)
        for i in email:
            if i == '@' :
                cpt+=1
        if cpt != 1:
            raise ValueError ('Votre adresse mail doit contenir un seul @')
        if len(tel)!=10 or not tel.isdigit():
            raise ValueError('Votre numero de telephone doit contenir 10 chiffre')    
        
        self._nom:str = nom
        self._email:str = email
        self._tel:str= tel
        self._discipline:str = discipline
        semaine = ['lundi','mardi','mercredi','jeudi','vendredi']
        for i in semaine:
            if self._jour_presence != semaine[i]:
                raise ValueError ('Choisir un jour entre lundi et vendredi')
        self._jour_presence:str = jour_presence
        if self._heure_debut > self._heure_fin or self._heure_debut < 10 or  self._heure_fin > 18:
            raise ValueError('Choisir un créneau entre 10h et 18h')
        self._heure_debut:int = heure_debut
        self._heure_fin:int = heure_fin       
        
        
        def coordonnees(self)->str:
            return f'nom:{self._nom} ,email:{self._email},tel:{self._tel}'

class Discipline:
    def __init__(self,nom:str,capacite:int)->None:
        self._nom:str = nom
        self._capacite:int = int
        self._creneaux:list= []
        
6    def ajouter_creneau(self,jour:str,heure_debut:int,heure_fin:int)->None:
        

