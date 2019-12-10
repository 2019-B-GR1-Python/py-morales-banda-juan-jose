# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 07:35:04 2019

@author: MORALES
"""
import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,5)
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

df = pd.DataFrame(arr_pand)

df[1] = ser1

df = df.append(ser2, ignore_index = True)

path = 'C://Users//MORALES//Documents//GitHub//py-morales-banda-juan-jose//Examen//I Bimestre//BostonHousing.csv'
columnas = ['crim','zn','nox','rm']
df2 = pd.read_csv(path, usecols = columnas)


mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie_A = pd.Series(mylist)
serie_B = pd.Series(myarr)
serie_C = pd.Series(mydict)



#12) ¿Como convertir el indice de una serie en una columna de un DataFrame?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict) 
indices=list(ser.index.values)

ser_df = pd.DataFrame(ser)
ser_df[1] = indices
# Transformar la serie en dataframe y hacer una columna indice

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
ser3 = pd.concat([ser1,ser2])
dataframe = pd.DataFrame(ser3)


ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

resp = ser2.isin(ser1)
for i in range(len(resp)):
  resp[i] = not resp[i]

ser2[resp]

#15) ¿Como obtener los items que no son comunes en una serie A y serie B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

resp = ser1.isin(ser2)
resp2 = ser2.isin(ser1)

for i in range(len(resp)):
  resp[i] = not resp[i]

for i in range(len(resp2)):
  resp2[i] = not resp2[i]

serie = ser1[resp]
serie2 = ser2[resp2]
serie3 =pd.concat([serie,serie2])



#19) ¿Obtener los valores de una serie conociendo la posicion por indice?
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u
ser[pos]

#18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un shape definido?
ser = pd.Series(np.random.randint(1, 10, 35))
ser_dfa = pd.DataFrame(ser)
ser_dfa.shape
