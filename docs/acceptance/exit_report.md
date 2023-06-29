# Informe de salida

## Resumen Ejecutivo

**Título del proyecto**: Proyecto de identificación de noticias falsas en una iniciativa de control de noticias en redes sociales.

**Objetivo**: Desarrollar un mecanismo de identificación de noticias falsas con el uso de tecnologías de Machine Learning que apoye al área de análisis de medios en la iniciativa de control de noticias.

Los datos a usar en el entrenamiento del modelo corresponden a un conjunto de noticias reales y falsas disponibles en el sitio público: Kaggle. Estos datos se encuentran organizados en dos archivos CSV (Fake.csv y True.csv), cada uno de los cuales contiene información asocidad a las noticias. La volumetría del conjunto de datos seleccionado se encuentra representada de la siguiente manera: Fake.csv contiene 23.502 noticias y True.csv contiene 21.418 noticias.

Se usó la metodología TDSP (Team Data Science Process), para guiar el análisis y desarrollo en fases de este proyecto y entregó una guía muy importante para la estructuración del trabajo y los resultados entregados.

Se llevaron a cabo actividades de adquisición y exploración de los datos, desarollo de los modelos con su respectiva evaluación y una versión final del modelo para despliegue. Cada uno de estas actividades se encuentra documentadas y los resultados detallados en los documentos elaborados en cada una de las etapas del proyecto y que hacen parte de los entregables del mismo.


## Resultados del proyecto

Los entregables del proyecto comprenden:

1. Carta de constitución del proyecto. 
2. Análisis exploratorio de los datos. Donde se presentan los hallazgos, resultados y decisiones tomadas para procesamiento de los mismos.
3. Implementación del preprocesamiento de los datos.
4. Implementación de la línea base del modelo y la implementación final del modelo.
5. Despliegue del modelo.
6. Documentación de cada una de las etapas del proyecto.

La evaluación final del modelo se encuentra documentada y puede ser consultada en el documento en _model_report_ y para destacar presento algunas de las conclusiones obtenidas:

1. Teniendo en cuenta las limitaciones en los recursos de cómputo disponibles en este proyecto y que se presentan en distintos proyectos, es importante considerar técnicas que permitan reducir la complejidad de los datos y que a su vez mantengan la información relevante. Por eso he considerado para una segunda fase de este proyecto usar técnicas de sumarización de texto con el propósito de reducir el tamaño del contenido de las noticias y poder usar este contenido (variable text) en el entrenamiento del modelo final seleccionado.
2. Aunque la implementación del modelo final seleccionado no se logró entrenar con la totalidad de los datos del dataset, se confirma ésta implementación como el modelo en esta fase del proyecto esperando probar esta implementación con mejores resultados computacionales y así lograr una comparación efectiva con el modelo Baseline elegido.
3. Aunque los resultados obtenidos en este modelo final pueden mejorarse dadas las limitaciones descritas. Todo este desarrollo de validar otros modelos hace parte de los proyectos de machine learning para lograr desarrollar conocimiento de otras implementaciones, entender su funcionamiento y ganar esa experiencia que se potencialice para futuros proyectos. 
4. En cuanto a la comparación de los resultados del modelo baseline y modelo final, las métricas nos muestran que el modelo baseline es mejor y cuenta con un nivel de confianza superior. 
5. Dados los resultados obtenidos con el modelo baseline y el modelo final y teniendo en cuenta las limitaciones para obtener una mejor versión del modelo final, se selecciona el modelo baseline como el artefacto a desplegar en la siguiente fase del proyecto.
6. Este proyecto ha sido desarrollado siguiendo las mejores prácticas y metodologías reconocidas de la industria lo cual es otro elemento importante para obtener resultados estructurados y permitir la evolución de trabajos como este.


## Impacto del proyecto

Este tipo de soluciones en la industria de medios que buscan de alguna manera controlar la proliferación de contenido falso que pueda llevar al público a tomar decisiones basadas en este tipo de contenido, a convencerlo de situaciones falsas y generar un desconocimiento son de gran relevancia para la población general. Y cada vez será más difícil, con el inmenso volumen de información que se genera constantemente, lograr algún tipo de control o de validación de la información que se dispone al público. Es por esto que soluciones basadas en Machine Learning representan un camino importante y posiblemente el único para lograr un control en la generación de este contenido falso y malintencionado.

Aunque en este proyecto se llevaron a cabo análisis y el desarrollo de varios modelos, este requiere más investigación y desarrollo considerando las limitaciones en infraestructura que me impidieron tener un modelo final con mejores resultados. No obstante, el modelo baseline entregó resultados realmente buenos y por ello lo seleccioné para la siguientes fases de despliegue del modelo.


## Conclusiones y lecciones aprendidas

1. Todas las etapas en un ciclo de vida de un proyecto de ciencias de datos son igualmente relevantes y es importante identificar los artefactos claves y resultados para no olvidar algo en el proceso. Esta guía entregada en este proyecto es un activo muy importante para llevar a cabo este tipo de proyectos no solo en el ámbito académico si no que es totalmente escalable al ámbito empresarial.
2. En este proyecto las limitaciones de infraestructura me limitaron para obtener mejores resultados en el modelo final y es acá donde destaco el papel relevante de la infraestructura en nube para ofrecer servicios que permitan desarrollar proyectos cada vez más complejos y que puede llegar ser imposible de adquirirlos de un modo distinto. 
3. La infraestructura es una variable importante en el desarrollo de proyectos de Machine Learning por eso es importante que desde un inicio  los distintos equipos de un proyecto: científicos de datos, ingenieros de machine learning, arquitectos y demás roles relevantes se encuentren presentes para llevar cabo las discusiones y la toma de decisiones para establecer la arquitectura, los recursos disponibles y las capacidades requeridas para lograr con éxito los resultados esperados.

## Agradecimientos

- Agradecimientos al equipo de trabajo y a los colaboradores que hicieron posible este proyecto.
- Agradecimientos especiales a los patrocinadores y financiadores del proyecto.
