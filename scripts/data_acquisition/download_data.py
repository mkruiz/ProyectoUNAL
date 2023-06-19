# -*- coding: utf-8 -*-
"""download_data.ipynb

Función para cargar los datos a analizar en el proyecto
# **Carga de los datos**
"""

# Librerías requeridas
import pandas as pd
import pathlib

# Función para obtener el directorio de los archivos a analizar
def get_directory():
    pathtest= pathlib.Path() 
    current_path = str(pathtest.parent.absolute())
    name_directory = "ProyectoUNAL"
    index_path = current_path.find(name_directory)
    path_data = current_path[:index_path+len(name_directory)]
    path_data += '\\src\\proy\\database\\'
    return path_data

# Archivos noticias
def get_data():
  path = get_directory()
  true_file = 'True.csv'
  fake_file = 'Fake.csv'
  pd_true = pd.read_csv(path + true_file)
  pd_fake = pd.read_csv(path + fake_file)
  return  pd_true, pd_fake


