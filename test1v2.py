import os
import datetime

# Definir el rango de tiempo de la última hora cerrada
last_closed_hour = (datetime.datetime.now() - datetime.timedelta(hours=1)).replace(minute=0, second=0)
start_time = last_closed_hour.strftime('%Y-%m-%d %H')
end_time = last_closed_hour.strftime('%Y-%m-%d %H:%M:%S')

# Abrir el archivo de registro
with open('/var/log/audit/audit.log', 'r') as archivo:
    # Inicializar contador de intentos fallidos
    failed_attempts_count = 0
    
    # Leer cada línea del archivo
    for linea in archivo:
        # Buscar las líneas que contienen "authentication" y están dentro del rango de tiempo
        if 'authentication' in linea and start_time in linea and end_time in linea:
            # Incrementar el contador de intentos fallidos
            failed_attempts_count += 1

# Mostrar el resultado
print(f"Cantidad de intentos fallidos de inicio de sesión en el rango {start_time} - {end_time}: {failed_attempts_count}")
