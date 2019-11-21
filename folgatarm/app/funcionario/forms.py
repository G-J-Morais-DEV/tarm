from django import forms
from django.forms import ModelForm
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome', 'sobrenome','feirista','folguista','plantaoPadrao')

class FuncionarioUpdate(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome', 'sobrenome','feirista','folguista','plantaoPadrao')
