# Spike Protein Analysis
## Proyecto Final para la clase de BioPython impartida en la Licenciatura en Ciencias Genómicas - UNAM
### Ana Marisol García Mejía: anagm@lcg.unam.mx
### Valentina Janet Arias Ojeda: vjarias@lcg.unam.mx
#### Introducción
El virus SARS-CoV-2 responsable de la pandemia por la enfermedad COVID-2019, ha tenido un gran impacto en la salud mundial, con un aproximado de 700 millones de casos de infección y 6.9 millones de muertes. Presentan un amplio espectro de indicadores clínicos desde infección respiratoria asintomática hasta neumonía grave asociada al síndrome de distrés respiratorio agudo, y de igual manera varios factores de riesgo pueden ser causa de esta variación

La proteína Spike, también conocida como S-proteína, es una estructura clave que se encuentra en la superficie de los coronavirus. Esta proteína desempeña un papel fundamental en el proceso de infección al facilitar la entrada del virus en las células huésped.

La estructura tridimensional de la proteína Spike presenta características únicas que la hacen crucial para comprender la patogénesis viral, así como para el desarrollo de terapias y vacunas efectivas. Su interacción con el receptor de la célula huésped es un punto de enfoque en la investigación biomédica para comprender la transmisión viral y el desarrollo de estrategias terapéuticas.

Este repositorio contiene herramientas y scripts para analizar la secuencia de la proteína S en diferentes cepas o variantes del virus SARS-Cov-2. Proporcionando información fundamental para la búsqueda de mutaciones o predicción de estructura.

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
#### Procedimiento
- Recuperación de IDs de NCBI para las cepas deseadas.

  Este paso implica la utilización de herramientas como la API de NCBI (Entrez) en Python para buscar y obtener los identificadores (IDs) de las cepas específicas de interés, como las variantes de la proteína Spike de diferentes cepas de coronavirus.
  ```
    # Ejecución de comandos desde la carpeta src
    python retrieve_strains delta alpha omicron
  ```
- Almacenamiento de archivos GenBank.

  Una vez obtenidos los IDs de las cepas deseadas, se procede a recuperar los archivos GenBank correspondientes a cada ID. Estos archivos contienen información detallada sobre la secuencia de ADN, incluyendo la información de la proteína Spike.
  ```
    # Proceder con la descarga de archivos
    yes
  ```
- Procesamiento de archivos y extracción de secuencia de interés.

  Se lleva a cabo el procesamiento de los archivos GenBank para extraer la secuencia de la proteína Spike.
  ```
    # Ejecución de segundo programa
    python fasta_generator.py
  ```
- Generación de archivo fasta.

  Con la secuencia de la proteína Spike extraída, se genera un archivo en formato FASTA que contiene la cepa y secuencia.

- Análisis de longitud de secuencias.

  Se analiza la longitud de las secuencias de la proteína Spike obtenidas de las diferentes cepas. Esto puede proporcionar información importante sobre la variabilidad en la longitud de la proteína entre las distintas cepas de coronavirus.
  ```
  python histogram.py
  ```
- Analisis de contenido de aminoácidos.

  Se lleva a cabo un análisis detallado del contenido de aminoácidos en las secuencias de la proteína Spike. Esto puede incluir la frecuencia y distribución de los diferentes aminoácidos presentes en las secuencias, lo cual es relevante para comprender la estructura y la función de la proteína.
  ```
  python aminoacid_count.py
  ```
  
