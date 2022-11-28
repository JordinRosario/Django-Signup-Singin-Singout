from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    return render(request,'home.html')

def crear_usuario(request):
    if request.method == 'GET':
        return render(request, 'crear_usuario.html', {
            'crear_usuario_form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:    
                print(request.POST)
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except:
                return render(request, 'crear_usuario.html', {
            'crear_usuario_form': UserCreationForm,
            'error':'El usuario ya esta creado'
        })
        else:
            return render(request, 'crear_usuario.html', {
            'crear_usuario_form': UserCreationForm,
            'error':'Las contrasenias no coinsiden'
        })
            
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request,'iniciar_sesion.html',{
            'iniciar_sesion_form': AuthenticationForm,
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'iniciar_sesion.html',{
            'iniciar_sesion_form': AuthenticationForm,
            'error':'usuario no encontrado o contrasenia incorrecta'
        })
        else:
            login(request,user)
            return redirect('home')
    