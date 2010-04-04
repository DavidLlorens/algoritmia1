#coding: latin1

#< full
from algoritmia.datastructures.digraphs import UndirectedGraph, WeightingFunction

km = WeightingFunction(
      {('Alc�dia', 'Art�')              : 36, ('Alc�dia', 'Inca')               : 25,
       ('Alc�dia', 'Pollen�a')          : 10, ('Andratx', 'Calvi�')             : 14,
       ('Andratx', 'Palma de Mallorca') : 30, ('Andratx', 'S�ller')             : 56,
       ('Art�', 'Capdepera')            : 8,  ('Art�','Manacor')                : 17,
       ('Calvi�', 'Palma de Mallorca')  : 14, ('Campos del Port', 'Llucmajor')  : 14,
       ('Campos del Port',   'Santany�'): 13, ('Inca',   'Manacor')             : 25,
       ('Inca', 'Marratx�')             : 12, ('Llucmajor', 'Palma de Mallorca'): 20,
       ('Manacor', 'Santany�')          : 27, ('Marratx�', 'Palma de Mallorca') : 14,
       ('Pollen�a', 'S�ller')           : 54},
       symmetrical=True)
Mallorca = UndirectedGraph(E=km.keys())
#> full