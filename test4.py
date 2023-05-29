#pip install pandas nltk
# pip3 install nltk

import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Cargar el archivo CSV en un DataFrame de pandas
df = pd.read_csv("endpoint.csv", delimiter="\t")

# Obtener la columna "texto" como una lista de cadenas
textos = df["texto"].tolist()

# Unir todos los textos en una sola cadena
texto_completo = " ".join(textos)

# Tokenizar el texto en palabras
tokens = nltk.word_tokenize(texto_completo)

# Obtener las palabras vacías (artículos, conectores, etc.) en el idioma inglés
nltk.download('stopwords')
palabras_vacias = set(stopwords.words('english'))

# Filtrar las palabras vacías y los signos de puntuación
palabras_filtradas = [palabra.lower() for palabra in tokens if palabra.lower() not in palabras_vacias and palabra.isalpha()]

# Contar la frecuencia de cada palabra
frecuencia_palabras = Counter(palabras_filtradas)

# Obtener el ranking top ten de palabras más repetidas
top_ten = frecuencia_palabras.most_common(10)

# Imprimir el resultado
print("Ranking Top Ten de palabras más repetidas (excluyendo artículos y conectores):")
for palabra, frecuencia in top_ten:
    print(f"Palabra: {palabra} - Frecuencia: {frecuencia}")