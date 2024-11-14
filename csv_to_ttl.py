import csv
import uuid
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF

# Define el namespace
EX = Namespace("http://example.org/trends#")

# Crea un gráfico RDF
g = Graph()

# Añade el prefijo al gráfico
g.bind("ex", EX)

# Lee el archivo CSV
with open('trends_processed.csv', mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Genera un UUID para cada registro
        record_uri = URIRef(f"http://example.org/trends/record/{uuid.uuid4()}")
        
        # Añade triples al gráfico
        g.add((record_uri, RDF.type, EX.TrendRecord))
        g.add((record_uri, EX.location, Literal(row['location'])))
        g.add((record_uri, EX.year, Literal(row['year'])))
        g.add((record_uri, EX.category, Literal(row['category'])))
        g.add((record_uri, EX.rank, Literal(row['rank'])))
        g.add((record_uri, EX.query, Literal(row['query'])))

# Guarda el gráfico en un archivo RDF
g.serialize(destination='trends.ttl', format='turtle')

print("Archivo RDF generado correctamente.")