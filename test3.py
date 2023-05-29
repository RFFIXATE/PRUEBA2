# pip install requests pandas
# para actualizar python.exe -m pip install --upgrade pip
# pip3 install requests

import requests
import csv

# Realizar la solicitud HTTP al endpoint
response = requests.get("https://dummyjson.com/quotes")

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener los datos de la respuesta en formato JSON
    data = response.json()

    # Extraer los valores de los campos "autor" y "texto"
    quotes = data['quotes']
    values = [[quote['autor'], quote['texto']] for quote in quotes]

    # Guardar los valores en un archivo CSV
    with open("endpoint.csv", mode='w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["autor", "texto"])  # Escribir la cabecera
        writer.writerows(values)  # Escribir los valores

    print("Archivo CSV guardado exitosamente.")
else:
    print("Error al realizar la solicitud al endpoint.")


