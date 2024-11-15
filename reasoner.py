from owlrl import DeductiveClosure, OWLRL_Semantics
import rdflib


# Crear un objeto Graph en rdflib
g = rdflib.Graph()

# Cargar tu archivo RDF/OWL
g.parse("trends.ttl", format="ttl")
g.parse("reglas_inferencias.ttl", format="ttl")

closure = DeductiveClosure(OWLRL_Semantics)

# Paso 5: Expansión de inferencias
closure.expand(g)
# Mostrar las triples inferidas
g.serialize(destination='infered_trend.ttl', format='turtle')
