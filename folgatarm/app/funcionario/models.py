from django.db import models
from multiselectfield import MultiSelectField

class Funcionario(models.Model):
    PLANTAO_CHOICES = [
        ("NDA","Nenhuma das Opções"),
        ("Mad", "Madrugada"),
        ("Man", "Manhã"),
        ("Tar", "Tarde"),
        ("Noi", "Noite"),
    ]
    # FOLFER_CHOICES = [
    #     ("Fei","Feirista"),
    #     ("Fol", "Folguista"),
    # ]

    nome = models.CharField(max_length=255,null=False,blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    plantaoPadrao = MultiSelectField(choices=PLANTAO_CHOICES)
    folguista = models.BooleanField("folguista" , default=False)
    feirista = models.BooleanField("feirista" ,default=False)

    