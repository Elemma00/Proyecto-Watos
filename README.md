# Descripción del proyecto
Este proyecto busca estructurar datos de Google Trends en un modelo RDF para facilitar su análisis mediante consultas SPARQL. Al integrar esta información con Wikidata, se enriquece el contexto de las tendencias, permitiendo explorar relaciones más complejas y realizar análisis semánticos avanzados.

# Instrucciones
## Ejecutar preprocesamiento, búsqueda de conceptos en wikidata e inferencia
Para realizar todos estos pasos y obtener un archivo inferred_trends.ttl con el cual hacer consultas, solo se debe ejecutar el archivo main.py en la carpeta raíz con el comando. La búsqueda de conceptos en wikidata demora aproximadamente 4 horas, por lo que si se desea, se puede utilizar el archivo _trends_updated.ttl_ ya generado previamente.
    
``` bash
python main.py
```

## Ejecutar Apache Jena Fuseki
Para ejecutar Apache Jena Fuseki, se debe ejecutar el archivo `fuseki-server.bat` dentro de la carpeta correspondiente. Esto iniciará el servidor en el puerto `3030`.

Con esto, se pueden ejecutar las consultas SPARQL presentes en el archivo _consultas.sparql_.
