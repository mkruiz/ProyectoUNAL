# Reporte de Datos

De acuerdo con el análisis explotario de los datos que comprende los dos archivos: Fake.csv y True.csv. Se identificó:
* Los archivos tienen la misma estructura, descrita en data_dictionary.md de este proyecto.
* Los archivos cuentan con un número similar de registros lo que permite afirmar que para el objetivo de este proyecto los dos grupo de datos se encuentran balanceados.
* La mayoría de los registros y en sus columnas presentan datos, no hay datos faltantes. Excepto por la fecha en registros del archivo Fake.csv.

## Resumen general de los datos
De acuerdo con el análisis exploratorio de los datos se encuentra para el archivo de **noticias reales - True.csv**:

1. Total de noticias: 21417.
2. Noticias en el año 2016: 4716.
3. Noticias en el año 2017: 16701.
4. Las noticias se encuentran asociadas a dos temas: 'politicsNews' y 'worldnews'.
5. Noticias que tratan de politicsNews : 11272
6. Noticias que tratan de worldnews: 10145

De acuerdo con el análisis exploratorio de los datos se encuentra para el archivo de **noticias falsas - False.csv**:

1. Total de noticias: 23481.
2. El campo 'date' presenta diferentes formatos e incluso datos que no corresponden a la fecha, sin embargo dado el problema que se plantea y como resultado de análisis exploratorio no se considera información relevante para el desarrollo del objetivo del proyecto.
4. Las noticias se encuentran asociadas a dos temas: 'News', 'politics', 'Government News', 'left-news', 'US_News' y 'Middle-east.
5. Noticias que tratan de politics : 6841.
6. Noticias que tratan de News: 9050.
7. Noticias que tratan de Government News: 1570.
8. Noticias que tratan de left-News: 4459.
9. Noticias que tratan de US_News: 783.
10. Noticias que tratan de Middle-east: 778.

Los formatos de las variables se explican en el documento data_dictionary.md.

## Resumen de calidad de los datos

Los datos se han analizado de manera individual para los dos archivos origen de los datos: True.csv y False.csv. Como resultado se tiene en este aspecto de calidad de los datos:
1. No hay datos faltantes en el archivo True.csv que corresponde a las noticias reales.
2. La información de las noticias reales está completa en cuanto al título, contenido y tópico de la noticia. La fecha aunque está completa para todos los registros no es relevante para el propósito de este proyecto.
3. El archivo False.csv presenta datos faltantes en la fecha de algunos de los registros (Se presentan registros (52) con errores), aunque presenta información no corresponde a una fecha. Y tal como se mencionó previamente no se dedicarán recursos y esfuerzos en corregir la situación de esta variable particular dado que no se considera relevante para el propósito de este proyecto.
4. La información de las noticias falsas está completa en cuanto al título, contenido y tópico de la noticia. 

## Variable objetivo

La variable objetivo corresponde al tipo de noticia y se crea al generar un solo conjunto de datos con las noticias falsas y reales, de tipo entero y asignando 1 a las noticias reales y 0  a las noticias falsas.

## Variables individuales

Las características a estudiar en este proyecto se 

En esta sección se presenta un análisis detallado de cada variable individual. Se muestran estadísticas descriptivas, gráficos de distribución y de relación con la variable objetivo (si aplica). Además, se describen posibles transformaciones que se pueden aplicar a la variable.

## Ranking de variables

En esta sección se presenta un ranking de las variables más importantes para predecir la variable objetivo. Se utilizan técnicas como la correlación, el análisis de componentes principales (PCA) o la importancia de las variables en un modelo de aprendizaje automático.

## Relación entre variables explicativas y variable objetivo

En esta sección se presenta un análisis de la relación entre las variables explicativas y la variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la regresión lineal para modelar la relación entre las variables.
