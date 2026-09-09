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
        self.nom:str = nom
        self.notes:float = []
    
    def nom(self) -> str:
        return self.nom
    
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
        if len(self.notes) < 5 :
            raise ValueError("Il n'y a pas assez de notes pour avoir une mention")
        
        elif CarnetNote.moyenne :
        elif
        elif
        elif
        elif
        
        return 
        
            





c=CarnetNote('Louis')
c.ajouter_note(-1)
c.ajouter_note(24)
c.ajouter_note(14)
print(c.moyenne())
c.ajouter_note(16)
c.ajouter_note(20)
print(c.moyenne())
