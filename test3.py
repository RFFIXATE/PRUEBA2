# pip install requests pandas
# para actualizar python.exe -m pip install --upgrade pip
# pip3 install requests

import requests
import pandas as pd

# Realizar la solicitud GET al endpoint
response = requests.get("https://dummyjson.com/quotes")

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()

    # Obtener los valores de los campos "autor" y "texto"
    quotes = data["quotes"]
    authors = [quote["autor"] for quote in quotes]
    texts = [quote["texto"] for quote in quotes]

    # Crear un DataFrame con los datos
    df = pd.DataFrame({"autor": authors, "texto": texts})

    # Guardar los datos en un archivo CSV
    df.to_csv("endpoint.csv", sep="\t", index=False, line_terminator="\n")

    print("Los datos se han guardado correctamente en el archivo 'endpoint.csv'.")
else:
    print("No se pudo acceder al endpoint.")


