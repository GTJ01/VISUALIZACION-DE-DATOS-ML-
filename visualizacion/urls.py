from django.urls import path
from . import views

app_name = 'visualizacion'

urlpatterns = [
    # URL 1: Inicio (raíz)
    path('', views.inicio, name='inicio'),

    # URL 2: Entregas
    path('entregas/', views.analisis_entregas, name='entregas'),

    # URL 3: Regional
    path('regional/', views.analisis_regional, name='regional'),

    # URL 4: Categorías
    path('categorias/', views.categorias_productos, name='categorias'),

    # URL 5: Indicadores
    path('indicadores/', views.otros_indicadores, name='indicadores'),

    # URL 6: Recomendaciones
    path('recomendaciones/', views.recomendaciones, name='recomendaciones'),
]