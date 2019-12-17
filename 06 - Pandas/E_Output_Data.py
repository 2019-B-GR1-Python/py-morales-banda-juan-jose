# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:57:41 2019

@author: MORALES
"""
import pandas as pd
import numpy as np
import xlsxwriter
import os
import sqlite3

path_guardado_full = 'C://Users//MORALES//Documents//GitHub//py-morales-banda-juan-jose//06 - Pandas//data//artwork_data_full.pickle'
df5 = pd.read_pickle(path_guardado_full)
# copiar una sección del dataframe
df = df5.iloc[49980:50519,:].copy()

# TIPOS ARCHIVOS
# JSON
# EXCEL
# SQL

### EXCEL ###

path_guardado = 'C://Users\MORALES//Documents//GitHub//py-morales-banda-juan-jose//06 - Pandas//data//mi_df_completo.xlsx'
df.to_excel(path_guardado)
df.to_excel(path_guardado, index = False)
columnas = ['artist', 'title', 'year']
df.to_excel(path_guardado, columns = columnas, index = False)

### Múltiples hojas de trabajo ###
path_multiple = 'C://Users\MORALES//Documents//GitHub//py-morales-banda-juan-jose//06 - Pandas//data//mi_df_múltiple.xlsx'
writer = pd.ExcelWriter(path_multiple, 
                        engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = 'Primera')
df.to_excel(writer, sheet_name = 'Segunda', index = False)
df.to_excel(writer, sheet_name = 'Tercera', columns = columnas)

writer.save()

### Múltiples hojas de trabajo ###
num_artistas = df['artist'].value_counts()
path_colores = 'C://Users\MORALES//Documents//GitHub//py-morales-banda-juan-jose//06 - Pandas//data//mi_df_colores.xlsx'

writer_colores = pd.ExcelWriter(path_colores,
                                engine = 'xlsxwriter')

num_artistas.to_excel(writer_colores,sheet_name = 'Artistas')

hoja_artistas = writer_colores.sheets['Artistas']

# Crear el rango de la celda
rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1)

# Crear formato (trabaja con diccionarios)
formato_artistas = {'type' : '2_color_scale',
                    'min_value' : '10',
                    'min_type' : 'percentile',
                    'max_value': '99',
                    'max_type': 'percentile'}

hoja_artistas.conditional_format(rango_celdas,
                                 formato_artistas)

writer_colores.save()

##############################

workbook = xlsxwriter.Workbook('mi_df_colores.xlsx')
worksheet = workbook.add_worksheet()

# Add the worksheet data to be plotted.
data = [10, 40, 50, 20, 10, 50]
worksheet.write_column('A1', data)

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart.add_series({
    'values': '=Sheet1!$A$1:$A$6',
    'marker': {
        'type': 'square',
        'size': 8,
        'border': {'color': 'black'},
        'fill':   {'color': 'red'},
    },
})

# Insert the chart into the worksheet.
worksheet.insert_chart('C1', chart)

workbook.close()

########## SQL #########
with sqlite3.connect('bdd_artist.db') as conexion:
  df5.to_sql('py_artist', conexion)

########## JSON ##########
df5.to_json('artistas.json')
df5.to_json('artistas_tabla.json', orient = 'table')
  
  
  
  
  
  

