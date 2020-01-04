# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:22:03 2020

@author: MORALES
"""
import pandas as pd
import numpy as np
import math

path_guardado_full = 'C://Users//MORALES//Documents//GitHub//py-morales-banda-juan-jose//06 - Pandas//data//artwork_data_full.pickle'
df = pd.read_pickle(path_guardado_full)

seccion_df = df.iloc[49980:50019,:].copy()

df_agrupado = seccion_df.groupby('artist')
type(df_agrupado)

for registros in df_agrupado:
  print(registros)

for a,b in df_agrupado:
  type(a)
  type(b)
  print(a) # Valores de las columnas agrupadas
  print(b) # Dataframe completo


y = seccion_df['units'].value_counts()
y.empty
x = seccion_df['depth'].value_counts()
x.empty # Verificar si está llena o vacía

# Funcion que recibe una serie y realice cosas
def llenar_valores_vacios(series, tipo):
  lista_valores = series.value_counts()
  if(lista_valores.empty == True):
    return series
  else:
    if(tipo == 'promedio'):
      suma = 0
      cantidad_valores = 0
      for valor_serie in series:
        if(isinstance(valor_serie, str)):
          valor = int(valor_serie)          
          suma = suma + valor
          cantidad_valores = cantidad_valores + 1
        else:
          pass
      promedio = suma / cantidad_valores
      series_valores_llenos = series.fillna(promedio)
      return series_valores_llenos
    if(tipo == 'value_counts'):
      """lista_valores.sort_values(ascending = False)
      print(lista_valores.values)"""
      lista = series.value_counts().keys().tolist()
      #print(lista)
      series_valores_llenos = series.fillna(lista[0])
      return series_valores_llenos
          
      


def transformar_df (df):
  df_artist = df.groupby('artist')
  lista_df = []
  for artista, df in df_artist:
    copia = df.copy()
    serie_w = copia['width']
    serie_h = copia['height']
    serie_u = copia['units']
    serie_i = copia['inscription']
    copia.loc[:,'width'] = llenar_valores_vacios(serie_w, 'promedio')
    copia.loc[:,'height'] = llenar_valores_vacios(serie_h, 'promedio')
    copia.loc[:,'units'] = llenar_valores_vacios(serie_u, 'value_counts')
    copia.loc[:,'inscription'] = llenar_valores_vacios(serie_i, 'value_counts')
    lista_df.append(copia)
  df_completo_con_valores = pd.concat(lista_df)
  return df_completo_con_valores

df_valores_llenos = transformar_df(seccion_df)

















