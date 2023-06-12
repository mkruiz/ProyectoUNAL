# Definición de los datos

## Origen de los datos

Los datos se obtienen del sitio público Kaggle, en donde se encontró el conjunto de datos: [Fake and Real news dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset). Este conjunto de datos provee dos archivos en formato CSV: Fake.csv y True.csv. 

Cada uno de los cuales contiene la siguiente la información:
  * Título de la noticia.
  * Texto de la noticia.
  * Subject: tópico asociado a la noticia.
  * Fecha de la noticia.
  
Analizando los datos se encuentra que el conjunto de datos con noticias falsas (Fake.csv):
  *  Contiene: 23501 registros
  *  Son noticias de los años 2015, 2016, 2017 y 2018.
  *  Se presentan registros (52) con errores en la información de la fecha que deberán ser analizados en la etapa de preparación de los datos.
  
Analizando los datos se encuentra que el conjunto de datos con noticias verdaderas (True.csv):
  *  Contienee: 21417 registros. 
  *  Son noticias de los años 2016 y 2017.
  *  No presentan errores en la información de las fechas.

## Especificación de los scripts para la carga de datos

Script utilizado para el cargue de la información: [Download_data.ipynb](https://github.com/mkruiz/ProyectoUNAL/blob/master/scripts/data_acquisition/download_data.ipynb). 

## Rereferencias a rutas del origen de los datos

Los datos se obtienen del sitio público Kaggle, en donde se encontró el conjunto de datos: [Fake and Real news dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset). Conjunto de datos que como se ha mencionado contiene dos archivos uno de noticias falsas y otro de noticias verdaderas.

Estos archivos se han disponibilizado en las rutas:
Archivo con noticias falsas: /content/drive/MyDrive/Colab Notebooks/MLOPS/Data/Fake.csv
Archivo con noticias verdaderas: /content/drive/MyDrive/Colab Notebooks/MLOPS/Data/True.csv

### Rutas de origen de datos

Los datos se encuentran en el drive de Google de la cuente del autor de este proyecto: /content/drive/MyDrive/Colab Notebooks/MLOPS/Data.

### Base de datos de destino

Para este proyecto no se contempla un repositorio distinto al mencionado que es propiedad del autor de este proyecto.
