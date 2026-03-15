import psutil
import platform

def obtener_info_cpu():
    try:
        porcentaje_cpu = psutil.cpu_percent(interval=1)
        nucleos_cpu = psutil.cpu_count(logical=True)
        return {'porcentaje': porcentaje_cpu, 'nucleos': nucleos_cpu}
    except:
        return {'porcentaje': 'N/A', 'nucleos': 'N/A'}

def obtener_info_ram():
    try:
        memoria = psutil.virtual_memory()
        total_gb = round(memoria.total / (1024**3), 2)
        usado_gb = round(memoria.used / (1024**3), 2)
        porcentaje = memoria.percent
        return {'total': total_gb, 'usado': usado_gb, 'porcentaje': porcentaje}
    except:
        return {'total': 'N/A', 'usado': 'N/A', 'porcentaje': 'N/A'}

def obtener_info_disco():
    try:
        disco = psutil.disk_usage('/')
        total_gb = round(disco.total / (1024**3), 2)
        usado_gb = round(disco.used / (1024**3), 2)
        libre_gb = round(disco.free / (1024**3), 2)
        return {'total': total_gb, 'usado': usado_gb, 'libre': libre_gb}
    except:
        return {'total': 'N/A', 'usado': 'N/A', 'libre': 'N/A'}

def obtener_info_so():
    try:
        nombre_so = platform.system()
        version_so = platform.version()
        return {'nombre': nombre_so, 'version': version_so}
    except:
        return {'nombre': 'N/A', 'version': 'N/A'}