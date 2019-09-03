from django.urls import path

from .views import paginaInicioView

urlpatterns = [
    path('', paginaInicioView, name='inicio')
]