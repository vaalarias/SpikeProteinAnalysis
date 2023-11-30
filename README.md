# Spike Protein Analysis
## Proyecto Final para la clase de BioPython impartida en la Licenciatura en Ciencias Genómicas - UNAM
### Ana Marisol García Mejía: anagm@lcg.unam.mx
### Valentina Arias: vjarias@lcg.unam.mx
## Introducción
El virus SARS-CoV-2 responsable de la pandemia por la enfermedad COVID-2019, ha tenido un gran impacto en la salud mundial, con un aproximado de 700 millones de casos de infección y 6.9 millones de muertes. Presentan un amplio espectro de indicadores clínicos desde infección respiratoria asintomática hasta neumonía grave asociada al síndrome de distrés respiratorio agudo, y de igual manera varios factores de riesgo pueden ser causa de esta variación

La proteína Spike, también conocida como S-proteína, es una estructura clave que se encuentra en la superficie de los coronavirus. Esta proteína desempeña un papel fundamental en el proceso de infección al facilitar la entrada del virus en las células huésped.

La estructura tridimensional de la proteína Spike presenta características únicas que la hacen crucial para comprender la patogénesis viral, así como para el desarrollo de terapias y vacunas efectivas. Su interacción con el receptor de la célula huésped es un punto de enfoque en la investigación biomédica para comprender la transmisión viral y el desarrollo de estrategias terapéuticas.

Este repositorio contiene herramientas y scripts para analizar la secuencia de la proteína S en diferentes cepas o variantes del virus SARS-Cov-2. Proporcionando información fundamental para la búsqueda de mutaciones o predicción de estructura.

## Estructura del Repositorio
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
## Procedimiento
- Recuperación de IDs de NCBI para las cepas deseadas.

  Este paso implica la utilización de herramientas como la API de NCBI (Entrez) en Python para buscar y obtener los identificadores (IDs) de las cepas específicas de interés, como las variantes de la proteína Spike de diferentes cepas de coronavirus.
  ```
    # Ejecución de comandos desde la carpeta src
    python retrieve_strains delta alpha omicron
  ```
- Almacenamiento de archivos GenBank.

  Una vez obtenidos los IDs de las cepas deseadas, se procede a recuperar los archivos GenBank correspondientes a cada ID. Estos archivos contienen información detallada sobre las secuencias proteicas, incluyendo la información de la proteína Spike.
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

  Con la secuencia de la proteína Spike extraída, se genera un archivo en formato FASTA que contiene la cepa y secuencia. Este archivo se guarda en la carpeta data con el nombre `s_protein.fasta`.

- Análisis de longitud de secuencias.

  Se analiza la longitud de las secuencias de la proteína Spike obtenidas de las diferentes cepas. Esto puede proporcionar información importante sobre la variabilidad en la longitud de la proteína entre las distintas cepas de coronavirus.
  ```
  python histogram.py
  ```
- Analisis de contenido de aminoácidos.

  Se lleva a cabo un análisis del contenido de aminoácidos en las secuencias de la proteína Spike. Esto incluye la frecuencia y distribución de los diferentes aminoácidos presentes en las secuencias, lo cual es relevante para comprender la estructura y la función de la proteína.
  ```
  python aminoacid_count.py
  ```

## Objetivo
Nuestro enfoque central es profundizar la comprensión de la variabilidad presente en las secuencias de la proteína-S de diferentes cepas del virus SARS-Cov-2.

## Resultados
A partir de los análisis realizados con las secuencias de la proteína correspondiente a cada una de las tres cepas ingresadas recuperamos gráficos para visualizar la información recolectada.
  - Histograma de largo de las secuencias
   ![](/results/histogram.png)
  
  - Contenido de aminoácidos correspondientes a la variante Alpha:
    ![](/results/aa_count_plot_SARS_CoV_2_human_CHE_SARS_CoV_2.png)
  
  - Contenido de aminoácidos correspondientes a la variante Delta:
    ![](/results/aa_count_plot_SARS_CoV_2_human_NLD_EMC_Delta_AY4_2_2021.png)
  
  - Contenido de aminoácidos correspondientes a la variante Omicron:
    ![](/results/aa_count_plot_SARS_CoV_2_human_KAZ_Omicron_XBB_1_9_1_406_2023.png)


## Conclusiones

La exploración detallada de las secuencias permite visualizar la diversidad genética entre las cepas, resaltando las áreas conservadas y las regiones propensas a variaciones. Además, el análisis revela una variación en las secuencias de la proteína S entre diferentes cepas de coronavirus. Estas variaciones pueden estar relacionadas con la adaptación del virus a diferentes entornos y la respuesta inmune del huésped. Finalmente, el uso de herramientas computacionales para automatizar la recuperación de datos, el procesamiento de archivos genéticos y la extracción de información relevante permite difundir conocimientos y metodologías que puedan ser aprovechados por la comunidad científica y académica.

## Referencias
1. Candido KL, Eich CR, de Fariña LO, Kadowaki MK, da Conceição Silva JL, Maller A, Simão RCG. Spike protein of SARS-CoV-2 variants: a brief review and practical implications. Braz J Microbiol. 2022 Sep;53(3):1133-1157. doi: 10.1007/s42770-022-00743-z. Epub 2022 Apr 9. PMID: 35397075; PMCID: PMC8994061.
2. WHO. WHO Coronavirus (COVID-19) Dashboard. 2023. https://covid19.who.int/ . Accessed 29 Noviembre 2023
