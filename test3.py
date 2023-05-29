# pip install requests pandas
# para actualizar python.exe -m pip install --upgrade pip
# pip3 install requests

import requests
import csv

response = requests.get("https://dummyjson.com/quotes")
if response.status_code == 200:
    data = response.json()
    quotes = data['quotes']
    values = [[quote['author'], quote['quote']] for quote in quotes]

    with open("endpoint.csv", mode='w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["author", "quote"])
        writer.writerows(values)

    print("Archivo CSV guardado exitosamente.")
else:
    print("Error al realizar la solicitud al endpoint.")


