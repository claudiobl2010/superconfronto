from django.db import models

class Game(models.Model):
    rodada = models.IntegerField()
    status = models.IntegerField()
    fechamento = models.DateTimeField()
    atualizacao = models.DateTimeField()

class Liga(models.Model):
    qtd = models.IntegerField()

class LigaTime(models.Model):
    posicao = models.IntegerField()
    rodada = models.IntegerField()
    pontos_rod = models.FloatField()
    time_id = models.IntegerField()
    nome_time = models.CharField(max_length=40)
    slug_time = models.CharField(max_length=40)
    nome_cartola = models.CharField(max_length=40)
    img_escudo_time_peq = models.CharField(max_length=200)
    img_escudo_time_gde = models.CharField(max_length=200)
