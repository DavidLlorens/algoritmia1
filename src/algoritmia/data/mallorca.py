#coding: latin1

#< full
from algoritmia.datastructures.digraphs import UndirectedGraph, WeightingFunction

km = WeightingFunction(
      {('Alcúdia', 'Artà')              : 36, ('Alcúdia', 'Inca')               : 25,
       ('Alcúdia', 'Pollença')          : 10, ('Andratx', 'Calvià')             : 14,
       ('Andratx', 'Palma de Mallorca') : 30, ('Andratx', 'Sóller')             : 56,
       ('Artà', 'Capdepera')            : 8,  ('Artà','Manacor')                : 17,
       ('Calvià', 'Palma de Mallorca')  : 14, ('Campos del Port', 'Llucmajor')  : 14,
       ('Campos del Port',   'Santanyí'): 13, ('Inca',   'Manacor')             : 25,
       ('Inca', 'Marratxí')             : 12, ('Llucmajor', 'Palma de Mallorca'): 20,
       ('Manacor', 'Santanyí')          : 27, ('Marratxí', 'Palma de Mallorca') : 14,
       ('Pollença', 'Sóller')           : 54},
       symmetrical=True)
Mallorca = UndirectedGraph(E=km.keys())
#> full