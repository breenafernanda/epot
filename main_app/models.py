from django.db import models

class Aula(models.Model):
    titulo = models.CharField(max_length=200)
    topicos = models.TextField()
    tempo_video = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.titulo

class Conceito(models.Model):
    titulo = models.CharField(max_length=200)
    definicao = models.TextField()
    aplicacoes = models.TextField(blank=True, null=True)
    tipos = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Metodologia(models.Model):
    item = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.item


