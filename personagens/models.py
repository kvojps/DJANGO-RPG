from django.db import models

class Member(models.Model):
    nome = models.CharField(max_length=50)
    nivel = models.IntegerField()
    raca = models.CharField(max_length=50)
    vida = models.IntegerField()
    mana = models.IntegerField()
    poder = models.CharField(max_length=50)
    dificuldade = models.IntegerField()

    def __str__(self):
        return self.nome

