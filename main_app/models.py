from django.db import models

class Aula(models.Model):
    titulo = models.CharField(max_length=200)
    topicos = models.TextField(blank=True, null=True) # Resumo dos tópicos
    conteudo_detalhado = models.TextField(blank=True, null=True) # Conteúdo detalhado da aula
    tempo_video = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.titulo

class Conceito(models.Model):
    titulo = models.CharField(max_length=200)
    definicao = models.TextField()
    aplicacoes = models.TextField(blank=True, null=True)
    tipos = models.TextField(blank=True, null=True)
    explicacao_detalhada = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Metodologia(models.Model):
    item = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.item

class Exercicio(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    solucao = models.TextField(blank=True, null=True)
    aula_relacionada = models.ForeignKey(Aula, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.titulo

class Formula(models.Model):
    nome = models.CharField(max_length=200)
    formula_latex = models.TextField()
    descricao = models.TextField(blank=True, null=True)
    aula_relacionada = models.ForeignKey(Aula, on_delete=models.SET_NULL, blank=True, null=True)
    conceito_relacionado = models.ForeignKey(Conceito, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nome

class Exemplo(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    passos_resolucao = models.TextField(blank=True, null=True)
    aula_relacionada = models.ForeignKey(Aula, on_delete=models.SET_NULL, blank=True, null=True)
    conceito_relacionado = models.ForeignKey(Conceito, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.titulo


