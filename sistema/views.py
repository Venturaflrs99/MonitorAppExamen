from django.shortcuts import render
from django.http import JsonResponse
from . import informacion_sistema

def pagina_principal(request):
    return render(request, 'home.html')

def obtener_datos_sistema(request):
    datos = {
        'cpu': informacion_sistema.obtener_info_cpu(),
        'ram': informacion_sistema.obtener_info_ram(),
        'disco': informacion_sistema.obtener_info_disco(),
        'so': informacion_sistema.obtener_info_so()
    }
    return JsonResponse(datos)