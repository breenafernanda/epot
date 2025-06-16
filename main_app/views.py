from django.shortcuts import render
from .models import Aula, Conceito, Metodologia

def index(request):
    aulas = Aula.objects.all().order_by("id")
    conceitos = Conceito.objects.all().order_by("id")
    metodologias = Metodologia.objects.all().order_by("id")

    context = {
        "aulas": aulas,
        "conceitos": conceitos,
        "metodologias": metodologias,
    }
    return render(request, "index.html", context)


