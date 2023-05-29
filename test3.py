# pip install requests pandas
# para actualizar python.exe -m pip install --upgrade pip
# pip3 install requests


import requests
import csv

response = requests.get("https://dummyjson.com/quotes")
data = response.json()

quotes = data.get("quotes", [])  # Obtener la lista de citas, o una lista vacía si no hay citas

if quotes:
    with open("endpoint.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter="\t")
        writer.writerow(["autor", "texto"])  # Escribir el encabezado en el archivo CSV

        for quote in quotes:
            author = quote.get("autor", "Desconocido")  # Obtener el autor, o usar "Desconocido" si no está presente
            text = quote.get("texto", "")  # Obtener el texto, o una cadena vacía si no está presente
            writer.writerow([author, text])  # Escribir los datos en el archivo CSV

    print("Los datos se han guardado correctamente en el archivo 'endpoint.csv'.")
else:
    print("No se encontraron citas en los datos obtenidos.")

