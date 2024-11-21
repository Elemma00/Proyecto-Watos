import csv
import re

# Función para procesar caracteres especiales
def process_special_characters(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            processed_row = [col.encode('utf-8').decode('utf-8') for col in row]
            # delete " character
            processed_row = [col.replace('"', '') if i == 4 else col for i, col in enumerate(processed_row)]
            # delete (something) regular expression only for column query
            processed_row = [re.sub(r'\(.*\)', '', col) if i == 4 else col for i, col in enumerate(processed_row)]
            writer.writerow(processed_row)
    outfile.close()
    print(f"Archivo procesado y guardado como {output_file}")
