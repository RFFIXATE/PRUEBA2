# pasos para ser probado en AWS cloud
# en amazon AWS sudo yum install python3-pip -y
# verificar version python3 --version
# pip3 --version
# sudo yum install git -y
#considerando que nosotros utilizamos la máquian virtual en aws nuestra ruta es /var/log/audit/audit.log en caso de utilizar la máquina de clases es /var/log/secure

import subprocess
import datetime

# Obtener la fecha y hora actual
now = datetime.datetime.now()

# Calcular la última hora cerrada
last_closed_hour = now.replace(minute=0, second=0, microsecond=0) - datetime.timedelta(hours=1)

# Obtener la fecha y hora de inicio y finalización del rango
if last_closed_hour.hour == 0:  # Si la última hora es medianoche
    start_time = last_closed_hour.replace(hour=23)
    end_time = last_closed_hour
else:
    start_time = last_closed_hour.replace(hour=last_closed_hour.hour - 1)
    end_time = last_closed_hour

# Formatear las fechas y horas como cadenas
start_time_str = start_time.strftime("%b %d %H")
end_time_str = end_time.strftime("%b %d %H")

# Construir el comando grep para filtrar el archivo de registro
grep_command = f"grep 'authentication' /var/log/audit/audit.log | grep '{start_time_str}\|{end_time_str}'"

try:
    # Ejecutar el comando grep y contar las líneas de salida
    output = subprocess.check_output(grep_command, shell=True)
    failed_attempts = len(output.decode().split('\n')) - 1
except subprocess.CalledProcessError:
    # Si no hay coincidencias, establecer la cantidad de intentos fallidos en 0
    failed_attempts = 0

# Mostrar el resultado
print(f"Cantidad de intentos fallidos de inicio de sesión en el rango {start_time_str}:00 - {end_time_str}:00: {failed_attempts}")

