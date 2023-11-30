# Spike Protein Analysis
## Proyecto Final para la clase de BioPython impartida en la Licenciatura en Ciencias Genómicas - UNAM
### Ana Marisol García Mejía: anagm@lcg.unam.mx
### Valentina Janet Arias Ojeda: vjarias@lcg.unam.mx
#### Introducción
El virus SARS-CoV-2 responsable de la pandemia por la enfermedad COVID-2019, ha tenido un gran impacto en la salud mundial, con un aproximado de 700 millones de casos de infección y 6.9 millones de muertes. Presentan un amplio espectro de indicadores clínicos desde infección respiratoria asintomática hasta neumonía grave asociada al síndrome de distrés respiratorio agudo, y de igual manera varios factores de riesgo pueden ser causa de esta variación

La proteína Spike, también conocida como S-proteína, es una estructura clave que se encuentra en la superficie de los coronavirus. Esta proteína desempeña un papel fundamental en el proceso de infección al facilitar la entrada del virus en las células huésped.

La estructura tridimensional de la proteína Spike presenta características únicas que la hacen crucial para comprender la patogénesis viral, así como para el desarrollo de terapias y vacunas efectivas. Su interacción con el receptor de la célula huésped es un punto de enfoque en la investigación biomédica para comprender la transmisión viral y el desarrollo de estrategias terapéuticas.

Este repositorio contiene herramientas y scripts para analizar la secuencia de la proteína S en diferentes cepas/variantes del virus SARS-Cov-2. Proporcionando información fundamental para la búsqueda de mutaciones o predicción de estructura.

#### Estructura del Repositorio
```
├───data
├───results
└───src
```
1. *data:* 
Contiene los archivos recuperados de GenBank en formato ```.gb``` y el archivo fasta generado con las secuencias de la proteína. 
2. *results:*
Aquí se almacenan los resultados generados por el análisis de las secuencias proteicas; visualizaciones y gráficos derivados del procesamiento de las secuencias.
3. *src:*
La carpeta src contiene todos los scripts y códigos fuente utilizados para el análisis, procesamiento y visualización de los datos. Incluye funciones, utilidades, y programas que realizan tareas específicas para el estudio de las proteínas.
