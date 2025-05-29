# app_cadastro/urls.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente

# app_cadastro/views.py
def sucesso(request):
    return HttpResponse("Cadastro realizado com sucesso!")

def cadastro_cliente(request):
    if request.method == 'POSfrom .models import ClienteT':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')

        # Verificar se todos os campos foram preenchidos
        if nome and email and telefone and endereco:
            # Salvar os dados no banco de dados
            cliente = Cliente(nome=nome, email=email, telefone=telefone, endereco=endereco)
            cliente.save()
            return redirect('sucesso')  # Redireciona para uma página de sucesso
        else:
            return HttpResponse("Por favor, preencha todos os campos.", status=400)
    
    return render(request, 'app_cadastro/cadastro.html')

