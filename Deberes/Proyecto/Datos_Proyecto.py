# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:21:31 2019

@author: MORALES
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

path = 'C://Users//MORALES//Documents//GitHub//py-morales-banda-juan-jose//Deberes//Proyecto//Anime.csv'
columnas = ['animeID',' name',' type',' source',' producers',' genre',' studio',' episodes',' status',' rating',' score',' premiered']
columnas2 = ['name','type','source','producers','genre','studio','episodes','status','rating','score','premiered']
df1 = pd.read_csv(path, usecols=columnas, index_col = 'animeID')
df1.columns = columnas2

x = len(df1)
for i in range(x):
  if (math.isnan(df1['score'].values[i])):
    df1['score'].values[i] = 0.0

for i in range(x):
  if (math.isnan(df1['rank'].values[i])):
    df1['rank'].values[i] = 0.0

for i in range(x):
  if (math.isnan(df1['episodes'].values[i])):
    df1['episodes'].values[i] = 0.0

df1['source'].value_counts().plot(kind='bar',legend='Reverse')
df1['type'].value_counts().plot(kind='bar',legend='Reverse')
df1['genre'].value_counts().plot(kind='bar',legend='Reverse')
df1['studio'].value_counts().plot(kind='bar',legend='Reverse')
df1['episodes'].value_counts().plot(kind='bar',legend='Reverse')
df1['status'].value_counts().plot(kind='bar',legend='Reverse')
df1['rating'].value_counts().plot(kind='bar',legend='Reverse')

df1.rating.value_counts().plot(kind='pie', cmap='Paired')
plt.ylabel('')

df1['episodes'].sort_values().tail(2).plot(kind='bar',legend='Reverse')

df1.episodes.sort_values().tail(20).plot(kind='bar',legend='Reverse')

df1['score'].sort_values().tail(20).plot(kind='bar',legend='Reverse')

df1.groupby('rating')['name'].nunique().plot(kind='bar',legend='Reverse')

df1['score'].sort_values(ascending = False).head(2).plot(kind='bar',legend='Reverse')

g = ['name','score']
valores = df1[g].sort_values(by='score').tail(20)
valores.index = valores['name']
valores.plot(kind='bar')


pivot_versiones = pd.pivot_table(df1, index=['status', 'rating'], values=['source'], columns=['type'], aggfunc='count')
pivot_versiones.groupby('status').plot(kind = 'bar', legend = 'Reverse')
plt.ylabel('Total de Aplicaciones')


#pivot_versiones = pd.pivot_table(df1, index=['Content Rating', 'Category'], values=['Rating'], columns=['Type'], aggfunc='count')
#pivot_versiones.groupby('Content Rating').plot(kind = 'bar', legend = 'Reverse')
#plt.ylabel('Total de Aplicaciones')

df1['premiered'].value_counts().tail(20).plot(kind='bar',legend='Reverse')
df1.premiered.value_counts().head(10).plot(kind='pie', cmap='Paired')

df1['source'].value_counts().plot(kind='bar')
