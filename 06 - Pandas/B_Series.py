# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:57:51 2019

@author: MORALES
"""
import numpy as np
import pandas as pd

lista_numeros = [1, 2, 3, 4]
tupla_numeros = (1, 2, 3, 4)
np_numeros = np.array((1, 2, 3, 4))

serie_A = pd.Series(lista_numeros)
serie_B = pd.Series(tupla_numeros)
serie_C = pd.Series(np_numeros)
serie_D = pd.Series([True,
                     False,
                     12,
                     12.12,
                     "Juanjo",
                     None,
                     (),
                     [],
                     {"nombre":"Juanjo"}])


serie_D[3]


lista_ciudades =  ["Ambato", "Cuenca", "Loja", "Quito"]

serie_ciudad = pd.Series(lista_ciudades, 
                         index=["A", "C", "L", "Q"])

serie_ciudad["Q"]
serie_ciudad[3]

valores_ciudad = {"Ibarra": 9500,
                  "Guayaquil": 10000,
                  "Cuenca": 7000,
                  "Quito": 8000,
                  "Loja": 3000
                  }

serie_valor_ciudad = pd.Series(valores_ciudad)
serie_valor_ciudad[0]
serie_valor_ciudad["Ibarra"]

ciudades_menores_5000 = serie_valor_ciudad <  5000

serie_5 = serie_valor_ciudad[ciudades_menores_5000]

# Mi forma
# serie_modificada_ciudad = pd.Series((serie_valor_ciudad *1.10))

# Forma del ing
serie_valor_ciudad = (serie_valor_ciudad * 1.10)

serie_valor_ciudad["Quito"]= (serie_valor_ciudad["Quito"] - 50)

print("Lima" in serie_valor_ciudad)
print("Loja" in serie_valor_ciudad)

rsquare = np.square(serie_valor_ciudad)
rsin = np.sin(serie_valor_ciudad)

ciudades_uno = pd.Series({"Montañita": 300,
                          "Guayaquil": 10000,
                          "Quito": 2000})

ciudades_dos = pd.Series({"Loja": 300,
                          "Guayaquil": 10000})

# Para añadir nuevo elemento, solo se necesita el índice y el valor
ciudades_uno["Loja"] = 0
ciudades_dos["Montañita"] = 0
ciudades_dos["Quito"] = 0

print(ciudades_uno + ciudades_dos)

ciudad_add = ciudades_uno.add(ciudades_dos)

ciudad_concatenada = pd.concat([ciudades_uno,
                                ciudades_dos])

# Para que no se junten los indices
ciudad_concat_v = pd.concat([ciudades_uno,
                             ciudades_dos], verify_integrity = True)

ciudad_append = ciudades_uno.append(ciudades_dos)

ciudad_append_v = ciudades_uno.append(ciudades_dos, verify_integrity = True)

#append y concat han sido lo mismo

ciudades_uno.max()
pd.Series.max(ciudades_uno)
np.max(ciudades_uno)

ciudades_uno.min()
pd.Series.min(ciudades_uno)
np.min(ciudades_uno)

ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

ciudades_uno.head(2)
ciudades_uno.tail(2)

ciudades_uno.sort_values().head(2)
ciudades_uno.sort_values(ascending = False).head(2)
ciudades_uno.sort_values().tail(2)





