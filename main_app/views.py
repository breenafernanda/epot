from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Aula, Conceito, Metodologia, Exercicio, Formula, Exemplo

def index(request):
    aulas = Aula.objects.all().order_by("titulo")
    conceitos = Conceito.objects.all().order_by("titulo")
    metodologias = Metodologia.objects.all().order_by("item") # Corrigido para 'item'
    exercicios = Exercicio.objects.all().order_by("titulo")
    return render(request, "index.html", {
        "aulas": aulas,
        "conceitos": conceitos,
        "metodologias": metodologias,
        "exercicios": exercicios
    })

def aula_detail(request, aula_id):
    aula = get_object_or_404(Aula, pk=aula_id)
    conceitos_aula = Conceito.objects.filter(aula_relacionada=aula)
    formulas_aula = Formula.objects.filter(aula_relacionada=aula)
    exemplos_aula = Exemplo.objects.filter(aula_relacionada=aula)
    return render(request, "aula_detail.html", {
        "aula": aula,
        "conceitos_aula": conceitos_aula,
        "formulas_aula": formulas_aula,
        "exemplos_aula": exemplos_aula
    })

def test_view(request):
    return HttpResponse("Hello from Django test view!")


