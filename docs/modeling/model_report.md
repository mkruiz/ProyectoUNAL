# Reporte del Modelo Final

## Resumen Ejecutivo

En esta sección se presentará un resumen de los resultados obtenidos del modelo final. Es importante incluir los resultados de las métricas de evaluación y la interpretación de los mismos.
El modelo final se basa en el uso del modelo de clasificación de deep learning y se ha implementado con el uso del modelo pre-entrenado BERT.

Las métricas de evaluación


En cuanto a las métricas obtenidas.


## Descripción del Problema

En distintos contextos de la comunicación de noticias y en especial en redes sociales es cada vez más común la mezcla de noticias reales y falsas y la dificultad para los lectores y consumidores de estas noticias de identificar que es real y que es falso. Las plataformas y en general algunas asociaciones de comunicadores se han preocupado por desarrollar mecanismos que les permitan la identificación de noticias falsas y que estos mecanimos se soporten de tecnología escalables y que puedan procesar grandes volumenes de información.

Es por esto que la inteligencia artificial y especialmente el Machine Learning alcanza un papel fundamental para proveer estos mecanismos que a través del entrenamiento puedan procesar grandes volúmenes de información, identificar las noticias falsas y que sean escalables de manera que su entrenamiento y actualización sea continúo en el tiempo para que no pierdan su efectividad en esta tarea de clasificación.

Particularmente en este proyecto se ha planteado desarrollar un mecanismo de identificación de noticias falsas con el uso de tecnologías de Machine Learning que apoye al área de análisis de medios en la iniciativa de control de noticias. 
    
Considerando el objetivo del proyecto se espera:
  1. Contar con un modelo de machine learning que permita identificar noticias falsas, dado un conjunto de noticias.
  2. El modelo implementado debe entregar el nivel de confianza de la predicción de manera que basado en un umbral acordado se establezcan las acciones a tomar.

El modelo final se seleccionado se describe en este documento y tiene como propósito responde al objetivos del proyecto descritos.


## Descripción del Modelo

En esta sección se describirá el modelo final que se desarrolló para resolver el problema planteado. Se debe incluir una descripción detallada del modelo, la metodología utilizada y las técnicas empleadas.

Como se ha mencionado en las secciones anteriores el modelo de clasificación implementado se basa en el uso del modelo pre-entrenado. La técnica de entrenamiento seleccionada para el Transfer Learning.

Descripción del modelo:

* Se congelan las capas del modelo BERT.
* Se compila el modelo definiendo Adam como optimizador y al tener dos neuronas de salida se usa la funci;on de pérdida: CategoricalCrossentropy. Además se usa una tasa de aprendizaje de 5e-6.
* Se define un stopping en callback, monitoreando la métrica "accuracy" en validación, patience de 5 y buscando maximizar el valor de accuracy en validación.
* Se define un checkpoint en callback, monitoreando la métrica "accuracy" en validación, patience de 5 y buscando maximizar el valor de accuracy en validación. Adicionalmente guardando los pesos del modelo con los mejores resultados.
* El parámetro validation_split (definición de la porción de datos usada para validación) es 0.2.
* Número de epochs = 10.
* Tamaño del batch = 1500.

Teniendo en cuenta los recursos computacionales para la implementación del presente modelo se tomaron las siguientes decisiones para lograr una versión entrenada del modelo y con resultados que pemitan ofrecer un mecanismo de clasificación de noticias reales y falsas:

* El entrenamiento no pudo hacerse con las variables title y text dado que la memoria del equipo de cómputo usado no era suficiente para la ejecución de las distintas funciones. Por ello se decidió solo usar la variable title.
* Adicionalmente y por las mismas razones de la infraestructura disponible se tomó una muestra de los datasets, 4000 registros de noticias falsas y 4000 registros de noticias reales.
* El número de epochs y el tamaño del batch también se selecionaron para lograr viabilidad en el entrenamiento del modelo.


## Evaluación del Modelo

En esta sección se presentará una evaluación detallada del modelo final. Se deben incluir las métricas de evaluación que se utilizaron y una interpretación detallada de los resultados.

## Conclusiones y Recomendaciones

En esta sección se presentarán las conclusiones y recomendaciones a partir de los resultados obtenidos. Se deben incluir los puntos fuertes y débiles del modelo, las limitaciones y los posibles escenarios de aplicación.

Como resultado de la implementación del Modelo Final descrito en este documento y las distintas actividades que involucra emprender un proyecto de este alcance se establecen las siguientes conclusiones:

1. Teniendo en cuenta las limitaciones en los recursos de cómputo disponibles en este proyecto y que se presentan en distintos proyectos es importante considerar técnicas que permitan reducir la complejidad de los datos y que a su vez mantengan la información relevante. Por eso he considerado para una segunda fase de este proyecto usar técnicas de sumarización de texto con el propósito de reducir el tamaño del contenido de las noticias y poder usar este contenido (variable text) en el entrenamiento del modelo final seleccionado.
2. Aunque la implementación del modelo final seleccionado no se logró entrenar con la totalidad de los datos del dataset, se confirma su uso en este paso esperando probar esta implementación con mejores resultados computacionales y así lograr una comparación efectiva con el modelo Baseline elegido.
3. La infraestructura es una variable importante en el desarrollo de proyectos de Machine Learning por eso es importante que desde un inicio  los distintos equipos de un proyecto: científicos de datos, ingenieros de machine learning, arquitectos y demás roles relevantes se encuentren presenter para llevar cabo las discusiones y la toma de decisiones para establecer la arquitectura, los recursos disponibles y las capacidades requeridas para lograr con éxito los resultados esperados.
4. Comparacion con baseline
5. Métricas


## Referencias

[Bert Model Documentation](https://huggingface.co/docs/transformers/model_doc/bert)

