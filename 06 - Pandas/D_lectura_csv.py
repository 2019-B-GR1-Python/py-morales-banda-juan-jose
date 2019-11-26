# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:32 2019

@author: MORALES
"""
import pandas as pd
import os

# Con Pandas se pueden leer:
# 1) JSON CSV HTML XML ...
# 2) Archivos binarios
# 3) Bases de datos relacionales

path = 'C://Users//MORALES//Documents//GitHub//py-morales-banda-juan-jose//06 - Pandas//data//artwork_data.csv'

# Dataframe con todos los datos
df1 = pd.read_csv(path, nrows=10)

# Para solo usar las columnas que queremos
columnas = ['id', 'artist', 'title',  'medium', 'year',
            'acquisitionYear', 'height',  'width', 'units']
df2 = pd.read_csv(path, nrows=10, usecols=columnas)

# Usar una columna del csv como índice del dataframe
df3 = pd.read_csv(path, nrows=10, usecols=columnas, index_col='id')

path_guardado = 'C://Users//MORALES//Documents//GitHub//py-morales-banda-juan-jose//06 - Pandas//data//artwork_data.pickle'

df3.to_pickle(path_guardado)

df4 = pd.read_csv(path)

path_guardado_full = 'C://Users//MORALES//Documents//GitHub//py-morales-banda-juan-jose//06 - Pandas//data//artwork_data_full.pickle'
df4.to_pickle(path_guardado_full)

df5 = pd.read_pickle(path_guardado)






