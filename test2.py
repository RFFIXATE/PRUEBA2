import subprocess
import time

while True:
    # Obtener la información de los recursos de hardware
    disk_usage = subprocess.check_output(['df', '-h'])
    memory_usage = subprocess.check_output(['free', '-h'])
    cpu_usage = subprocess.check_output(['top', '-n', '1', '-b'])
    network_status = subprocess.check_output(['ifconfig'])

    # Imprimir los resultados
    print("Espacio en disco:")
    print(disk_usage.decode('utf-8'))
    print("\nUso de memoria:")
    print(memory_usage.decode('utf-8'))
    print("\nUso de CPU:")
    print(cpu_usage.decode('utf-8'))
    print("\nEstado de la red:")
    print(network_status.decode('utf-8'))

    # Esperar 10 segundos antes de la siguiente iteración
    time.sleep(10)
