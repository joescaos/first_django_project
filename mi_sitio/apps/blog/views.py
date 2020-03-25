# para poder llamar las vistas
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrarForm
from django.contrib.auth.models import User

# Create your views here.


def index(request):  # siempre se asigna request
    return render(request, 'index.html', {

    })


def ingresar(request):  # siempre se asigna request

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)

            messages.success(request, 'Bienvenido {}'.format(user.username))

            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrecta')

    return render(request, 'login.html', {
    })


def salir(request):
    logout(request)
    messages.success(request, 'Sesión finalizada correctamente')
    return redirect('ingresar')


def registrar(request):
    form = RegistrarForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():

        user = form.GuardarUsuarios()
        '''
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        
        user = User.objects.create_user(username, email, password)
        '''
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'registrar.html', {
        'form': form

    })
