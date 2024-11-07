import re
import requests

with open('relations.rdf', 'r', encoding='utf-16') as f:
    lines = f.readlines()

with open('relations_updated.rdf', 'w', encoding='utf-16') as f:
    for line in lines:
        f.write(line)
        # if the line contains a query, extract the name of the query
        match = re.search(r'ex:query\s+"([^"]+)"', line)
        if match:
            name = match.group(1)
            # search in wikidata for the corresponding entity
            url = "https://www.wikidata.org/w/api.php"
            params = {
                'action': 'wbsearchentities',
                'search': name,
                'language': 'en',
                'format': 'json'
            }
            response = requests.get(url, params=params)
            data = response.json()
            concept_uri = data['search'][0]['concepturi']
            # append a line to link the current entity with the corresponding wikidata entity
            f.write(f'        ex:wikidata <{concept_uri}> .\n')