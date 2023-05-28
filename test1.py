import subprocess
from datetime import datetime, timedelta

# Obtener la fecha y hora actual
now = datetime.now()

# Definir la hora de inicio y finalización del rango de tiempo deseado
start_time = datetime(now.year, now.month, now.day, 9, 0)
end_time = datetime(now.year, now.month, now.day, 9, 59)

# Verificar si hay cambio de día
if now.hour < 9:
    # Cambio de día anterior
    start_time -= timedelta(days=1)
    end_time -= timedelta(days=1)

# Obtener el rango de horas para buscar
hours_range = []
current_time = start_time
while current_time <= end_time:
    hours_range.append(current_time.strftime("%H:%M"))
    current_time += timedelta(hours=1)

# Comando grep para buscar los intentos fallidos en los archivos de registro
grep_command = f"grep 'authentication failure' /var/log/auth.log | grep -E ' {'|'.join(hours_range)} ' | wc -l"
result = subprocess.run(grep_command, shell=True, capture_output=True, text=True)

# Obtener la cantidad total de intentos fallidos de inicio de sesión
failed_attempts = int(result.stdout.strip())

# Imprimir el resultado
print(f"La cantidad total de intentos fallidos de inicio de sesión en el rango {start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')} es: {failed_attempts}")
