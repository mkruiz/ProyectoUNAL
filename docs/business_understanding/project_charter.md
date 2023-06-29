# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto
Proyecto de identificación de noticias falsas en una iniciativa de control de noticias en redes sociales.

## Objetivo del Proyecto

Desarrollar un mecanismo de identificación de noticias falsas con el uso de tecnologías de Machine Learning que apoye al área de análisis de medios en la iniciativa de control de noticias.

## Alcance del Proyecto

### Incluye:

- Los datos a usar en el entrenamiento del modelo corresponden a un conjunto de noticias reales y falsas disponibles en el sitio público: Kaggle. Estos datos se encuentran organizados en dos archivos CSV (Fake.csv y True.csv), cada uno de los cuales contiene información asocidad a las noticias. La volumetría del conjunto de datos seleccionado se encuentra representada de la siguiente manera: Fake.csv contiene 23.502 noticias y True.csv contiene 21.418 noticias.
Este conjunto de datos seraá utilizado en el entrenamiento, validación y prueba del modelo.
    
- Resultados esperados:

  Considerando el objetivo del proyecto se espera:
  1. Contar con un modelo de machine learning que permita identificar noticias falsas, dado un conjunto de noticias.
  2. El modelo implementado debe entregar el nivel de confianza de la predicción de manera que basado en un umbral acordado se establezcan las acciones a tomar.

- Criterios de éxito del proyecto:

  1. El modelo entrega el nivel de confianza de la predicción dado un conjunto de noticias.
  2. El desarrollo sigue una metodología reconocida y mejores prácticas de la industria.
  3. Identificación de los roles requeridos para el desarrollo y operación del modelo entregado.
  4. Código documentado y siguiendo las mejores prácticas.
  5. Documentación del proyecto y del desarrollo que explique los recursos usados, herramientas, dependencias y estructura del proyecto que facilite su entendimiento y su futuro mantenimiento.
  6. Transferencia de conocimiento al equipo de TI de la organización.

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
| Preprocesamiento, análisis exploratorio de los datos y recursos a usar | 1 semana | del 6 de junio al 12 de junio |
| Modelamiento y extracción de características | 1 semana | del 13 de junio al 19 de junio |
| Despliegue y refinamiento de la documentación | 1 semana | del 20 de junio al 26 de junio |
| Evaluación, Revisión de la documentación y entrega final | 1 semana | del 27 de junio al 2 de julio |


## Equipo del Proyecto

- Líder de proyecto: Mónica Ruiz
- Gerente de proyeto del negocio.
- Equipo de científicos de datos.
- Arquitecto de solución.
- Equipo de infraestructura.
- Analista de medios.

## Presupuesto

El presupuesto del proyecto comprende los siguientes elementos:

![Presupuesto](https://github.com/mkruiz/ProyectoUNAL/blob/master/docs/business_understanding/Presupuesto.jpg)

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
