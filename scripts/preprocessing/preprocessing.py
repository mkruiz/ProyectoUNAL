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
    new_mod = df[df['len_text'] > 0]
    new_df = new_mod[['title', 'text','subject']]
    new_df['type'] = 1
    return new_df


# Función para crear un solo dataframe con todos los datos requeridos
def preprocessing_data(news_true, news_false, size_content_false):
    df_true = preprocessing_true(news_true)
    df_false = preprocessing_false(news_false, size_content_false)
    dfs = [df_true, df_false]
    df_new = pd.concat(dfs)
    return df_new


# Función de preprocesamiento de las noticias falsas
def preprocessing_false(df, size):
    # Cálculo de la extensión del contenido (text) de las noticias falsas
    df['len_text'] = (df['text'].str.strip()).str.len()
    # Se crea un nuevo dataframe eliminando los registros sin información en el campo text
    news_false_mod = df[df['len_text'] > 0]
    # Se crea un nuevo dataframe eliminando los registros cuyo tamaño del campo text es inferior o igual al límite establecido
    new_false_mod2 = news_false_mod[news_false_mod['len_text'] > size]
    new_df = new_false_mod2[['title', 'text','subject']]
    new_df['type'] = 0
    return new_df



    


