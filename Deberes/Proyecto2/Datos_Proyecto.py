# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:28:12 2020

@author: MORALES
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from datetime import datetime

path = 'C://Users//MORALES//Documents//GitHub//py-morales-banda-juan-jose//Deberes//Proyecto2//Gamesfull//Juegos.xlsx'

df_gamesfull = pd.read_excel(path)

#El uploader que más ha subido
df_gamesfull['Uploader'].value_counts().plot(kind='bar',legend='Reverse')

max = len(df_gamesfull['Titulo'])

listaAnios = []
for i in range (0, max):
  if (type(df_gamesfull['Fechas'][i]) == str):
    fechaCompleta = datetime.strptime(df_gamesfull['Fechas'][i], '%d/%m/%y')
    listaAnios.append(fechaCompleta.year)
  else:
    pass

df_anios = pd.DataFrame()
df_anios = df_anios.append(listaAnios)
df_anios[0].value_counts().plot(kind='pie',cmap ='Paired')
plt.ylabel('')
  #df_gamesfull['Fechas'][i] = fecha[2]
  

df_columnas = ['Titulo', 'Visitas']
valores = df_gamesfull[df_columnas].sort_values(by='Visitas', ascending = False).head(20)
valores.index = valores['Titulo']
valores.plot( kind='bar')  
  
  
 
df_gamesfull['Rating'][1] = float(df_gamesfull['Rating'][1])

for i in range(0,max):
  df_gamesfull['Rating'][i] = float(df_gamesfull['Rating'][i])
   



for i in range(0,max):
  df_gamesfull['Votos'][i] = float(df_gamesfull['Votos'][i])
  
np.average(df_gamesfull['Visitas'])


df_gamesfull['Votos'].sort_values().tail(5).plot(kind='bar',legend='Reverse')  



df_gamesfull['Tamanio'].fillna('0 GB', inplace= True)
df_gamesfull['Votos'].fillna(method ='ffill', inplace= True)
df_gamesfull['Rating'].fillna(method ='ffill', inplace= True)
df_gamesfull['Visitas'].fillna(method ='ffill', inplace= True)

## TRANSFORMAR EL TAMAÑO EN FLOAT Y QUITARLE MB Y GB
for i in range(0,max):
  if(type(df_gamesfull['Tamanio'][i]) == str): 
    df_gamesfull['Tamanio'][i] = df_gamesfull['Tamanio'][i].replace(',','.')

for i in range(0,max):
  if(type(df_gamesfull['Tamanio'][i]) == str): 
    df_gamesfull['Tamanio'][i] = df_gamesfull['Tamanio'][i].replace(' MB','')
  
for i in range(0,max):
  if(type(df_gamesfull['Tamanio'][i]) == str):
    df_gamesfull['Tamanio'][i] = df_gamesfull['Tamanio'][i].replace(' GB','')
    df_gamesfull['Tamanio'][i] = df_gamesfull['Tamanio'][i].replace(' gb','')
    df_gamesfull['Tamanio'][i] = float(df_gamesfull['Tamanio'][i])
    df_gamesfull['Tamanio'][i] = df_gamesfull['Tamanio'][i] * 1000
    
for i in range(0,max):
  if(type(df_gamesfull['Tamanio'][i]) == str): 
    df_gamesfull['Tamanio'][i] = float(df_gamesfull['Tamanio'][i])    
    
df_columnas = ['Titulo', 'Tamanio']
valores = df_gamesfull[df_columnas].sort_values(by='Tamanio', ascending = False).head(20)
valores.index = valores['Titulo']
valores.plot( kind='bar')
    
  
  
df_gamesfull['Votos'].sort_values(ascending).head(10).plot(kind='bar',legend='Reverse')

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



