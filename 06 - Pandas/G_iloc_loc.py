# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:04:58 2019

@author: MORALES
"""

import pandas as pd

path_guardado_full = 'C://Users//MORALES//Documents//GitHub//py-morales-banda-juan-jose//06 - Pandas//data//artwork_data_full.pickle'
df = pd.read_pickle(path_guardado_full)
df2 = df.set_index('id')

## loc
primero = df.loc[1035, 'artist']
primero = df.loc[1035]
primero = df.loc[1035, 'units']

segundo = df.iloc[1035, 'artist']

datos = {'nota 1': {'Pepito':7,
                    'Juanito':8,
                    'Maria': 9},
          'disciplina': {'Pepito':5,
                    'Juanito':9,
                    'Maria': 2}}
notas = pd.DataFrame(datos)

valores = notas.iloc[0]
valores = notas.iloc[0,1]
valores = notas.iloc[[0,1]]
valores = notas.loc['Pepito']
valores = notas.loc['Pepito', 'disciplina']
valores = notas.loc['Pepito', ['disciplina', 'nota 1']]
valores = notas.loc[['Pepito', 'Maria'], ['disciplina', 'nota 1']]
valores = notas.loc[[True, False, True]]

resp = notas['nota 1'] > 7
resp2 = notas['disciplina'] > 7
valores = notas.loc[resp]
## También vale poner condiciones anidadas
valores = notas.loc[resp][resp2]

## setear valores
## A los menores que 7 en disciplina se les pondrá 7
cond = notas['disciplina'] < 7
notas.loc[cond, 'disciplina'] = 7

## Solo a Pepito se le pondrá 10 en todo
notas.loc['Pepito'] = 10

## Disciplina bajar a 7
## notas.loc[notas.index, 'disciplina'] = 7
notas.loc[:, 'disciplina'] = 7

## Añadir el promedio
notas['Promedio'] = notas.mean([1][0])
