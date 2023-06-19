# -*- coding: utf-8 -*-
"""download_data.ipynb

Función para cargar los datos a analizar en el proyecto
# **Carga de los datos**
"""

# Importar las librerías con el código desarrollado
import sys
import pathlib
import pandas as pd

# Función de preprocesamiento de las noticias reales
def preprocessing_true(df):
    # Cálculo de la extensión del contenido (text) de las noticias reales
    df['len_text'] = (df['text'].str.strip()).str.len()
    # Se crea un nuevo dataframe eliminando el registro sin información en el campo text
    new_df = df[df['len_text'] > 0]
    return new_df


# Función de preprocesamiento de las noticias falsas
def preprocessing_false(df, size):
    # Cálculo de la extensión del contenido (text) de las noticias falsas
    df['len_text'] = (df['text'].str.strip()).str.len()
    # Se crea un nuevo dataframe eliminando los registros sin información en el campo text
    news_false_mod = df[df['len_text'] > 0]
    # Se crea un nuevo dataframe eliminando los registros cuto tamaño del campo text es inferior o igual al límite establecido
    new_df = news_false_mod[news_false_mod['len_text'] > size]
    return new_df


