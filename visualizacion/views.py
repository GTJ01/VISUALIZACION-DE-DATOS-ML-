from django.shortcuts import render
import json
import os
from django.conf import settings

# Cargar datos de la encuesta
def cargar_datos():
    """Función auxiliar para cargar los datos JSON"""
    json_path = os.path.join(settings.BASE_DIR, 'datos_encuesta_ml_nuevo.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Vista 1: Inicio - Dashboard principal
def inicio(request):
    """Vista principal que muestra el dashboard con el resumen ejecutivo"""
    datos = cargar_datos()
    context = {
        'titulo': 'Análisis de Calidad - Mercado Libre',
        'problema': datos['problema_principal'],
        'estadisticas': datos['estadisticas_clave'],
        'satisfaccion': datos['satisfaccion_distribucion'],
    }
    return render(request, 'visualizacion/inicio.html', context)

# Vista 2: Análisis de Entregas
def analisis_entregas(request):
    """Vista detallada del problema de logística y entregas"""
    datos = cargar_datos()

    context = {
        'titulo': 'Análisis de Entregas y Logística',
        'entregas_json': json.dumps(datos['cumplimiento_entregas']),
        'frecuencia_json': json.dumps(datos['frecuencia_compra']),
        'estadisticas': datos['estadisticas_clave'],
    }
    return render(request, 'visualizacion/entregas.html', context)

# Vista 3: Análisis Regional
def analisis_regional(request):
    """Vista con análisis por regiones de Chile"""
    datos = cargar_datos()

    # Ordenar regiones por porcentaje
    regiones_ordenadas = sorted(
        datos['regiones'], 
        key=lambda x: x['porcentaje'], 
        reverse=True
    )

    context = {
        'titulo': 'Análisis Regional',
        'regiones': regiones_ordenadas,
        'total_compradores': datos['estadisticas_clave']['total_compradores'],
    }
    return render(request, 'visualizacion/regional.html', context)

# Vista 4: Categorías y Productos
def categorias_productos(request):
    """Vista de análisis de categorías más compradas"""
    datos = cargar_datos()

    context = {
        'titulo': 'Categorías y Productos',
        'categorias_json': json.dumps(datos['categorias_favoritas']),
        'total_compradores': datos['estadisticas_clave']['total_compradores'],
    }
    return render(request, 'visualizacion/categorias.html', context)

# Vista 5: Otros Indicadores
def otros_indicadores(request):
    """Vista con precios, descripciones y métodos de pago"""
    datos = cargar_datos()

    context = {
        'titulo': 'Otros Indicadores de Calidad',
        'descripciones_json': json.dumps(datos['descripciones_claras']),
        'precios_json': json.dumps(datos['precios_competitivos']),
        'metodos_json': json.dumps(datos['metodos_pago']),
        'proceso_json': json.dumps(datos['proceso_rapido']),
        'variedad_json': json.dumps(datos['variedad_satisfactoria']),
        'genero_json': json.dumps(datos['genero_distribucion']),
        'satisfaccion_json': json.dumps(datos['satisfaccion_distribucion']),
        'estadisticas': datos['estadisticas_clave'],
    }
    return render(request, 'visualizacion/indicadores.html', context)

# Vista 6: Recomendaciones
def recomendaciones(request):
    """Vista con recomendaciones y soluciones propuestas"""
    datos = cargar_datos()

    context = {
        'titulo': 'Recomendaciones y Soluciones',
        'estadisticas': datos['estadisticas_clave'],
    }
    return render(request, 'visualizacion/recomendaciones.html', context)
