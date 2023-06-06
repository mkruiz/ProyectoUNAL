# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto
Proyecto de Machine Learning para clasificación de noticias falsas.

## Objetivo del Proyecto

Desarrollar un mecanismo de identificación de noticias falsas con el uso de tecnologías de Machine Learning.

## Alcance del Proyecto

### Incluye:

- Los datos corresponden a un conjunto de noticias reales y falsas disponibles en el sitio público: Kaggle. Estos datos se encuentran organizados en dos archivos CSV (Fake.csv y True.csv), cada uno de los cuales contiene la siguiente la información:
  * Título de la noticia.
  * Texto de la noticia.
  * Subject: tópico asociado a la noticia.
  * Fecha de la noticia.
  Analizando los datos se encuentra que el conjunto de datos con noticias falsas:
  *  Contiene: 23502 registros
  *  Son noticias de los años 2015, 2016, 2017 y 2018.
  *  Se presentan registros (52) con errores en la información de la fecha que deberán ser tratados en la etapa de preparación de los datos.
  
  Analizando los datos se encuentra que el conjunto de datos con noticias verdaderas:
  *  Contienee: 21418 registros. 
  *  Son noticias de los años 2016 y 2017.
  *  No presentan errores en la información de las fechas.
  
- Resultados esperados:
  Considerando el objetivo del proyectos se espera:
  1. Contar con un artefacto que permita identificar noticias falsas, dado un conjunto de noticias.
  2. El modelo implementado debe entregar el nivel de confianza de la predicció de manera que basado en un umbral acordado se establezcan las acciones a tomar.

- [Criterios de éxito del proyecto]
  1. El modelo entrega el nivel de confianza de la predicción dado un conjunto de noticias.
  2. El desarrollo sigue una metología reconocida y mejores prácticas de la industria.
  3. Identificación de los roles requeridos para el desarrollo y operación del modelo entregado.
  4. Código documentado y siguiendo las mejores prácticas.
  5. Documentación del proyecto y del desarrollo que explique los recursos usados, dependencias y estructura del proyecto que permita su mantenimiento.

### Excluye:

- El proyecto no incluye la adquisición de la infraestructura requerida.

## Metodología

La metodología corresponde a CRISP/DM

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semanas | del 5 de junio al 15 de mayo |
| Preprocesamiento, análisis exploratorio | 4 semanas | del 16 de mayo al 15 de junio |
| Modelamiento y extracción de características | 4 semanas | del 16 de junio al 15 de julio |
| Despliegue | 2 semanas | del 16 de julio al 31 de julio |
| Evaluación y entrega final | 3 semanas | del 1 de agosto al 21 de agosto |


## Equipo del Proyecto

- Líder de proyecto: Mónica Ruiz
- Equipo de ingenieros de Machine Learning.
- Arquitecto de solución.
- Equipo de infraestrutura.

## Presupuesto

El 

## Stakeholders

- Gerente del área de negocio.
- Sponsor del proyecto.
- Analistas de medios.

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
