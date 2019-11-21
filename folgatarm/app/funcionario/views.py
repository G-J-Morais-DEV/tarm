from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,permission_required
from app.coordenador.models import Coordenador
from .forms import FuncionarioForm, FuncionarioUpdate
from .models import Funcionario

from datetime import datetime
from pytz import timezone
from datetime import date

# Create your views here.
@login_required(login_url='login')
def cad_func(request):
    coordenador = Coordenador.objects.get(username=request.user.username)
    
    if request.method == 'POST' and coordenador.is_authenticated:
        func_campos = FuncionarioForm(request.POST)
        print(func_campos.errors)
        if func_campos.is_valid():
            func_campos.save(commit=False)
            funcionario = Funcionario()
            funcionario.nome = func_campos.cleaned_data['nome']
            funcionario.sobrenome = func_campos.cleaned_data['sobrenome']
            funcionario.folguista = func_campos.cleaned_data['folguista']
            funcionario.feirista = func_campos.cleaned_data['feirista']
            funcionario.plantaoPadrao = func_campos.cleaned_data['plantaoPadrao']
            funcionario.save()
            return render(request, 'funcionario/cad_func.html')
            
        else:
            return render(request, 'funcionario/cad_func.html')
    else:
        if coordenador.is_authenticated:
            return render(request, "funcionario/cad_func.html")
        else:
            return redirect('logout_view')

#lista dos funcionarios cadastrados
@login_required(login_url='login')
def listar_func(request):
    funcionarios = Funcionario.objects.all()
    coordenador = Coordenador.objects.get(username=request.user.username)
    if coordenador.is_authenticated:
        return render(request, "funcionario/lista_func.html",{"funcionarios":funcionarios})
    else:
        return redirect('logout_view')

#apagar funcionario
@login_required(login_url='login')
def apagar_func(request, nome):
    funcionarios = Funcionario.objects.filter(nome=nome)
    funcionarios.delete()
    coordenador = Coordenador.objects.get(username=request.user.username)
    if coordenador.is_authenticated:
        return render(request, "funcionario/lista_func.html",{"funcionarios":funcionarios})
    else:
        return redirect('logout_view')

#atualizar cadastro do funcionario
@login_required(login_url='login')
def update_func(request, id):
    funcionarios = Funcionario.objects.filter(id=id)
    #nome = Funcionario.objects.get(nome=nome)
    coordenador = Coordenador.objects.get(username=request.user.username)
    #form = FuncionarioForm()
    if request.method == 'POST' and coordenador.is_authenticated:
        update = FuncionarioUpdate(request.POST, request.FILES)
        if update.is_valid():
            funcionario = Funcionario()
            funcionario.nome = update.cleaned_data['nome']
            funcionario.sobrenome = update.cleaned_data['sobrenome']
            funcionario.folguista = update.cleaned_data['folguista']
            funcionario.feirista = update.cleaned_data['feirista']
            funcionario.plantaoPadrao = update.cleaned_data['plantaoPadrao']
            funcionario.save()
            return redirect('lista_func')
        else:
            return render(redirect, "funcionario/update_func.html",{"funcionarios":funcionarios})
    else:
        if coordenador.is_authenticated:
            return render(request,"funcionario/update_func.html",{"funcionarios":funcionarios})
        else:
            return redirect('logout_view')

#escala dos Tarms
@login_required(login_url='login')
def escala_func(request):
    #Achando a data de hoje
    timeDate = datetime.now()
    fuso = timezone('America/Sao_Paulo')
    realTime = timeDate.astimezone(fuso)
    realDate = realTime.strftime('%d/%m/%Y')
    realTime = realTime.strftime('%H:%M:%S')
    #pegando o mes/dia da semana 
    month = timeDate.month
    weekDay = timeDate.weekday()
    days_of_Month = [31,28,31,30,31,30,31,31,30,31,30,31]
    daysTotal = days_of_Month[month-1]
    dayNamesMin = ['S', 'T', 'Q', 'Q', 'S', 'S','D']
    #criar lista para setar a quantidade de dias que há no mes 
    completeMonth = []
    for i in range(1 ,(daysTotal+1)):
        completeMonth.append(i)

    #criar a lista para os dias da semana
    completeWeek = []
    x = 1 
    firsDayMonth = date(year=2019, month=month, day=1)
    y = datetime.weekday(firsDayMonth)
    print(y)
    # listas de folgas
    day_off_Mad = []
    day_off_Man = []
    day_off_Tar = []
    day_off_Noi = []
    day_off = 0
    while x < (len(completeMonth)+1):
        x+=1
        day_off+=1
        completeWeek.append(dayNamesMin[y])
        day_off_Mad.append("A")
        day_off_Man.append("B")
        day_off_Tar.append("C")
        day_off_Noi.append("D")
        y+=1
        if y == 7:
            y = 0
        if day_off == 6:
            day_off_Mad[-1] = "E"
        if day_off == 7:
            day_off_Man[0] = "E"
            day_off_Man[-1] = "E"
        if day_off == 8:
            day_off_Tar[1] = "E"
            day_off_Tar[-1] = "E"
        if day_off == 9:
            day_off_Noi[2] = "E"
            day_off_Noi[-1] = "E"
            day_off = 3
    # renderizando a pagina 
    funcionarios = Funcionario.objects.all()
    coordenador = Coordenador.objects.get(username=request.user.username)
    if coordenador.is_authenticated:
        return render(request, "funcionario/escala_func.html",{"funcionarios":funcionarios,"daysTotal":daysTotal,"completeMonth":completeMonth,"realTime":realTime,"weekDay":weekDay,"dayNamesMin":dayNamesMin,"completeWeek":completeWeek,"day_off_Mad":day_off_Mad,"day_off_Man":day_off_Man,"day_off_Tar":day_off_Tar,"day_off_Noi":day_off_Noi})
    else:
        return redirect('logout_view')

