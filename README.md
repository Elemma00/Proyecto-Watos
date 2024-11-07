# Instrucciones

## Ejecutar Apache Jena Fuseki

Para ejecutar Apache Jena Fuseki, se debe ejecutar el archivo `fuseki-server.bat` dentro de la carpeta correspondiente. Esto iniciará el servidor en el puerto `3030`.

## Convertir CSV a RDF

Para convertir el archivo CSV a RDF, se creó el archivo `constructor.sparql` que, tomando las columnas del archivo CSV, crea entidades con los respectivos atributos.
Se debe ejecutar esto `.\tarql-1.2\bin\tarql.bat constructor.sparql trends.csv > relations.rdf` 

## 