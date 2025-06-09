from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('listarClientes')),

    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
]
