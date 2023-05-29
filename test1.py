# pasos para ser probado en AWS cloud
# en amazon AWS sudo yum install python3-pip -y
# verificar version python3 --version
# pip3 --version
# sudo yum install git -y

import subprocess
import datetime

# Obtener la fecha y hora actual
now = datetime.datetime.now()

# Calcular la última hora cerrada
last_hour = now.replace(minute=0, second=0, microsecond=0) - datetime.timedelta(hours=1)

# Obtener el rango de tiempo para la última hora cerrada
if last_hour.hour == 0:  # Si la última hora es medianoche
    start_time = last_hour.replace(hour=23)
    end_time = last_hour
else:
    start_time = last_hour.replace(hour=last_hour.hour - 1)
    end_time = last_hour

# Formatear el rango de tiempo como cadena
start_time_str = start_time.strftime("%b %d %H")
end_time_str = end_time.strftime("%b %d %H")

# Construir el comando grep para filtrar el archivo de registro
grep_command = f"grep 'Failed password' /var/log/audit/audit.log | grep '{start_time_str}\|{end_time_str}'"

# Ejecutar el comando grep y contar las líneas de salida
output = subprocess.check_output(grep_command, shell=True)
failed_attempts = len(output.decode().split('\n')) - 1

# Mostrar el resultado
print(f"Cantidad de intentos fallidos de inicio de sesión en el rango {start_time_str}:00 - {end_time_str}:59: {failed_attempts}")
