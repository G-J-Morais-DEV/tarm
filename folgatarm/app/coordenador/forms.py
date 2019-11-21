from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Coordenador

class CoordenadorForm(UserCreationForm):
      photo = forms.ImageField(required=False)
      class Meta(UserCreationForm):
          model = Coordenador
          fields = ('username','email',)