Monitor del Sistema

Aplicacion web desarrollada con Django que muestra informacion en tiempo real del sistema utilizando la libreria psutil.

Caracteristicas

- Monitoreo de CPU (porcentaje de uso y numero de nucleos)
- Monitoreo de memoria RAM (usado, total y porcentaje)
- Monitoreo de disco duro (usado, libre y total)
- Informacion del sistema operativo
- Actualizacion automatica cada 5 segundos
- Interfaz responsive con tarjetas informativas

Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional)

Instalacion

1. Clonar o descargar el repositorio:
git clone <url-del-repositorio>
cd monitor_app
2. Crear el contenedor:
docker compose build
docker compose up