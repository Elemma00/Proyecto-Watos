import re
import requests

with open('trends.rdf', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('trends_updated.ttl', 'w', encoding='utf-8') as f:
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
            if data['search']:
                concept_uri = data['search'][0]['concepturi']
                # append a line to link the current entity with the corresponding wikidata entity
                f.write(f'    ex:wikidata <{concept_uri}> ;\n')
            else:
                continue
         