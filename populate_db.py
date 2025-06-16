import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "epot_project.settings")
django.setup()

from main_app.models import Aula, Conceito, Metodologia

def populate_data():
    # Limpar dados existentes
    Aula.objects.all().delete()
    Conceito.objects.all().delete()
    Metodologia.objects.all().delete()

    # Aulas
    aulas_data = [
        {"titulo": "Introdução à Eletrônica de Potência", "topicos": "Definição, Aplicações, Elementos básicos", "tempo_video": "20:27"},
        {"titulo": "Diodos de Potência", "topicos": "Características, Tipos, Aplicações", "tempo_video": "30:15"},
        {"titulo": "Dispositivos Tiristores", "topicos": "SCR, TRIAC, DIAC", "tempo_video": "36:55"},
        {"titulo": "Transistores de Potência", "topicos": "BJT, MOSFET, IGBT", "tempo_video": "23:04"},
        {"titulo": "Retificador Monofásico - Meia Onda - Carga R", "topicos": "Análise, Cálculos, Formas de onda", "tempo_video": "17:21"},
        {"titulo": "Retificador Monofásico - Meia Onda - Carga RL", "topicos": "Modo contínuo, Modo descontínuo", "tempo_video": "27:12"},
        {"titulo": "Retificador Monofásico - Meia Onda - Carga RL + Diodo de Roda Livre", "topicos": "Diodo de roda livre, Análise", "tempo_video": "18:02"},
        {"titulo": "Retificador Monofásico - Meia Onda - Carga RLE", "topicos": "Fonte CC, Análise completa", "tempo_video": "26:18"},
        {"titulo": "Retificador Monofásico - Onda Completa - Carga R", "topicos": "Ponte de diodos, Centro derivado", "tempo_video": "25:29"},
        {"titulo": "Retificador Monofásico - Onda Completa - Carga RL", "topicos": "Análise harmônica, Cálculos", "tempo_video": "20:46"},
        {"titulo": "Retificador Monofásico - Onda Completa - Carga RLE", "topicos": "Modo contínuo, Potência", "tempo_video": None},
        {"titulo": "Projeto de Filtros de Saída", "topicos": "Filtro capacitivo, Filtro LC", "tempo_video": None},
        {"titulo": "Retificador Trifásico - Três Pulsos", "topicos": "Análise, Vantagens", "tempo_video": None},
        {"titulo": "Retificador Trifásico - Seis Pulsos", "topicos": "Ponte trifásica, Cálculos", "tempo_video": None},
        {"titulo": "Retificador Trifásico - Seis Pulsos com Transformadores", "topicos": "Δ-Y, Y-Δ", "tempo_video": None},
    ]
    for aula_data in aulas_data:
        Aula.objects.create(**aula_data)

    # Conceitos
    conceitos_data = [
        {"titulo": "Eletrônica de Potência", "definicao": "Trata da aplicação de dispositivos semicondutores de potência na conversão e no controle da energia elétrica em níveis altos de potência.", "aplicacoes": "Fontes de alimentação, Controle de motores, Sistemas de energia renovável", "tipos": None},
        {"titulo": "Retificadores", "definicao": "Circuitos que convertem tensão CA em tensão CC utilizando diodos ou outros dispositivos semicondutores.", "aplicacoes": None, "tipos": "Meia onda, Onda completa, Monofásicos, Trifásicos"},
        {"titulo": "Dispositivos Semicondutores", "definicao": "Componentes eletrônicos que controlam o fluxo de corrente elétrica.", "aplicacoes": None, "tipos": "Diodos, Tiristores (SCR, TRIAC), Transistores (BJT, MOSFET, IGBT)"},
    ]
    for conceito_data in conceitos_data:
        Conceito.objects.create(**conceito_data)

    # Metodologia
    metodologia_data = [
        {"item": "Teoria Sólida", "descricao": "Fundamentação teórica completa antes da prática"},
        {"item": "Exemplos Práticos", "descricao": "Resolução detalhada de exercícios passo a passo"},
        {"item": "Aplicações Reais", "descricao": "Conexão com aplicações industriais e comerciais"},
    ]
    for metodologia_item in metodologia_data:
        Metodologia.objects.create(**metodologia_item)

    print("Dados populados com sucesso!")

if __name__ == "__main__":
    populate_data()


