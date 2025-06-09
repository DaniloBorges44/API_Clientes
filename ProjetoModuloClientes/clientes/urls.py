from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('listarClientes', views.listarClientes, name='listarClientes'),
    path('cadastrarCliente', views.cadastroCliente),
    path('excluirCliente/<int:id>', views.excluirCliente),
    path('editarCliente/<int:id>', views.editarCliente),
]

urlpatterns += router.urls