from preprocesamiento import csv_preprocessing, csv_to_ttl, link_rdf_to_wikidata
from inferencia import reasoner

# Se genera el archivo trends_processed.csv, eliminando caracteres no deseados
csv_preprocessing.process_special_characters('./preprocesamiento/trends.csv', './preprocesamiento/trends_processed.csv')

# Se genera el archivo ttl
csv_to_ttl.csv_to_ttl('./preprocesamiento/trends.ttl')

# Se genera el archivo trends_updated, utilizando conceptos de wikidata (demora bastante, 4 horas aprox)
#link_rdf_to_wikidata.link_rdf_to_wikidata()

# Se genera el archivo inferred_trends, según las reglas de inferencia establecidas
reasoner.reasoner()
