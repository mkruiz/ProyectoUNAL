# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto
Proyecto de Machine Learning para clasificación de noticias falsas.

## Objetivo del Proyecto

Desarrollar un mecanismo de identificación de noticias falsas con el uso de tecnologías de Machine Learning que apoye al área de análisis de medios en el control de noticias de falsas.

## Alcance del Proyecto

### Incluye:

- Los datos a usar en el entrenamiento del modelo corresponden a un conjunto de noticias reales y falsas disponibles en el sitio público: Kaggle. Estos datos se encuentran organizados en dos archivos CSV (Fake.csv y True.csv), cada uno de los cuales contiene la siguiente la información:
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
  2. El modelo implementado debe entregar el nivel de confianza de la predicción de manera que basado en un umbral acordado se establezcan las acciones a tomar.

- Criterios de éxito del proyecto:

  1. El modelo entrega el nivel de confianza de la predicción dado un conjunto de noticias.
  2. El desarrollo sigue una metología reconocida y mejores prácticas de la industria.
  3. Identificación de los roles requeridos para el desarrollo y operación del modelo entregado.
  4. Código documentado y siguiendo las mejores prácticas.
  5. Documentación del proyecto y del desarrollo que explique los recursos usados, herramientas, dependencias y estructura del proyecto que facilite su entendimiento y su futuro mantenimiento.

### Excluye:

- El proyecto no incluye la adquisición de la infraestructura requerida.

## Metodología

La metodología a usar corresponde a TDSP (Team Data Science Process), metodología propuesta por Microsoft en 2016 para proyectos de Data Science y que propone estructurar el proyecto desde varios niveles:
 *  Ciclo de vida de ciencia de datos, el cual comprende: Entendimiento del negocio, Adquisición y entendimiento de los datos, Modelamiento, Despliegue y Aceptación del cliente.
 *  Estructuración del proyecto.
 *  Infraestrutura y recursos.
 *  Herramientas y utilidades.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 5 días | del 1 de junio al 5 de junio |
| Preprocesamiento, análisis exploratorio | 1 semana | del 6 de junio al 12 de junio |
| Modelamiento y extracción de características | 1 semana | del 13 de junio al 19 de junio |
| Despliegue y refinamiento de la documentación | 1 semana | del 20 de junio al 26 de junio |
| Evaluación, Revisión de la documentación y entrega final | 1 semana | del 27 de junio al 2 de julio |


## Equipo del Proyecto

- Líder de proyecto: Mónica Ruiz
- Gerente de proyeto del negocio.
- Equipo de científicos de datos.
- Arquitecto de solución.
- Equipo de infraestructura.

## Presupuesto

El 

## Stakeholders

- Gerente del área de negocio.
- Sponsor del proyecto.
- Analistas de medios.
- Equipo control del negocio.
- Equipo de presupuesto y finanzas del negocio.
- Equipo de TI del negocio.

## Aprobaciones

- Gerente del proyecto y sponsor del negocio.
- 6 de junio de 2023
