#pip3 install psutil

import psutil
import platform
import subprocess
import time

while True:
    # Obtener información sobre el disco
    disk_usage = psutil.disk_usage('/')
    total_disk = disk_usage.total
    used_disk = disk_usage.used
    free_disk = disk_usage.free

    # Obtener información sobre la memoria
    memory = psutil.virtual_memory()
    total_memory = memory.total
    used_memory = memory.used
    free_memory = memory.available

    # Obtener información sobre la CPU
    cpu_percent = psutil.cpu_percent()
    cpu_count = psutil.cpu_count()

    # Obtener información sobre la red
    network = psutil.net_io_counters()
    bytes_sent = network.bytes_sent
    bytes_received = network.bytes_recv

    # Imprimir los resultados en pantalla
    print("Recursos de hardware disponibles:")
    print(f"Disco: Total={total_disk}B, Usado={used_disk}B, Libre={free_disk}B")
    print(f"Memoria: Total={total_memory}B, Usada={used_memory}B, Libre={free_memory}B")
    print(f"CPU: Uso={cpu_percent}%, Núcleos={cpu_count}")
    print(f"Red: Bytes enviados={bytes_sent}, Bytes recibidos={bytes_received}")

    # Esperar 10 segundos antes de volver a obtener la información
    time.sleep(10)
