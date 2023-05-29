
import csv
from collections import Counter
import re

excluded_words = ['the', 'a', 'an', 'and', 'or', 'but', 'for', 'with', 'in', 'on', 'at', 'to', 'from']  # Palabras a excluir en inglés

word_counter = Counter()  # Contador de palabras

with open("endpoint.csv", mode='r') as file:
    reader = csv.reader(file, delimiter='\t')
    next(reader)  # Omitir la primera fila (cabecera)
    for row in reader:
        quote = row[1]
        words = re.findall(r'\b\w+(?:\'\w+)?\b', quote)  # Extraer palabras de la cita

        # Incrementar el contador de palabras (excluyendo las palabras excluidas)
        for word in words:
            if word.lower() not in excluded_words:
                word_counter[word.lower()] += 1

# Obtener las diez palabras más repetidas
top_ten = word_counter.most_common(10)

# Mostrar el ranking
print("Ranking de las diez palabras más repetidas:")
for i, (word, count) in enumerate(top_ten, start=1):
    print(f"{i}. Palabra: {word}, Repeticiones: {count}")


