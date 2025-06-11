from django.shortcuts import render, get_object_or_404
from .models import Cliente
from datetime import datetime
from django.http import HttpResponseRedirect

from .serializers import ClienteSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import login_required

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.

@login_required
def listarClientes(request):
    
    clientes = Cliente.objects.all()

    return render(request, "listarClientes.html", {"clientes" : clientes})

@login_required
def cadastroCliente(request):
    
    if(request.method == "POST"):
        nome = request.POST.get('nome')
        email = request.POST.get('email')        
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        sexo = request.POST.get('sexo')
        data_nasc = request.POST.get('data_nasc')

        novo_cliente = Cliente(nome=nome, email=email, telefone=telefone, cpf=cpf, sexo = sexo, data_nasc = data_nasc)
        novo_cliente.save()

        return HttpResponseRedirect('/clientes/listarClientes')
    
    return render(request, "cadastroCliente.html")

@login_required
def excluirCliente(request, id):

    cliente = Cliente.objects.get(id=id)
    cliente.delete()

    return HttpResponseRedirect('/clientes/listarClientes')

@login_required
def editarCliente(request, id):

    cliente = Cliente.objects.get(id=id)
    
    if(request.method == 'POST'):
        cliente.nome = request.POST.get('nome')
        cliente.email = request.POST.get('email')
        cliente.telefone = request.POST.get('telefone')
        cliente.cpf = request.POST.get('cpf')
        cliente.sexo = request.POST.get('sexo')
        cliente.data_nasc = request.POST.get('data_nasc')
        cliente.save()
        return HttpResponseRedirect('/clientes/listarClientes')

    return render(request, 'editarCliente.html', {'cliente': cliente})