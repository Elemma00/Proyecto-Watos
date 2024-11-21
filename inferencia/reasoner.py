from owlrl import DeductiveClosure, OWLRL_Semantics
import rdflib

def reasoner():
    # Create an rdflib Graph object
    g = rdflib.Graph()

    # Load your RDF/OWL files
    g.parse("./preprocesamiento/trends_updated.ttl", format="ttl")
    g.parse("./inferencia/reglas_inferencias.ttl", format="ttl")

    closure = DeductiveClosure(OWLRL_Semantics)

    # Expand inferences
    closure.expand(g)

    # Filter out unwanted inferences
    unwanted_triples = []
    for s, p, o in g:
        if (p == rdflib.OWL.sameAs and s == o) or (o in [rdflib.XSD.decimal, rdflib.XSD.integer]):
            unwanted_triples.append((s, p, o))
        # Check if the subject is not a URI or a blank node
        if not (isinstance(s, rdflib.URIRef) or isinstance(s, rdflib.BNode)):
            unwanted_triples.append((s, p, o))

    for triple in unwanted_triples:
        g.remove(triple)

    # Serialize the graph with inferred triples
    g.serialize(destination='./inferencia/inferred_trends.ttl', format='turtle')
    print("Inferencias realizadas y guardadas en inferred_trend.ttl")