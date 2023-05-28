import requests
import csv

# Realizar la solicitud GET al endpoint
response = requests.get("https://dummyjson.com/quotes")

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()

    # Obtener los valores de los campos "autor" y "texto"
    quotes = data["quotes"]
    authors = [quote["autor"] for quote in quotes]
    texts = [quote["texto"] for quote in quotes]

    # Guardar los datos en un archivo CSV
    with open("endpoint.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter="\t")
        writer.writerow(["autor", "texto"])  # Escribir la cabecera
        for i in range(len(quotes)):
            writer.writerow([authors[i], texts[i]])  # Escribir los datos

    print("Los datos se han guardado correctamente en el archivo 'endpoint.csv'.")
else:
    print("No se pudo acceder al endpoint.")
