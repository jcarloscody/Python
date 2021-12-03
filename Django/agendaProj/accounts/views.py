from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(req):
    if req.method != 'POST':
        return render(req, 'accounts/login.html')

    usuario  = req.POST.get('usuario')
    senha  = req.POST.get('senha')

    user = auth.authenticate(req, username=usuario, password=senha)

    if not user:
        messages.error(req, "login invalido")
        return render(req, 'accounts/login.html')
    else:
        auth.login(req, user)
        messages.success(req, "sucesso")
        return  redirect('dashboard')



def logout(req):
    auth.logout(req)
    return redirect('login')

def cadastro(req):
    if req.method != 'POST':
        return render(req, 'accounts/cadastro.html')

    nome = req.POST.get('nome')
    sobrenome = req.POST.get('sobrenome')
    email = req.POST.get('email')
    usuario = req.POST.get('usuario')
    senha = req.POST.get('senha')
    senha2 = req.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.add_message(req, messages.ERROR, "nenhum campo pode ficar vazio")
        return render(req, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.add_message(req, messages.ERROR, "email invalido")
        return render(req, 'accounts/cadastro.html')


    if len(senha) < 6:
        messages.add_message(req, messages.ERROR, "senha deve >5")
        return render(req, 'accounts/cadastro.html')

    if senha != senha2:
        messages.add_message(req, messages.ERROR, "senhas nao batem")
        return render(req, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.add_message(req, messages.ERROR, "usuario ja existentes")
        return render(req, 'accounts/cadastro.html')

    messages.add_message(req, messages.SUCCESS, "sucesso")
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(req):
    return render(req, 'accounts/dashboard.html')
