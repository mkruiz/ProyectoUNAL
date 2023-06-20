# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo baseline seleccionado es el modelo: XGBClassifier considerando que se trata de un problema de clasificación de noticias falsas y verdaderas.

## Variables de entrada

Las variables de entrada del modelo son:

title : título de  la noticia

text : contenido de la noticia

Subject: tópico de la noticia

Estas tres variables se procesaron para unirlas en una sola columna, generar una lista y  posteriormente convertir estos textos en una matriz de características TF-IDF. Representación que es requerida para el modelo.

## Variable objetivo

La variable objetivo utilizada en el modelo es:

type : tipo de la noticia. 0 - Falsa, 1 - verdadera.

## Evaluación del modelo

### Métricas de evaluación

Las métricas usadas en el modelo son accuracy y F1-score.

### Resultados de evaluación

Los resultados no han mostrado hasta el momento resultados coherentes, se continuará en la revisión y generación de la línea base adecuada.

## Análisis de los resultados

> Descripción de los resultados del modelo baseline, incluyendo fortalezas y debilidades del modelo.

Aún no he logrado encontrar resultados concluyentes.

## Conclusiones

Los resultados obtenidos hasta el momento no corresponden con lo esperado, pues después de varios intentos y modificaciones en la definición del modelo se sigue presentando una exactitud de 1. Lo cual en este tipo de problemas refleja posibles errores que deben ser revisados.

Hasta el momento no he podido generar la línea base continuaré realizando iteraciones y ajustes al modelo y revisiones a los datos. Lo cual hace parte del ciclo de la metodología utilizada y cuyo objetivo es lograr el mejor resultado para el problema planteado.

## Referencias

[XGBoost Documentation](https://xgboost.readthedocs.io/en/stable/index.html).
