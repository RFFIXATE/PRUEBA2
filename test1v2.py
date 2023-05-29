import os
import datetime

# Obtener la hora actual
now = datetime.datetime.now()

# Definir el rango de tiempo de la última hora cerrada
last_closed_hour = now - datetime.timedelta(hours=1)
start_time = last_closed_hour.strftime('%Y-%m-%d %H:%M:%S')
end_time = now.strftime('%Y-%m-%d %H:%M:%S')

# Obtener el día actual en formato 'May 29'
current_day = now.strftime('%b %d')

# Manejar el cambio de día
if last_closed_hour.day != now.day:
    current_day = last_closed_hour.strftime('%b %d') + ' - ' + now.strftime('%b %d')

# Abrir el archivo de registro
with open('/var/log/audit/audit.log', 'r') as archivo:
    # Inicializar contador de intentos fallidos
    failed_attempts_count = 0
    
    # Leer cada línea del archivo
    for linea in archivo:
        # Buscar las líneas que contienen "authentication" y están dentro del rango de tiempo
        if 'authentication' in linea and current_day in linea:
            timestamp = linea.split()[1]
            # Obtener la hora de la línea en formato 'HH:MM:SS'
            hora = datetime.datetime.strptime(timestamp, '%H:%M:%S').strftime('%H:%M:%S')
            # Verificar si la hora está dentro del rango deseado
            if start_time <= hora <= end_time:
                # Incrementar el contador de intentos fallidos
                failed_attempts_count += 1

# Mostrar el resultado
print(f"Cantidad de intentos fallidos de inicio de sesión en el rango {current_day} {start_time} - {end_time}: {failed_attempts_count}")
