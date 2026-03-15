from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('api/datos-sistema/', views.obtener_datos_sistema, name='datos_sistema'),
]