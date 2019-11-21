from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Coordenador
from .forms import CoordenadorForm
from app.home.views import *
# Create your views here.
@login_required(login_url='login')
def homecoord(request):
    coordenador = Coordenador.objects.get(username=request.user.username)
    if coordenador.is_authenticated:
        return render(request, 'coordenador/inicial.html',{"coordenador":coordenador})
    else:
        return redirect('logout_view')

def loginCoordenador(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        coordenador = None
        try:
            coordenador = Coordenador.objects.get(email=email)
            user = authenticate(request, username=coordenador.username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    msg = "Email ou senha Incorretos!"
                    return redirect('login',{"msg":msg})
            else:
                msg = "Email ou senha Incorretos!"
                return render(request, "coordenador/login.html", {"msg":msg})
        except Exception as e:
            print(e)
            msg = "Email ou senha Incorretos!"
            return render(request, "coordenador/login.html", {"msg":msg})
        else:
            msg = None
            return render(request, "coordenador/login.html", {"mng":msg})

def logout_view(request):
    logout(request)
    return home(request)