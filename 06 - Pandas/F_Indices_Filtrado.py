# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:49:24 2019

@author: MORALES
"""

import pandas as pd

path_guardado_full = 'C://Users//MORALES//Documents//GitHub//py-morales-banda-juan-jose//06 - Pandas//data//artwork_data_full.pickle'
df = pd.read_pickle(path_guardado_full)

## Obtener 
serie_artistas_repetidos = df['artist']

artistas = pd.unique(serie_artistas_repetidos)
## Otra manera
## artistas = pd.unique(df['artist'])

artistas.size
len(artistas)

blake = (df['artist'] == 'Blake, William')

blake.value_counts()
df['artist'].value_counts()

df_blake = df[blake]





