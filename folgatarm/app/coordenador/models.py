from django.contrib.auth.models import AbstractUser
from django.db import models

class Coordenador(AbstractUser):
    photo = models.ImageField(upload_to="gerente/",default='gerente/default.jpg',blank=True,null=True)
    email = models.EmailField(primary_key=True, blank=False, null=False, unique=True)

    def __str__(self):
        return self.username
