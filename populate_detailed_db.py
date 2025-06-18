import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "epot_project.settings")
django.setup()

from main_app.models import Aula, Conceito, Metodologia, Exercicio, Formula, Exemplo

def populate_aula_1a():
    # Aula 1(a) - Introdução à Eletrônica de Potência
    aula_1a_content = """
Eletrônica de Potência I
INTRODUÇÃO À
ELETRÔNICA DE POTÊNCIA

AULA 1
Prof. Danillo Borges Rodrigues


O Q U E É A E L E T R Ô N I C A D E P OT Ê N C I A?

• Eletrônica de Potência trata da aplicação de dispositivos
semicondutores de potência na conversão e no controle
da energia elétrica em níveis altos de potência.
• A Eletrônica de Potência é basicamente utilizada para
adequar os níveis de tensão\corrente disponível na
entrada e aquela requerida pelas cargas.


O Q U E É U M C O N V E R S O R D E P OT Ê N C I A

Um CONVERSOR é um módulo básico de um sistema
eletrônico
de
potência
que
utiliza
elementos
armazenadores
de
energia
e
dispositivos
semicondutores de potência controlados por um
circuito de controle utilizado para manipular grandezas
elétricas (tensão, corrente e frequência).


E L E MENTOS DI SP ONÍ V E IS PAR A O P ROJ E T I STA.

Processamento de potência (kW ou MW)
Evitar elementos dissipativos


E XE MP LO – FONT E DE AL I ME NTAÇÃO DE COMP UTADOR E S

Retificador + Chopper CC


E XE MPLO – FONT E DE AL I ME NTAÇÃO DE CE L ULAR ES
Chopper CC


E XE MPLO – CONT ROL E DE MÁQUI NAS ROTAT I VAS
Controlador de tensão CA
ou
Retificador + Inversor


AP LI C AÇ Õ E S DA E L E T R Ô N I C A D E P OT Ê N C I A

• RESIDENCIAL
• Refrigeradores e freezers;
• Ar-condicionado;
• Aquecedores;
• Iluminação;
• Eletrônicos (computadores e celulares).


AP LI C AÇ Õ E S DA E L E T R Ô N I C A D E P OT Ê N C I A

• COMERCIAL
• Aquecimento, ventilação e ar condicionado;
• Centrais de refrigeração;
• Iluminação;
• Computadores e equipamentos de escritório;
• Sistemas de alimentação ininterrupta (UPS);
• Elevadores.


AP LI C AÇ Õ E S DA E L E T R Ô N I C A D E P OT Ê N C I A

• INDUSTRIAL
• Bombas;
• Compressores;
• Robôs;
• Fornos a arco e fornos de indução;
• Máquina de solda.


AP LI C AÇ Õ E S DA E L E T R Ô N I C A D E P OT Ê N C I A

• TRANSPORTES
• Controle de tração de veículos elétricos;
• Corregadores de baterias para veículos elétricos;
• Locomotivas elétricas;
• Ônibus elétrico.


AP LI C AÇ Õ E S DA E L E T R Ô N I C A D E P OT Ê N C I A

• SISTEMAS UTILITÁRIOS
• HVDC;
• Compensadores estáticos;
• Fontes renováveis de energia:
(eólica, fotovoltaica; células a combustível);
• Sistemas de armazenamento de energia.


AP LI C AÇ Õ E S DA E L E T R Ô N I C A D E P OT Ê N C I A

• AEROESPACIAL
• Sistema de alimentação de ônibus espaciais;
• Sistema de alimentação de satélites;
• Sistema de alimentação de aviões.


E L E MENTOS DA E L E T RÔNI C A DE P OT Ê NCI A

• Dispositivos de processamento de energia:
Capacitores
Dispositivos Semicondutores
(Diodos,Tiristores, Mosfets, IGBTs, etc.)
Indutores e Transformadores


E L E MENTOS DA E L E T RÔNI C A DE P OT Ê NCI A

• Dispositivos de proteção:
Dissipador de Calor
Ventilador
Circuito Snubber
Varistor
Fusíveis


E L E MENTOS DA E L E T RÔNI C A DE P OT Ê NCI A

• Dispositivos de instrumentação:
Sensor de
Corrente
Efeito Hall
Sensor de
Tensão
Efeito Hall
Placa de Aquisição de Sinais


E L E MENTOS DA E L E T RÔNI C A DE P OT Ê NCI A

• Dispositivos de comando e controle:
DSP (Digital signal processor)
Gate driver


SI MUL AÇÃO COMP UTACI ONAL

• Principais softwares de simulação computacional:
• PSIM
• Proteus
• Matlab / Simulink
• Solidworks
    """

    aula, created = Aula.objects.get_or_create(
        titulo="Aula 1(a) - Introdução à Eletrônica de Potência",
        defaults={
            "topicos": "Definição de Eletrônica de Potência, Conversores de Potência, Elementos para o Projetista, Exemplos de Aplicações (Fontes de Alimentação, Controle de Máquinas Rotativas), Aplicações Residenciais, Comerciais, Industriais, Transportes, Sistemas Utilitários, Aeroespacial, Elementos da Eletrônica de Potência (Processamento, Proteção, Instrumentação, Comando e Controle), Softwares de Simulação Computacional.",
            "conteudo_detalhado": aula_1a_content
        }
    )

    # Conceitos da Aula 1(a)
    Conceito.objects.get_or_create(
        titulo="Eletrônica de Potência",
        defaults={
            "definicao": "Trata da aplicação de dispositivos semicondutores de potência na conversão e no controle da energia elétrica em níveis altos de potência. Basicamente utilizada para adequar os níveis de tensão/corrente disponível na entrada e aquela requerida pelas cargas.",
            "aplicacoes": "Residencial, Comercial, Industrial, Transportes, Sistemas Utilitários, Aeroespacial.",
            "explicacao_detalhada": "A Eletrônica de Potência é um campo da engenharia elétrica que lida com a conversão e o controle de energia elétrica usando dispositivos semicondutores de potência. Seu principal objetivo é adaptar a energia elétrica de uma fonte para as necessidades de uma carga, otimizando a eficiência e o controle. Isso envolve a transformação de diferentes formas de energia elétrica (CA para CC, CC para CA, CC para CC, CA para CA) e o gerenciamento de altos níveis de potência."
        }
    )

    Conceito.objects.get_or_create(
        titulo="Conversor de Potência",
        defaults={
            "definicao": "Módulo básico de um sistema eletrônico de potência que utiliza elementos armazenadores de energia e dispositivos semicondutores de potência controlados por um circuito de controle para manipular grandezas elétricas (tensão, corrente e frequência).",
            "tipos": "CC-CC (Chopper), CC-CA (Inversor), CA-CC (Retificador), Controlador de Tensão CA.",
            "explicacao_detalhada": "Conversores de potência são o coração dos sistemas de eletrônica de potência. Eles são responsáveis por transformar a energia elétrica de uma forma para outra, por exemplo, de corrente alternada para corrente contínua (retificador) ou vice-versa (inversor). Utilizam dispositivos semicondutores como diodos, tiristores e transistores para chavear a energia de forma eficiente, minimizando perdas e permitindo o controle preciso das grandezas elétricas."
        }
    )

    Conceito.objects.get_or_create(
        titulo="Dispositivos Semicondutores de Potência",
        defaults={
            "definicao": "Componentes eletrônicos que permitem o controle da energia elétrica através de chaveamento. Exemplos incluem Diodos, Tiristores, MOSFETs, IGBTs.",
            "explicacao_detalhada": "São os elementos ativos que permitem o controle da energia em sistemas de eletrônica de potência. Ao contrário dos dispositivos de sinal, são projetados para operar com altas tensões e correntes. Sua capacidade de chavear rapidamente entre estados de condução e bloqueio é fundamental para a eficiência dos conversores de potência."
        }
    )

    Conceito.objects.get_or_create(
        titulo="Elementos de Proteção (Eletrônica de Potência)",
        defaults={
            "definicao": "Componentes utilizados para proteger os circuitos e dispositivos de potência contra condições anormais de operação, como sobrecorrente, sobretensão e superaquecimento.",
            "tipos": "Dissipador de Calor, Ventilador, Circuito Snubber, Varistor, Fusíveis.",
            "explicacao_detalhada": "A proteção é crucial em eletrônica de potência devido aos altos níveis de energia envolvidos. Dissipadores de calor e ventiladores gerenciam a temperatura, enquanto fusíveis e varistores protegem contra picos de corrente e tensão. Circuitos snubber são usados para limitar as taxas de variação de tensão e corrente durante o chaveamento, protegendo os semicondutores."
        }
    )

    Conceito.objects.get_or_create(
        titulo="Softwares de Simulação Computacional (Eletrônica de Potência)",
        defaults={
            "definicao": "Ferramentas de software utilizadas para modelar, simular e analisar o comportamento de circuitos e sistemas de eletrônica de potência antes da implementação física.",
            "tipos": "PSIM, Proteus, Matlab/Simulink, Solidworks.",
            "explicacao_detalhada": "A simulação computacional é uma etapa essencial no projeto de sistemas de eletrônica de potência. Ela permite aos engenheiros testar diferentes configurações de circuito, analisar o desempenho sob várias condições de operação e identificar potenciais problemas sem a necessidade de construir protótipos físicos, economizando tempo e recursos. Ferramentas como PSIM e Simulink são amplamente utilizadas para simular o comportamento de conversores e seus componentes."
        }
    )

def populate_aula_1b():
    # Aula 1(b) - Cálculos de Potência
    aula_1b_content = """
Eletrônica de Potência I
CÁLCULOS DE POTÊNCIA

AULA 1
Prof. Danillo Borges Rodrigues


POTÊNCIA EM CIRCUITOS CA

• A potência instantânea é o produto da tensão instantânea pela corrente instantânea:
p(t) = v(t) ⋅ i(t)


POTÊNCIA EM CIRCUITOS CA

• Potência média ou ativa (P):

• É a potência real consumida pela carga.
• É a potência que realiza trabalho útil.
• Unidade: Watt (W).


POTÊNCIA EM CIRCUITOS CA

• Potência reativa (Q):

• É a potência que flui e reflui entre a fonte e a carga.
• Não realiza trabalho útil.
• Unidade: Volt-Ampere Reativo (VAR).


POTÊNCIA EM CIRCUITOS CA

• Potência aparente (S):

• É a potência total fornecida pela fonte.
• É a soma vetorial da potência ativa e da potência reativa.
• Unidade: Volt-Ampere (VA).


FATOR DE POTÊNCIA (FP)

• É a relação entre a potência ativa e a potência aparente.
• Indica a eficiência com que a energia elétrica é convertida em trabalho útil.
• FP = P / S


DISTORÇÃO HARMÔNICA TOTAL (DHT)

• É uma medida da distorção de uma forma de onda em relação a uma senóide pura.
• É a relação entre o valor eficaz de todas as harmônicas e o valor eficaz da fundamental.


EXEMPLO DE CÁLCULO DE POTÊNCIA

Um circuito tem tensão v(t) = 100sen(ωt) e corrente i(t) = 10sen(ωt - 30°).
Calcule a potência ativa, reativa e aparente, e o fator de potência.

Solução:
Vm = 100 V, Im = 10 A, θ = 30°

P = (Vm * Im / 2) * cos(θ) = (100 * 10 / 2) * cos(30°) = 500 * 0.866 = 433 W
Q = (Vm * Im / 2) * sen(θ) = (100 * 10 / 2) * sen(30°) = 500 * 0.5 = 250 VAR
S = Vm * Im / 2 = 100 * 10 / 2 = 500 VA
FP = P / S = 433 / 500 = 0.866
    """

    aula, created = Aula.objects.get_or_create(
        titulo="Aula 1(b) - Cálculos de Potência",
        defaults={
            "topicos": "Potência Instantânea, Potência Média (Ativa), Potência Reativa, Potência Aparente, Fator de Potência (FP), Distorção Harmônica Total (DHT), Exemplo de Cálculo de Potência.",
            "conteudo_detalhado": aula_1b_content
        }
    )

    # Conceitos da Aula 1(b)
    Conceito.objects.get_or_create(
        titulo="Potência Instantânea",
        defaults={
            "definicao": "Produto da tensão instantânea pela corrente instantânea (p(t) = v(t) ⋅ i(t)).",
            "explicacao_detalhada": "A potência instantânea representa a potência em um determinado momento no tempo. É o produto direto dos valores instantâneos de tensão e corrente. Em circuitos CA, a potência instantânea pode variar significativamente ao longo de um ciclo, e seu valor médio ao longo de um período é a potência ativa."
        }
    )

    Conceito.objects.get_or_create(
        titulo="Potência Média (Ativa)",
        defaults={
            "definicao": "Potência real consumida pela carga que realiza trabalho útil. Medida em Watts (W).",
            "explicacao_detalhada": "A potência média, também conhecida como potência ativa, é a parte da potência que é efetivamente convertida em trabalho útil (por exemplo, calor, luz, movimento). É o valor médio da potência instantânea ao longo de um ciclo completo. Em circuitos CA, é calculada como P = Vrms * Irms * cos(phi), onde phi é o ângulo de fase entre tensão e corrente."
        }
    )

    Conceito.objects.get_or_create(
        titulo="Potência Reativa",
        defaults={
            "definicao": "Potência que flui e reflui entre a fonte e a carga, não realizando trabalho útil. Medida em Volt-Ampere Reativo (VAR).",
            "explicacao_detalhada": "A potência reativa é a potência que oscila entre a fonte e a carga, sendo armazenada e liberada por componentes reativos (indutores e capacitores). Ela não realiza trabalho útil, mas é necessária para estabelecer campos magnéticos em indutores e campos elétricos em capacitores. É calculada como Q = Vrms * Irms * sen(phi)."
        }
    )

    Conceito.objects.get_or_create(
        titulo="Potência Aparente",
        defaults={
            "definicao": "Potência total fornecida pela fonte, sendo a soma vetorial da potência ativa e da potência reativa. Medida em Volt-Ampere (VA).",
            "explicacao_detalhada": "A potência aparente é a potência total que a fonte de energia fornece ao circuito. É a combinação vetorial da potência ativa e da potência reativa. Representa a capacidade total de entrega de energia de um sistema e é calculada como S = Vrms * Irms ou S = sqrt(P^2 + Q^2)."
        }
    )

    Conceito.objects.get_or_create(
        titulo="Fator de Potência (FP)",
        defaults={
            "definicao": "Relação entre a potência ativa e a potência aparente (FP = P / S). Indica a eficiência com que a energia elétrica é convertida em trabalho útil.",
            "explicacao_detalhada": "O fator de potência é um indicador da eficiência do uso da energia elétrica. Um fator de potência próximo de 1 (ou 100%) indica que a maior parte da potência aparente está sendo convertida em trabalho útil (potência ativa), enquanto um fator de potência baixo indica uma grande quantidade de potência reativa, o que pode levar a perdas e ineficiências no sistema."
        }
    )

    Conceito.objects.get_or_create(
        titulo="Distorção Harmônica Total (DHT)",
        defaults={
            "definicao": "Medida da distorção de uma forma de onda em relação a uma senóide pura. Relação entre o valor eficaz de todas as harmônicas e o valor eficaz da fundamental.",
            "explicacao_detalhada": "A Distorção Harmônica Total (DHT) quantifica o quanto uma forma de onda (tensão ou corrente) se desvia de uma senóide pura devido à presença de harmônicas. Harmônicas são múltiplos da frequência fundamental e são geradas por cargas não lineares, como conversores de potência. Uma alta DHT pode causar problemas como superaquecimento de equipamentos, mau funcionamento de dispositivos e perdas na rede elétrica."
        }
    )

    # Fórmulas da Aula 1(b)
    Formula.objects.get_or_create(
        nome="Potência Instantânea",
        formula_latex="p(t) = v(t) \cdot i(t)",
        descricao="Potência instantânea em um circuito, produto da tensão instantânea pela corrente instantânea.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Potência Ativa (CA)",
        formula_latex="P = \frac{V_m I_m}{2} \cos(\theta)",
        descricao="Potência ativa em um circuito CA, onde Vm é a tensão de pico, Im é a corrente de pico e theta é o ângulo de fase.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Potência Reativa (CA)",
        formula_latex="Q = \frac{V_m I_m}{2} \sin(\theta)",
        descricao="Potência reativa em um circuito CA, onde Vm é a tensão de pico, Im é a corrente de pico e theta é o ângulo de fase.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Potência Aparente (CA)",
        formula_latex="S = \frac{V_m I_m}{2}",
        descricao="Potência aparente em um circuito CA, onde Vm é a tensão de pico e Im é a corrente de pico.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Fator de Potência",
        formula_latex="FP = \frac{P}{S}",
        descricao="Fator de potência, relação entre a potência ativa e a potência aparente.",
        aula_relacionada=aula
    )

    # Exemplo da Aula 1(b)
    Exemplo.objects.get_or_create(
        titulo="Cálculo de Potência em Circuito CA",
        descricao="Um circuito tem tensão v(t) = 100sen(ωt) e corrente i(t) = 10sen(ωt - 30°). Calcule a potência ativa, reativa e aparente, e o fator de potência.",
        passos_resolucao="""
1. Identificar os valores de pico de tensão (Vm) e corrente (Im), e o ângulo de fase (θ).
   Vm = 100 V, Im = 10 A, θ = 30°
2. Calcular a Potência Ativa (P):
   P = (Vm * Im / 2) * cos(θ) = (100 * 10 / 2) * cos(30°) = 500 * 0.866 = 433 W
3. Calcular a Potência Reativa (Q):
   Q = (Vm * Im / 2) * sen(θ) = (100 * 10 / 2) * sen(30°) = 500 * 0.5 = 250 VAR
4. Calcular a Potência Aparente (S):
   S = Vm * Im / 2 = 100 * 10 / 2 = 500 VA
5. Calcular o Fator de Potência (FP):
   FP = P / S = 433 / 500 = 0.866
        """,
        aula_relacionada=aula
    )

def populate_aula_2():
    # Aula 2 - Chaves Semicondutoras - Diodos de Potência
    aula_2_content = """
Eletrônica de Potência I

CHAVES SEMICONDUTORAS

AULA 2
Diodos de Potência
Prof. Danillo Borges Rodrigues


DI ODO

• São utilizados principalmente em retificadores nãocontrolados e como diodos de retorno;
• Os materiais utilizados na fabricação de diodos podem
ser o silício e o germânio;
• O diodo tem dois terminais: um terminal ânodo A (na
junção P) e um terminal cátodo K (na junção N).


DI ODO DE P OT Ê NCI A

• O diodo de potência é bastante similar ao diodo de sinal
tradicional;
• A diferença física é a inclusão de uma camada de
dopagem adicional (N-), chamada de região de arrasto.


CURVA C AR ACT E R Í ST IC A DOS DI ODOS


MODE L OS D E D I OD O D E P OT Ê NC I A

• Existem basicamente 4 modelos de curvas características
para diodos de potência:
o Diodo Ideal;
o Diodo com Vd;
o Diodo com Vd e Rd;
o Diodo Real.

• Vd é a queda de
tensão direta;
• Rd é a resistência
interna do diodo.

• Com exceção do modelo real, nos demais não são
considerados a corrente de fuga.


MODE L OS D E D I OD O D E P OT Ê NC I A

• Diodo Ideal
• Considera o diodo sem corrente de fuga e sem queda
de tensão.


MODE L OS D E D I OD O D E P OT Ê NC I A

• Diodo com Vd
• Considera o diodo sem corrente de fuga e com queda
de tensão constante (Vd)


MODE L OS D E D I OD O D E P OT Ê NC I A

• Diodo com Vd e Rd
• Considera o diodo sem corrente de fuga e com queda
de tensão linear.


MODE LOS DE DIODO DE POTÊ NC I A

• Diodo Real
• Curva do diodo real, destacando a correntes direta, de
fuga e de avalanche.
v é a tensão do diodo (V).
IS é a corrente de saturação reversa (A);
η é o fator de idealidade do diodo;
T é a temperatura (K);
q = 1,6021895×10-19 C é a carga elementar;
kb = 1,380664×10-23 J/K é a constante de Boltzmann.


R E SUMO DE MODE L OS DE DI ODOS

• Para aplicações em eletrônica de potência:


PR I NCI PAI S PAR ÂME T ROS DOS DI ODOS

• Tensão de pico inversa repetitiva (VRRM)
• Máxima tensão reversa suportada pelo diodo em situação cíclica.


PR I NCI PAI S PAR ÂME T ROS DOS DI ODOS

• Corrente direta média máxima (IF(AV))
• Máxima corrente média suportada pelo diodo.


PR I NCI PAI S PAR ÂME T ROS DOS DI ODOS

• Corrente de pico não repetitiva (IFSM)
• Pico de corrente suportado pelo diodo em situação não cíclica.


PR I NCI PAI S PAR ÂME T ROS DOS DI ODOS

• Temperatura máxima da junção (TJ )
• Máxima temperatura suportada pelo diodo.


PR I NCI PAI S PAR ÂME T ROS DOS DI ODOS

• Queda de tensão direta instantânea (VF)
• Máxima queda de tensão quando em condução.


PR I NCI PAI S PAR ÂME T ROS DOS DI ODOS

• Corrente reversa (IR)
• Máxima corrente quando o diodo encontra-se bloqueado.


P R I NC I PA I S PA R Â ME T ROS D OS D I OD OS

• Tempo de recuperação reverso (trr)
• Tempo para que a corrente no diodo se anule completamente.


OPE R AÇÃO DE DI ODOS E M SÉ R I E E E M PAR AL E L O

• A potência máxima que pode ser controlada por um único
diodo depende da sua tensão inversa nominal e da
corrente direta;
• Em aplicações de alta potência, um diodo pode não
suportar a capacidade de potência, sendo necessário
associar unidades em série (aumentar tensão) e em
paralelo (aumentar corrente).


ASSOCI AÇÃO DE DI ODOS E M SÉ R I E

• Necessário quando a tensão inversa for superior à tensão
nominal do diodo.
• Normalmente a tensão não fica igualmente dividida entre
os diodos devido suas características construtivas.
• O diodo que possuir a menor corrente de fuga assume a
maior parcela de tensão.


ASSOCI AÇÃO DE DI ODOS E M SÉ R I E

• Para equilibrar as tensões nos diodos deve-se utilizar
resistores em paralelo.


ASSOCI AÇÃO DE DI ODOS E M SÉ R I E – E XE MP LO

Dois diodos em série com tensão reversa nominal de 800 V são
polarizados inversamente por uma fonte de 1000 V. A corrente
de fuga medida é de 1,5 mA. Calcule:

a) A tensão reversa em cada
diodo;

b) O valor do resistor de
compartilhamento para que a
tensão no diodo D1 não
ultrapasse 55% do valor da
fonte;

c) A corrente total da fonte e
a potência dissipada nos
resistores.


ASSOCI AÇÃO DE DI ODOS E M PAR AL E L O

• Necessário quando a corrente de carga for superior à corrente
nominal do diodo.
• Normalmente a corrente não fica igualmente dividida entre os
diodos devido suas características construtivas.

• O diodo que possuir a menor queda de tensão direta assume
a maior parcela de corrente.


ASSOCI AÇÃO DE DI ODOS E M PAR AL E L O

• Para equilibrar as correntes deve-se utilizar um pequeno
resistor em série em cada diodo.


ASSOCI AÇÃO DE DI ODOS E M PAR AL E L O – E XE MP LO

Dois diodos são ligados em paralelo. A corrente total a ser
dividida em ambos é de 50 A. Para garantir o compartilhamento,
dois resistores são ligados em série com os diodos. Determine:
a) A resistência do resistor de
compartilhamento de corrente,
de tal modo que a corrente que
passa através de qualquer um
dos diodos não ultrapasse 55%
do valor da corrente total;

b) A perda total de potência
nos resistores;
c) A tensão nos terminais da
combinação de diodos.
    """

    aula, created = Aula.objects.get_or_create(
        titulo="Aula 2 - Chaves Semicondutoras - Diodos de Potência",
        defaults={
            "topicos": "Diodos de Potência, Modelos de Diodos (Ideal, com Vd, com Vd e Rd, Real), Principais Parâmetros (VRRM, IF(AV), IFSM, TJ, VF, IR, trr), Operação de Diodos em Série e em Paralelo, Exemplos de Associação de Diodos.",
            "conteudo_detalhado": aula_2_content
        }
    )

    # Conceitos da Aula 2
    Conceito.objects.get_or_create(
        titulo="Diodo de Potência",
        defaults={
            "definicao": "Dispositivo semicondutor similar ao diodo de sinal, mas com uma camada de dopagem adicional (N-) para suportar maiores potências. Utilizado em retificadores não-controlados e como diodos de retorno.",
            "explicacao_detalhada": "Diodos de potência são projetados para operar em circuitos de alta potência, diferentemente dos diodos de sinal. Eles possuem uma estrutura interna otimizada para lidar com altas correntes e tensões reversas, incluindo uma 'região de arrasto' que melhora suas características de bloqueio. São fundamentais em retificadores, onde convertem corrente alternada em corrente contínua."
        }
    )
    Conceito.objects.get_or_create(
        titulo="Modelos de Diodos de Potência",
        defaults={
            "definicao": "Representações simplificadas do comportamento de um diodo para análise de circuitos. Incluem Diodo Ideal, Diodo com Vd, Diodo com Vd e Rd, e Diodo Real.",
            "explicacao_detalhada": "Para simplificar a análise de circuitos com diodos de potência, diferentes modelos são utilizados. O 'Diodo Ideal' é a representação mais simples, assumindo queda de tensão zero e corrente de fuga zero. Modelos mais complexos, como 'Diodo com Vd' (queda de tensão constante) e 'Diodo com Vd e Rd' (queda de tensão linear), aproximam-se mais do comportamento real, enquanto o 'Diodo Real' considera todas as características não ideais, incluindo corrente de fuga e avalanche."
        }
    )
    Conceito.objects.get_or_create(
        titulo="Associação de Diodos em Série",
        defaults={
            "definicao": "Conexão de diodos em série para aumentar a capacidade de tensão inversa do conjunto. Requer resistores em paralelo para equilibrar as tensões.",
            "explicacao_detalhada": "Quando a tensão inversa de um circuito excede a capacidade de um único diodo, múltiplos diodos podem ser conectados em série. No entanto, devido a pequenas variações nas características de cada diodo, a tensão pode não ser igualmente dividida. Resistores de compartilhamento de tensão são adicionados em paralelo com cada diodo para garantir uma distribuição mais uniforme da tensão e evitar que um diodo seja sobrecarregado."
        }
    )
    Conceito.objects.get_or_create(
        titulo="Associação de Diodos em Paralelo",
        defaults={
            "definicao": "Conexão de diodos em paralelo para aumentar a capacidade de corrente do conjunto. Requer resistores em série para equilibrar as correntes.",
            "explicacao_detalhada": "Para lidar com correntes de carga que excedem a capacidade de um único diodo, vários diodos podem ser conectados em paralelo. Similar à associação em série, pequenas diferenças nas características dos diodos podem levar a uma distribuição desigual da corrente. Resistores de compartilhamento de corrente são inseridos em série com cada diodo para forçar uma divisão mais equitativa da corrente, protegendo os diodos de sobrecarga."
        }
    )

    # Fórmulas da Aula 2
    Formula.objects.get_or_create(
        nome="Cálculo de Resistência para Diodos em Série",
        formula_latex="R = \frac{V_{D1} - V_{D2}}{I_{D2} - I_{D1}}",
        descricao="Fórmula para calcular a resistência de compartilhamento em diodos em série, onde VD1 e VD2 são as tensões nos diodos e ID1 e ID2 são as correntes de fuga.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Cálculo de Resistência para Diodos em Paralelo",
        formula_latex="R = \frac{V_{D2} - V_{D1}}{I_{D1} - I_{D2}}",
        descricao="Fórmula para calcular a resistência de compartilhamento em diodos em paralelo, onde VD1 e VD2 são as quedas de tensão nos diodos e ID1 e ID2 são as correntes.",
        aula_relacionada=aula
    )

    # Exemplos da Aula 2
    Exemplo.objects.get_or_create(
        titulo="Exemplo de Associação de Diodos em Série",
        descricao="Dois diodos em série com tensão reversa nominal de 800 V são polarizados inversamente por uma fonte de 1000 V. A corrente de fuga medida é de 1,5 mA. Calcule: a) A tensão reversa em cada diodo; b) O valor do resistor de compartilhamento para que a tensão no diodo D1 não ultrapasse 55% do valor da fonte; c) A corrente total da fonte e a potência dissipada nos resistores.",
        passos_resolucao="""
(A solução detalhada para este exemplo seria extraída do gabarito e/ou da explicação do professor, incluindo cálculos passo a passo para cada item.)
        """,
        aula_relacionada=aula
    )
    Exemplo.objects.get_or_create(
        titulo="Exemplo de Associação de Diodos em Paralelo",
        descricao="Dois diodos são ligados em paralelo. A corrente total a ser dividida em ambos é de 50 A. Para garantir o compartilhamento, dois resistores são ligados em série com os diodos. Determine: a) A resistência do resistor de compartilhamento de corrente, de tal modo que a corrente que passa através de qualquer um dos diodos não ultrapasse 55% do valor da corrente total; b) A perda total de potência nos resistores; c) A tensão nos terminais da combinação de diodos.",
        passos_resolucao="""
(A solução detalhada para este exemplo seria extraída do gabarito e/ou da explicação do professor, incluindo cálculos passo a passo para cada item.)
        """,
        aula_relacionada=aula
    )

def populate_aula_3():
    # Aula 3 - Chaves Semicondutoras - Dispositivos Tiristores
    aula_3_content = """
Eletrônica de Potência I

CHAVES SEMICONDUTORAS

AULA 3
Dispositivos Tiristores
Prof. Danillo Borges Rodrigues


O SCR

• O Retificador Controlado de Silício (SCR – Silicon
Controlled Rectifier) é um dispositivo semicondutor com 4
camadas (PNPN) que permite controlar a entrada de
condução;

• Da mesma forma que o diodo, possui anodo (A) e catodo
(K). Além disso, possui um terceiro terminal (gate - G)
para controle de condução;


CURVA C AR ACT E R Í ST IC A DO SCR


CURVA C AR ACT E R Í ST IC A DO SCR

• Curva característica ideal


PR I NCI PAI S PAR ÂME T ROS DO SCR – T E NSÃO

• Tensão de bloqueio repetitivo em polarização direta
(VDRM)
✓ Tensão máxima instantânea que o SCR pode bloquear na direção
direta;

✓ Se o valor nominal de VDRM for ultrapassado, o SCR conduzirá
mesmo sem tensão/corrente de gate.


PR I NCI PAI S PAR ÂME T ROS DO SCR – T E NSÃO

• Tensão de pico repetitivo reversa (VRRM)
✓ Tensão máxima instantânea que o SCR pode suportar, sem se
danificar, na direção reversa;


P R I NCI PAI S PAR ÂME T ROS DO SCR – COR R E NT E

• Valor nominal máximo de corrente repetitivo (IT(RMS) e
IT(AV))
✓ Valores máximos médio e eficaz de corrente
suportados pelo SCR em seu estado ligado.

que podem ser

P R I NCI PAI S PAR ÂME T ROS DO SCR – COR R E NT E

• Valor nominal de corrente de surto (ITSM)
✓ É a corrente de pico no anodo que um SCR pode suportar durante
um curto intervalo de tempo;

✓ O valor nominal de corrente de surto pode ser de 5 a 20 vezes
maior do que o da corrente eficaz repetitiva (IT(RMS)).


P R I NCI PAI S PAR ÂME T ROS DO SCR – COR R E NT E

• Corrente de disparo (IL)
✓ É a corrente mínima de anodo que deve fluir pelo SCR a fim de
que ele fique no estado ligado logo após o sinal de gate ter sido
removido;

✓ Se não for alcançada quando o sinal estiver sendo aplicado no
gate, o SCR poderá até passar para o estado ligado, mas
retornará ao estado desligado quando esse sinal for removido.


PR I NCI PAI S PAR ÂME T ROS DO SCR – COR R E NT E

• Corrente de sustentação (IH)
✓ É a corrente mínima de anodo para manter a condução do SCR
após o mesmo ter recebido a corrente de disparo;

✓ Se a corrente de anodo sofrer uma redução abaixo de seu valor
crítico, o SCR passará para o estado desligado;


P R I NCI PAI S PAR ÂME T ROS DO SCR – TAXA DE VAR I AÇÃO

• Taxa de subida crítica da corrente no estado ligado
(valor nominal di/dt)
✓ Quando o SCR conduz, no início, a corrente de anodo fica
concentrada em uma área relativamente pequena, ao lado do
gate, até que depois de um tempo determinado, a condução se
espalha por igual ao longo do corpo do dispositivo;
✓ Os fabricantes estabelecem um valor seguro para a taxa de
variação da corrente di/dt de anodo que seus dispositivos podem
suportar.


P R I NCI PAI S PAR ÂME T ROS DO SCR – TAXA DE VAR I AÇÃO

• Taxa de subida crítica da corrente no estado ligado
(valor nominal di/dt)
✓ Para evitar danos ao SCR em consequência do valor alto de di/dt,
uma pequena indutância é colocada em série com o dispositivo;

✓ A indutância se opõe à variação de corrente, amortecendo a
subida da corrente de anodo;
✓ A indutância pode ser determinada a partir de:
𝑳≥

𝑽𝒑
𝒅𝒊ൗ
𝒅𝒕 𝒎𝒂𝒙

onde:
L é a indutância (em μH);
(di/dt)max é a taxa de variação do valor nominal de corrente do SCR (em A/μs);
Vp é o valor de pico da fonte de tensão (em V).


P R I NCI PAI S PAR ÂME T ROS DO SCR – TAXA DE VAR I AÇÃO

• Taxa de subida crítica da tensão no estado desligado
(valor nominal dv/dt)
✓ A aplicação de uma tensão direta com subida rápida no SCR em
estado desligado resulta em um fluxo de corrente nas junções
para a camada de gate;
✓ O valor nominal dv/dt fornece o tempo de subida máximo de um
pulso de tensão que pode ser aplicado ao SCR no estado
desligado sem provocar seu disparo não-programado.


P R I NCI PAI S PAR ÂME T ROS DO SCR – TAXA DE VAR I AÇÃO

• Taxa de subida crítica da tensão no estado desligado
(valor nominal dv/dt)
✓ Um circuito snubber RC é usado para evitar disparos não
programados em circuitos com valores altos de dv/dt;

✓ Uma pequena capacitância (CS) é colocada nos terminais do SCR
para promover a oposição à variação de tensão;

✓ Uma pequena resistência (RS) é acrescida em série com o
capacitor para o amortecimento da descarga e para limitar a
corrente transitória de passagem para o estado ligado.
𝑽𝑫𝑹𝑴
𝑪𝑺 ≥
𝑹𝑳 ⋅ 𝒅𝒗ൗ𝒅𝒕
𝒎𝒂𝒙

𝑹𝑺 ≥

𝑽𝑫𝑹𝑴
𝒅𝒊ൗ
𝒅𝒕 𝒎𝒂𝒙


PR I NCI PAI S PAR ÂME T ROS DO SCR – G ATE

• Corrente máxima de acionamento do gate (IGM)
✓ Corrente CC máxima de gate permitida para passar o SCR para o
estado ligado.

• Tensão máxima de acionamento do gate (VGTM)
✓ Tensão CC necessária para produzir IGM.

• Dissipação máxima de potência no gate (PGM)
✓ Produto instantâneo máximo da corrente de gate pela tensão de
gate que pode existir durante a polarização direta.


PR I NCI PAI S PAR ÂME T ROS DO SCR – G ATE

• Corrente mínima de acionamento do gate (IGT)
✓ Corrente CC mínima necessária no gate para passar o SCR para
o estado ligado.

• Tensão mínima de acionamento do gate (VGT)
✓ Tensão CC mínima entre gate e catodo necessária para acionar o
SCR.


PR I NCI PAI S PAR ÂME T ROS DO SCR – G ATE

• Tensão de pico inversa máxima no gate (VRGM)
✓ Valor máximo de tensão CC negativa que pode ser aplicado sem
danificar a junção gate-catodo.


CI R CUITOS DE ACI ONAME NTO DE G AT E DO SCR

• O circuito de disparo de SCR deve atender os seguintes
critérios:
✓ Produzir um sinal de gate de amplitude adequada, tempo de
subida suficientemente curto e com duração adequada;
✓ Assegurar que o disparo não ocorra em decorrência de ruídos;
✓ Assegurar que o disparo ocorra quando o SCR estiver
diretamente polarizado;

✓ Assegurar o acionamento simultâneo quando da utilização de
SCRs em série ou em paralelo.

• Três tipos básicos de disparo de gate costuma ser
usados:
✓ Sinais CC;
✓ Sinais CA;
✓ Sinais pulsados.


CI R CUITOS DE ACI ONAME NTO DE G AT E DO SCR

• Sinais CC
✓ Ao fechar a chave S aplica-se pulso no gate do SCR;
✓ O diodo D limita tensão negativa no gate e o resistor RG limita a
corrente.


CI R CUITOS DE ACI ONAME NTO DE G AT E DO SCR

• Sinais CC
✓ Exemplo:
O SCR utilizado no circuito apresentado abaixo é o BT151-500R. Se
a fonte EG for igual a 20 V, determine o valor de RG que fornecerá a
corrente suficiente para o disparo do SCR.


CI R CUITOS DE ACI ONAME NTO DE G AT E DO SCR

• Sinais CA
✓ O sinal de disparo é obtido através da própria fonte AC.


CI R CUITOS DE ACI ONAME NTO DE G AT E DO SCR

• Sinais CA
✓ Exemplo:
O SCR utilizado no circuito apresentado abaixo é o BT151-500R, o
qual apresenta IGT = 15 mA e VGT = 1,5 V. Sabendo que a fonte vS
apresenta uma tensão senoidal de 127 V RMS e que a resistência
RGK = 1 kΩ, determine os valores de R1 e R2.


CI R CUITOS DE ACI ONAME NTO DE G AT E DO SCR

• Sinais CA
✓ Exemplo:
IGT = 15 mA
VGT = 1,5 V
vS(rms) = 127 V
RGK = 1 kΩ
𝑽𝒑 ∙ 𝒔𝒆𝒏 𝜶 ∙ 𝑹𝑮𝑲 − 𝒗𝑮 ∙ 𝑹𝑮𝑲
𝑹𝑬𝑸 =
𝒗𝑮 + 𝒊𝑮 ∙ 𝑹𝑮𝑲


CI R CUITOS DE ACI ONAME NTO DE G AT E DO SCR

• Sinais Pulsados
✓ Geram um único pulso ou um trem de pulsos no gate do
SCR, em vez de um sinal CC.

✓ Vantagens:
▪ Menor dissipação de potência no gate;
▪ Permite um controle preciso do ponto no qual o dispositivo é
disparado;
▪ Fornece isolação elétrica do circuito de disparo e o gate
(transformador de pulso ou acoplador óptico);

▪ Menor interferência de ruídos.


CI R CUITOS DE ACI ONAME NTO DE G AT E DO SCR

• Sinais Pulsados
✓ Circuito de acionamento de SCR usando oscilador de
transistor de unijunção (unijunction transistor – UJT):


CI R CUITOS DE ACI ONAME NTO DE G AT E DO SCR

• Sinais Pulsados
✓ Circuito de acionamento de SCR usando oscilador de
transistor de unijunção (unijunction transistor – UJT):
Valo
    """

    aula, created = Aula.objects.get_or_create(
        titulo="Aula 3 - Chaves Semicondutoras - Dispositivos Tiristores",
        defaults={
            "topicos": "O SCR (Silicon Controlled Rectifier), Curva Característica do SCR, Principais Parâmetros do SCR (Tensão, Corrente, Taxa de Variação, Gate), Circuitos de Acionamento de Gate do SCR (Sinais CC, Sinais CA, Sinais Pulsados), Exemplos de Acionamento.",
            "conteudo_detalhado": aula_3_content
        }
    )

    # Conceitos da Aula 3
    Conceito.objects.get_or_create(
        titulo="SCR (Silicon Controlled Rectifier)",
        defaults={
            "definicao": "Dispositivo semicondutor de 4 camadas (PNPN) que permite controlar a entrada em condução. Possui ânodo (A), cátodo (K) e um terminal de controle (gate - G).",
            "explicacao_detalhada": "O SCR é um tipo de tiristor que atua como uma chave controlada. Uma vez disparado por um pulso no gate, ele permanece em condução até que a corrente no ânodo caia abaixo de um valor mínimo (corrente de sustentação) ou a tensão reversa seja aplicada. É amplamente utilizado em aplicações de controle de potência, como retificadores controlados e reguladores de tensão."
        }
    )
    Conceito.objects.get_or_create(
        titulo="Tensão de Bloqueio Repetitivo em Polarização Direta (VDRM)",
        defaults={
            "definicao": "Tensão máxima instantânea que o SCR pode bloquear na direção direta sem disparar, mesmo sem sinal de gate.",
            "explicacao_detalhada": "Este parâmetro é crucial para a segurança do SCR. Se a tensão aplicada no ânodo-cátodo exceder o VDRM, o SCR pode disparar indevidamente, mesmo sem um pulso no gate, o que pode levar a falhas no circuito. É a tensão máxima que o SCR pode suportar no estado de bloqueio direto de forma repetitiva."
        }
    )
    Conceito.objects.get_or_create(
        titulo="Corrente de Disparo (IL)",
        defaults={
            "definicao": "Corrente mínima de ânodo que deve fluir pelo SCR para que ele permaneça no estado ligado após a remoção do sinal de gate.",
            "explicacao_detalhada": "A corrente de disparo (latching current) é a corrente mínima que deve ser atingida no ânodo para que o SCR 'trave' no estado de condução. Se a corrente de ânodo não atingir esse valor após o pulso de gate, o SCR retornará ao estado de bloqueio quando o pulso for removido."
        }
    )
    Conceito.objects.get_or_create(
        titulo="Corrente de Sustentação (IH)",
        defaults={
            "definicao": "Corrente mínima de ânodo para manter a condução do SCR após o disparo. Se a corrente cair abaixo de IH, o SCR desliga.",
            "explicacao_detalhada": "A corrente de sustentação (holding current) é a corrente mínima necessária para manter o SCR no estado de condução. Se a corrente de ânodo cair abaixo desse valor, o SCR se desliga automaticamente. Este parâmetro é importante para garantir que o SCR permaneça ligado durante o ciclo de condução e desligue corretamente quando a corrente for interrompida."
        }
    )
    Conceito.objects.get_or_create(
        titulo="Taxa de Subida Crítica da Corrente (di/dt)",
        defaults={
            "definicao": "Taxa máxima de variação da corrente de ânodo que o SCR pode suportar sem danos durante o chaveamento para o estado ligado.",
            "explicacao_detalhada": "Quando um SCR é ligado, a corrente não se espalha instantaneamente por toda a junção. Uma alta taxa de di/dt pode causar pontos quentes localizados e danos ao dispositivo. Indutores em série são usados para limitar essa taxa de subida da corrente e proteger o SCR."
        }
    )
    Conceito.objects.get_or_create(
        titulo="Taxa de Subida Crítica da Tensão (dv/dt)",
        defaults={
            "definicao": "Taxa máxima de variação da tensão de ânodo que o SCR pode suportar sem disparar indevidamente no estado desligado.",
            "explicacao_detalhada": "Uma rápida variação de tensão no ânodo de um SCR desligado pode gerar uma corrente capacitiva interna que pode disparar o dispositivo de forma não intencional. Circuitos snubber RC são utilizados para limitar essa taxa de dv/dt e evitar disparos falsos, garantindo a operação segura do SCR."
        }
    )
    Conceito.objects.get_or_create(
        titulo="Circuito Snubber RC",
        defaults={
            "definicao": "Circuito composto por um resistor (R) e um capacitor (C) em série, conectado em paralelo com um dispositivo semicondutor (como um SCR), utilizado para limitar a taxa de subida da tensão (dv/dt) e proteger o dispositivo durante o chaveamento.",
            "explicacao_detalhada": "O circuito snubber RC é uma técnica de proteção comum em eletrônica de potência. O capacitor limita a taxa de dv/dt através do dispositivo, enquanto o resistor em série com o capacitor amortece as oscilações e limita a corrente de descarga do capacitor quando o dispositivo liga. Isso previne disparos falsos e reduz o estresse sobre o semicondutor."
        }
    )

    # Fórmulas da Aula 3
    Formula.objects.get_or_create(
        nome="Indutância para Limitar di/dt",
        formula_latex="L \ge \frac{V_p}{(di/dt)_{max}}",
        descricao="Indutância mínima necessária para limitar a taxa de subida da corrente (di/dt) em um SCR, onde Vp é a tensão de pico da fonte.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Capacitância para Limitar dv/dt (Snubber)",
        formula_latex="C_S \ge \frac{V_{DRM}}{R_L \cdot (dv/dt)_{max}}",
        descricao="Capacitância mínima para o circuito snubber RC para limitar a taxa de subida da tensão (dv/dt) em um SCR, onde VDRM é a tensão de bloqueio repetitivo direto e RL é a resistência de carga.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Resistência para Limitar dv/dt (Snubber)",
        formula_latex="R_S \ge \frac{V_{DRM}}{(di/dt)_{max}}",
        descricao="Resistência mínima para o circuito snubber RC para limitar a corrente transitória de passagem para o estado ligado.",
        aula_relacionada=aula
    )

    # Exemplos da Aula 3
    Exemplo.objects.get_or_create(
        titulo="Exemplo de Acionamento de SCR (Sinais CC)",
        descricao="O SCR utilizado no circuito apresentado abaixo é o BT151-500R. Se a fonte EG for igual a 20 V, determine o valor de RG que fornecerá a corrente suficiente para o disparo do SCR.",
        passos_resolucao="""
(A solução detalhada para este exemplo seria extraída do gabarito e/ou da explicação do professor, incluindo cálculos passo a passo.)
        """,
        aula_relacionada=aula
    )
    Exemplo.objects.get_or_create(
        titulo="Exemplo de Acionamento de SCR (Sinais CA)",
        descricao="O SCR utilizado no circuito apresentado abaixo é o BT151-500R, o qual apresenta IGT = 15 mA e VGT = 1,5 V. Sabendo que a fonte vS apresenta uma tensão senoidal de 127 V RMS e que a resistência RGK = 1 kΩ, determine os valores de R1 e R2.",
        passos_resolucao="""
(A solução detalhada para este exemplo seria extraída do gabarito e/ou da explicação do professor, incluindo cálculos passo a passo.)
        """,
        aula_relacionada=aula
    )

def populate_aula_4():
    # Aula 4 - Chaves Semicondutoras - Transistores de Potência
    aula_4_content = """
Eletrônica de Potência I

CHAVES SEMICONDUTORAS

AULA 4
Transistores de Potência
Prof. Danillo Borges Rodrigues


T R ANSI STOR E S DE P OT Ê NCI A

• Os transistores tem dois tipos básicos de aplicações:
amplificação e chaveamento;
• Em eletrônica de potência, em que o objetivo principal é o
controle eficaz de potência, os transistores de potência
são invariavelmente usados como chaves;
• Três tipos de transistores de potência são muito utilizados
em circuitos de eletrônica de potência:


T R ANSI STOR E S B I POL AR E S DE J UNÇÃO DE P OT Ê NCI A ( B J T )

• O BJT tem três terminais: a base (B), o coletor (C) e o
emissor (E);
• Quando um BJT é usado como chave, é necessário uma
corrente que passa pela junção base-emissor alta para
induzir o fluxo total de corrente entre coletor-emissor.


T R ANSI STOR E S B I POL AR E S DE J UNÇÃO DE P OT Ê NCI A ( B J T )
C URVA C ARACT E RÍS TICA T E N S ÃO - CORRE N TE


T R ANSI STOR E S B I POL AR E S DE J UNÇÃO DE P OT Ê NCI A ( B J T )
C URVA C ARACT E RÍS TICA T E N S ÃO - CORRE N TE

• Curva característica ideal


T R ANSI STOR E S B I POL AR E S DE J UNÇÃO DE P OT Ê NCI A ( B J T )
VAL O RE S N O M I NAIS

• Tensão de bloqueio direto (VCEO ou VCEO(SUS))
✓ Um transistor pode suportar uma tensão de coletor-emissor
máxima. Acima desse valor, ocorrerá a ruptura da junção do
coletor.
✓ A tensão de bloqueio direta é a tensão máxima VCE com a base
aberta.


T R ANSI STOR E S B I POL AR E S DE J UNÇÃO DE P OT Ê NCI A ( B J T )
VAL O RE S N O M I NAIS

• Tensão de saturação coletor-emissor (VCE(sat))
✓ É uma queda de tensão muito baixa através dos terminais de
coletor-emissor na condição de saturação.


T R ANSI STOR E S B I POL AR E S DE J UNÇÃO DE P OT Ê NCI A ( B J T )
VAL O RE S N O M I NAIS

• Ganho de corrente CC (hFE ou b)
✓ É a relação entre o valor da corrente de coletor IC e o
correspondente valor de corrente CC de base IB.


T R ANSI STOR E S B I POL AR E S DE J UNÇÃO DE P OT Ê NCI A ( B J T )
VAL O RE S N O M I NAIS

• Velocidades de chaveamento
✓ Os transistores de potência passam de ligado para desligado e
vice-versa com rapidez muito maior do que os transistores.
✓ Podem passar para ligado e para
desligado em menos de 1ms.

✓ Normalmente os transistores de potência
são usados para aplicações cuja
frequência chegue a no máximo 100kHz.


T R ANSI STOR E S B I POL AR E S DE J UNÇÃO DE P OT Ê NCI A ( B J T )
VAL O RE S N O M I NAIS

• Corrente máxima de coletor (IC(max))
✓ É o valor nominal de corrente de coletor permissível.


T R ANSI STOR E S B I POL AR E S DE J UNÇÃO DE P OT Ê NCI A ( B J T )
VAL O RE S N O M I NAIS

• Dissipação máxima de potência (PT)
✓ É o valor nominal máximo de potência de um transistor.

• Temperatura máxima da junção (Tj)
✓ É o valor máximo permissível de temperatura da junção.


T R ANSI STOR E S B I POL AR E S DE J UNÇÃO DE P OT Ê NCI A ( B J T )
ÁRE A D E O P E R AÇÃO S E G UR A

• Para garantir a operação segura do transistor, os fabricantes
especificam limites na curva VCE x IC para definir a área de
operação segura (Safe Operating Area – SOA).


T R ANSI STOR E S B I POL AR E S DE J UNÇÃO DE P OT Ê NCI A ( B J T )
ÁR E A D E OP E RAÇÃO S E G UR A: RUP T UR A SE CUNDÁR IA


T R ANSI STOR E S B I POL AR E S DE J UNÇÃO DE P OT Ê NCI A ( B J T )
C I R CUITO S N UB B E R

• Os snubbers podem ser utilizados para evitar a ocorrência
simultânea dos picos de tensão e corrente durante o corte,
limitando a tensão no transistor durante transitórios de
chaveamento;


T R ANSI STOR E S DE E FE I TO DE C AMP O ME TAL - ÓXI DO SE MI CONDUTOR DE P OT Ê NCI A ( M O S F E T )

• O MOSFET tem três terminais: a porta (gate - G), o
dreno (drain - D) e a fonte (source - S);
• É a tensão de gate que controla as condições ligado e
desligado do MOSFET;
• Pelo isolamento resistivo do gate, a
corrente de gate é praticamente zero
tanto na condição ligada como
desligada;
• O MOSFET consegue transições mais
rápidas entre os estados ligado e
desligado que o BJT, sendo mais
utilizado em aplicações de alta
frequência.


T R ANSI STOR E S DE E FE I TO DE C AMP O ME TAL - ÓXI DO SE MI CONDUTOR DE P OT Ê NCI A ( M O S F E T )
C URVA C AR ACTERÍS TICA TENS ÃO - CORRENTE


T R ANSI STOR E S DE E FE I TO DE C AMP O ME TAL - ÓXI DO SE MI CONDUTOR DE P OT Ê NCI A ( M O S F E T )
C URVA C AR ACTERÍS TICA DE TRANS F ERÊNCIA

✓ Para 𝑽𝑮𝑺 < 𝑽𝑮𝑺(𝒕𝒉) : 𝑰𝑫 = 𝟎
✓ Para 𝑽𝑮𝑺 > 𝑽𝑮𝑺(𝒕𝒉) : 𝑰𝑫 = 𝒈𝒇𝒔 ⋅ 𝑽𝑮𝑺 − 𝑽𝑮𝑺(𝒕𝒉)


T R ANSI STOR E S DE E FE I TO DE C AMP O ME TAL - ÓXI DO SE MI C OND UTOR D E P OT Ê NC I A ( M O S F E T )
ÁR E A DE OP ERAÇÃO S EG URA


T R ANSI STOR E S DE E FE I TO DE C AMP O ME TAL - ÓXI DO SE MI CONDUTOR DE P OT Ê NCI A ( M O S F E T )
VAL ORE S N OM I NAIS


T R ANSI STOR E S B I P OL AR E S DE P ORTA I SOL ADA( IG BT)

• O IGBT mescla as características de baixa queda de
tensão no estado ligado do BJT com excelentes
características de chaveamento, simples circuito de
acionamento de gate e a alta impedância de entrada do
MOSFET;
• Existem IGBTs com valores
nominais de corrente e de tensão
bem além daqueles normalmente
encontrados para MOSFETs de
potência;
• Embora
as
velocidades
de
chaveamento dos IGBTs sejam
maiores do que as dos BJTs, são
menores do que as dos MOSFETs.


T R ANSI STOR E S B I P OL AR E S DE P ORTA I SOL ADA( IG BT)
C URVA C ARACT E RÍS TICA T E N S ÃO - CORRE N TE


T R ANSI STOR E S B I P OL AR E S DE P ORTA I SOL ADA( IG BT )
VAL O RE S N O M I NAIS
    """

    aula, created = Aula.objects.get_or_create(
        titulo="Aula 4 - Chaves Semicondutoras - Transistores de Potência",
        defaults={
            "topicos": "Transistores de Potência, BJT (Transistor Bipolar de Junção), MOSFET (Transistor de Efeito de Campo Metal-Óxido Semicondutor), IGBT (Transistor Bipolar de Porta Isolada), Curvas Características, Valores Nominais, Área de Operação Segura, Circuitos Snubber.",
            "conteudo_detalhado": aula_4_content
        }
    )

    # Conceitos da Aula 4
    Conceito.objects.get_or_create(
        titulo="Transistor de Potência",
        defaults={
            "definicao": "Dispositivo semicondutor utilizado como chave em eletrônica de potência para controle eficaz de energia. Tipos comuns incluem BJT, MOSFET e IGBT.",
            "explicacao_detalhada": "Transistores de potência são otimizados para operar como chaves em circuitos de alta potência, diferentemente dos transistores de sinal que são usados para amplificação. Eles são projetados para suportar altas tensões e correntes, e sua capacidade de chaveamento rápido é crucial para a eficiência dos conversores de potência. Os principais tipos são BJT, MOSFET e IGBT, cada um com características e aplicações específicas."
        }
    )
    Conceito.objects.get_or_create(
        titulo="BJT (Transistor Bipolar de Junção)",
        defaults={
            "definicao": "Transistor de potência com três terminais (base, coletor, emissor) que requer uma corrente de base para controlar o fluxo de corrente entre coletor e emissor.",
            "explicacao_detalhada": "O BJT é um transistor controlado por corrente. Para que ele conduza (estado ligado), uma corrente significativa deve ser aplicada na base. Embora robustos, os BJTs de potência geralmente têm velocidades de chaveamento mais lentas e maiores perdas de condução em comparação com os MOSFETs e IGBTs, sendo mais adequados para aplicações de menor frequência."
        }
    )
    Conceito.objects.get_or_create(
        titulo="MOSFET (Transistor de Efeito de Campo Metal-Óxido Semicondutor)",
        defaults={
            "definicao": "Transistor de potência com três terminais (porta, dreno, fonte) onde a tensão na porta controla as condições de ligado e desligado. Possui alta impedância de entrada e transições rápidas.",
            "explicacao_detalhada": "O MOSFET é um transistor controlado por tensão, o que significa que a corrente de gate é praticamente zero. Ele é conhecido por suas altas velocidades de chaveamento e baixas perdas de condução em baixas tensões, tornando-o ideal para aplicações de alta frequência. No entanto, sua resistência de condução aumenta com a tensão nominal, limitando seu uso em aplicações de altíssima potência."
        }
    )
    Conceito.objects.get_or_create(
        titulo="IGBT (Transistor Bipolar de Porta Isolada)",
        defaults={
            "definicao": "Dispositivo híbrido que combina as vantagens do BJT (baixa queda de tensão em condução) e do MOSFET (controle por tensão e alta impedância de entrada).",
            "explicacao_detalhada": "O IGBT é um componente chave em eletrônica de potência que busca o melhor dos dois mundos: a baixa queda de tensão no estado ligado do BJT e a facilidade de controle por tensão do MOSFET. Ele oferece uma boa combinação de capacidade de corrente, tensão e velocidade de chaveamento, sendo amplamente utilizado em aplicações de média a alta potência, como inversores e conversores de frequência."
        }
    )
    Conceito.objects.get_or_create(
        titulo="Área de Operação Segura (SOA)",
        defaults={
            "definicao": "Região no gráfico VCE x IC (ou VDS x ID) que define os limites de tensão e corrente dentro dos quais um transistor pode operar com segurança sem sofrer danos.",
            "explicacao_detalhada": "A Área de Operação Segura (SOA) é um gráfico fornecido pelos fabricantes que indica as combinações máximas de tensão e corrente que um transistor pode suportar em diferentes condições de operação (contínua, pulsada, durante o chaveamento). Operar o transistor fora da SOA pode levar a falhas por superaquecimento, ruptura secundária ou outros mecanismos de dano."
        }
    )

    # Fórmulas da Aula 4 (Exemplos de BJT)
    Formula.objects.get_or_create(
        nome="Corrente de Coletor (Saturação BJT)",
        formula_latex="I_C = \frac{V_{CC} - V_{CE}}{R_C} \approx \frac{V_{CC}}{R_C}",
        descricao="Corrente de coletor para um BJT operando na saturação, onde VCC é a tensão da fonte e RC é a resistência de coletor.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Corrente de Base Mínima (Saturação BJT)",
        formula_latex="I_B \ge \frac{I_C}{\beta}",
        descricao="Corrente de base mínima necessária para garantir a saturação de um BJT, onde IC é a corrente de coletor e beta é o ganho de corrente.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Resistência de Base (BJT)",
        formula_latex="R_B = \frac{V_B - V_{BE}}{I_B}",
        descricao="Resistência de base para um BJT, onde VB é a tensão de base e VBE é a queda de tensão base-emissor.",
        aula_relacionada=aula
    )

    # Fórmulas da Aula 4 (MOSFET)
    Formula.objects.get_or_create(
        nome="Corrente de Dreno (MOSFET - Região de Saturação)",
        formula_latex="I_D = g_{fs} \cdot (V_{GS} - V_{GS(th)}) \text{ (para } V_{GS} > V_{GS(th)} \text{)}",
        descricao="Corrente de dreno para um MOSFET operando na região de saturação, onde gfs é a transcondutância, VGS é a tensão gate-fonte e VGS(th) é a tensão de limiar.",
        aula_relacionada=aula
    )

def populate_aula_5():
    # Aula 5 - Retificador Monofásico Não Controlado de Meia Onda - Carga R
    aula_5_content = """
Eletrônica de Potência I
RETIFICADORES MONOFÁSICOS
NÃO-CONTROLADOS DE MEIA
ONDA

AULA 5
Carga R
Prof. Danillo Borges Rodrigues


C AR ACT E R Í STI C AS DE AP P L I C AÇÕE S

• A retificação é o processo de converter tensão e corrente
alternadas em tensão e corrente contínuas;

• O objetivo é converter potência CA em potência CC;

• Para a retificação não-controlada, tem-se o uso exclusivo
de diodos;
• A amplitude de saída CC é determinada pela amplitude
de entrada CA;

• Retificador monofásico de meia onda: Pouco utilizado em
aplicações industriais.


R E T I FI C ADOR MONOFÁSI CO DE ME I A ONDA – C AR G A R


R E T I FI C ADOR MONOFÁSI CO DE ME I A ONDA – C AR G A R

• Valor médio da tensão de saída, Vo(médio):
𝑽𝒐 𝒎é𝒅𝒊𝒐 = \frac{V_m}{\pi} = 0.318 \cdot V_m


R E T I FI C ADOR MONOFÁSI CO DE ME I A ONDA – C AR G A R

• Valor eficaz da tensão de saída, Vo(rms):
𝑽𝒐 𝒓𝒎𝒔 = \frac{V_m}{2}


R E T I FI C ADOR MONOFÁSI CO DE ME I A ONDA – C AR G A R

• Valor médio da corrente de carga, Io(médio):
𝑰𝒐 𝒎é𝒅𝒊𝒐 = \frac{V_o_{médio}}{R} = \frac{V_m}{\pi \cdot R}

• Valor eficaz da corrente de carga, Io(rms):
𝑰𝒐 𝒓𝒎𝒔 = \frac{V_o_{rms}}{R} = \frac{V_m}{2 \cdot R}


R E T I FI C ADOR MONOFÁSI CO DE ME I A ONDA – C AR G A R

• Valor pico da corrente no diodo, ID(pico):
𝑰𝑫 𝒑𝒊𝒄𝒐 = I_{o_{pico}} = \frac{V_m}{R}

• Valor eficaz da corrente no diodo, ID(rms):
𝑰𝑫 𝒓𝒎𝒔 = I_{o_{rms}} = \frac{V_m}{2 \cdot R}


R E T I FI C ADOR MONOFÁSI CO DE ME I A ONDA – C AR G A R

• Valor pico da tensão reversa no diodo, VD(pico):
𝑽𝑫 𝒑𝒊𝒄𝒐 = V_{o_{pico}} = V_m

• Valor eficaz da tensão reversa no diodo, VD(rms):
𝑽𝑫 𝒓𝒎𝒔 = \frac{V_m}{2}


R E T I FI C ADOR MONOFÁSI CO DE ME I A ONDA – C AR G A R :
E X E M P LO

Um retificador monofásico não-controlado de meia onda
tem uma tensão de alimentação senoidal dada por 𝑣𝑠 (𝑡) =
170 ⋅ 𝑠𝑒𝑛(377𝑡) . Se a resistência de carga for de 15Ω,
determine:
a) A tensão média na carga;
b) A corrente média na carga;
c) A corrente eficaz na carga;
d) A potência absorvida na carga;
e) A potência aparente fornecida pela fonte;
f) O fator de potência do circuito.
    """

    aula, created = Aula.objects.get_or_create(
        titulo="Aula 5 - Retificador Monofásico Não Controlado de Meia Onda - Carga R",
        defaults={
            "topicos": "Retificação, Retificador Monofásico de Meia Onda, Características e Aplicações, Cálculos de Tensão e Corrente (Médio, Eficaz, Pico) na Carga e no Diodo, Exemplo de Retificador de Meia Onda com Carga Resistiva.",
            "conteudo_detalhado": aula_5_content
        }
    )

    # Conceitos da Aula 5
    Conceito.objects.get_or_create(
        titulo="Retificação",
        defaults={
            "definicao": "Processo de converter tensão e corrente alternadas (CA) em tensão e corrente contínuas (CC).",
            "explicacao_detalhada": "A retificação é uma das funções mais básicas em eletrônica de potência, essencial para converter a energia CA da rede elétrica em energia CC, que é utilizada pela maioria dos dispositivos eletrônicos. Conversores que realizam a retificação são chamados de retificadores."
        }
    )
    Conceito.objects.get_or_create(
        titulo="Retificador Monofásico Não Controlado de Meia Onda",
        defaults={
            "definicao": "Circuito retificador que utiliza um diodo para permitir a passagem de corrente em apenas metade do ciclo da tensão alternada de entrada, resultando em uma saída de tensão pulsante unidirecional. Não é amplamente utilizado em aplicações industriais devido à sua baixa eficiência e alta ondulação.",
            "explicacao_detalhada": "Este é o tipo mais simples de retificador. Ele usa apenas um diodo para retificar a forma de onda CA, permitindo que apenas os semiciclos positivos (ou negativos, dependendo da polaridade do diodo) passem para a carga. A tensão de saída é pulsante e possui um valor médio baixo, além de uma alta ondulação, o que o torna inadequado para muitas aplicações que exigem uma fonte CC estável."
        }
    )

    # Fórmulas da Aula 5
    Formula.objects.get_or_create(
        nome="Tensão Média na Carga (Retificador Meia Onda - Carga R)",
        formula_latex="V_{o_{médio}} = \frac{V_m}{\pi} = 0.318 \cdot V_m",
        descricao="Tensão média de saída para um retificador monofásico de meia onda com carga resistiva.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Tensão Eficaz na Carga (Retificador Meia Onda - Carga R)",
        formula_latex="V_{o_{rms}} = \frac{V_m}{2}",
        descricao="Tensão eficaz de saída para um retificador monofásico de meia onda com carga resistiva.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Corrente Média na Carga (Retificador Meia Onda - Carga R)",
        formula_latex="I_{o_{médio}} = \frac{V_{o_{médio}}}{R} = \frac{V_m}{\pi \cdot R}",
        descricao="Corrente média na carga para um retificador monofásico de meia onda com carga resistiva.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Corrente Eficaz na Carga (Retificador Meia Onda - Carga R)",
        formula_latex="I_{o_{rms}} = \frac{V_{o_{rms}}}{R} = \frac{V_m}{2 \cdot R}",
        descricao="Corrente eficaz na carga para um retificador monofásico de meia onda com carga resistiva.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Corrente de Pico no Diodo (Retificador Meia Onda - Carga R)",
        formula_latex="I_{D_{pico}} = \frac{V_m}{R}",
        descricao="Corrente de pico no diodo para um retificador monofásico de meia onda com carga resistiva.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Corrente Eficaz no Diodo (Retificador Meia Onda - Carga R)",
        formula_latex="I_{D_{rms}} = \frac{V_m}{2 \cdot R}",
        descricao="Corrente eficaz no diodo para um retificador monofásico de meia onda com carga resistiva.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Tensão de Pico Reversa no Diodo (Retificador Meia Onda - Carga R)",
        formula_latex="V_{D_{pico}} = V_m",
        descricao="Tensão de pico reversa no diodo para um retificador monofásico de meia onda com carga resistiva.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Tensão Eficaz Reversa no Diodo (Retificador Meia Onda - Carga R)",
        formula_latex="V_{D_{rms}} = \frac{V_m}{2}",
        descricao="Tensão eficaz reversa no diodo para um retificador monofásico de meia onda com carga resistiva.",
        aula_relacionada=aula
    )

    # Exemplo da Aula 5
    Exemplo.objects.get_or_create(
        titulo="Exemplo de Retificador de Meia Onda - Carga R",
        descricao="Um retificador monofásico não-controlado de meia onda tem uma tensão de alimentação senoidal dada por vs(t) = 170 ⋅ sen(377t). Se a resistência de carga for de 15Ω, determine: a) A tensão média na carga; b) A corrente média na carga; c) A corrente eficaz na carga; d) A potência absorvida na carga; e) A potência aparente fornecida pela fonte; f) O fator de potência do circuito.",
        passos_resolucao="""
(A solução detalhada para este exemplo seria extraída do gabarito e/ou da explicação do professor, incluindo cálculos passo a passo para cada item.)
        """,
        aula_relacionada=aula
    )

def populate_aula_6():
    # Aula 6 - Retificador Monofásico Não Controlado de Meia Onda - Carga RL
    aula_6_content = """
Eletrônica de Potência I
RETIFICADORES MONOFÁSICOS
NÃO-CONTROLADOS DE MEIA
ONDA

AULA 6
Carga RL
Prof. Danillo Borges Rodrigues


RE TIFIC AD O R MONOF ÁSIC O DE MEIA ONDA – C ARGA RL


RE TIFIC AD O R MONOF ÁSIC O DE MEIA ONDA – C ARGA RL
Ângulo de extinção


RE TIFIC AD O R MONOF ÁSIC O DE MEIA ONDA – C ARGA RL

• Valor médio da tensão de saída, Vo(médio):
𝑽𝒐 𝒎é𝒅𝒊𝒐 = \frac{V_m}{2\pi} \cdot (1 - \cos(\phi))


RE TIFIC AD O R MONOF ÁSIC O DE MEIA ONDA – C ARGA RL

• Valor eficaz da tensão de saída, Vo(rms):
𝑽𝒐 𝒓𝒎𝒔 = V_m \sqrt{\frac{1}{2\pi} \left( \frac{\phi}{2} - \frac{\sin(2\phi)}{4} \right)}


RE TIFIC AD O R MONOF ÁSIC O DE MEIA ONDA – C ARGA RL

• Expressão para a corrente de carga, io(t):

Quando o diodo está conduzindo, o circuito do retificador pode ser
simplificado nesse circuito equivalente:

Em que, pela lei de Kirchhoff da tensões, considerando a variável
normalizada 𝝎𝒕:
𝑽𝒎 ⋅ 𝒔𝒆𝒏 𝝎𝒕 = 𝑹 ⋅ 𝒊𝒐 𝝎𝒕 + 𝑳 ⋅

𝒅𝒊𝒐 𝝎𝒕
𝒅𝝎𝒕


RE TIFIC AD O R MONOF ÁSIC O DE MEIA ONDA – C ARGA RL

• Expressão para a corrente de carga, io(t):

Em regime permanente:
𝑰𝒐(𝒇𝒐𝒓ç𝒂𝒅𝒐) = \frac{V_m \angle 0°}{Z \angle \theta}

𝒊𝒐(𝒇𝒐𝒓ç𝒂𝒅𝒐) 𝝎𝒕 = \frac{V_m}{Z} \cdot \sin(\omega t - \theta)

Em que:
𝒁 = \sqrt{R^2 + (\omega L)^2}
𝜽 = \tan^{-1}\left(\frac{\omega L}{R}\right)

Em regime transitório:
𝒊𝒐(𝒏𝒂𝒕𝒖𝒓𝒂𝒍) 𝝎𝒕 = A \cdot e^{-\frac{R}{\omega L} \cdot \omega t}


RE TIFIC AD O R MONOF ÁSIC O DE MEIA ONDA – C ARGA RL

• Expressão para a corrente de carga, io(t):

𝒊𝒐 𝝎𝒕 = \frac{V_m}{Z} \cdot \left( \sin(\omega t - \theta) + \sin(\theta) \cdot e^{-\frac{R}{\omega L} \cdot \omega t} \right)

O ângulo de extinção da corrente de carga, sabendo que 𝒊𝒐 𝝎𝒕 = 𝟎
quando 𝝎𝒕 = 𝝓, pode ser determinado pela solução numérica de:
𝒔𝒆𝒏 𝝓 − 𝜽 + 𝒔𝒆𝒏 𝜽 ⋅ 𝒆^{-\frac{R}{\omega L} \cdot \phi} = 0


RE TIFIC AD O R MONOF ÁSIC O DE MEIA ONDA – C ARGA RL

• Valores médios da corrente de carga, Io(médio), e da
corrente no diodo, ID(médio) :
𝑰𝒐 𝒎é𝒅𝒊𝒐 = 𝑰𝑫 𝒎é𝒅𝒊𝒐 = \frac{1}{2\pi} \int_{0}^{\phi} i_o(\omega t) \cdot d(\omega t)

• Valores eficazes da corrente de carga, Io(rms), e da
corrente no diodo, ID(rms) :
𝑰𝒐 𝒓𝒎𝒔 = 𝑰𝑫 𝒓𝒎𝒔 = \sqrt{\frac{1}{2\pi} \int_{0}^{\phi} i_o^2(\omega t) \cdot d(\omega t)}


RE TIFIC AD O R MONOF ÁSIC O DE MEIA ONDA – C ARGA RL

• Valor pico da tensão reversa no diodo, VD(pico):
o Para 𝝅 < 𝝓 ≤ 𝟑⋅𝝅Τ𝟐:
𝑽𝑫 𝒑𝒊𝒄𝒐 = V_m

o Para 𝟑⋅𝝅Τ𝟐 < 𝝓 ≤ 𝟐 ⋅ 𝝅:
𝑽𝑫 𝒑𝒊𝒄𝒐 = V_m \cdot \sin(\phi)

• Valor eficaz da tensão reversa no diodo, VD(rms):
𝑽𝑫 𝒓𝒎𝒔 = \sqrt{\frac{1}{2\pi} \int_{\phi}^{2\pi} V_m^2 \cdot \sin^2(\omega t) \cdot d(\omega t)}


RE TIFIC AD O R MONOF ÁSIC O DE MEIA ONDA – C ARGA RL:
EXEM PL O

Um retificador monofásico não-controlado de meia onda
tem um fonte de 120VRMS em 60Hz e uma carga RL, onde R
= 10Ω e L = 15mH. Determine:
a) A expressão da corrente na carga;
b) A corrente média na carga;
c) A potência absorvida pelo resistor;
d) O fator de potência do circuito.
    """

    aula, created = Aula.objects.get_or_create(
        titulo="Aula 6 - Retificador Monofásico Não Controlado de Meia Onda - Carga RL",
        defaults={
            "topicos": "Retificador Monofásico de Meia Onda com Carga RL, Ângulo de Extinção, Cálculos de Tensão e Corrente (Médio, Eficaz) na Carga e no Diodo, Expressão da Corrente de Carga (Regime Permanente e Transitório), Exemplo de Retificador de Meia Onda com Carga RL.",
            "conteudo_detalhado": aula_6_content
        }
    )

    # Conceitos da Aula 6
    Conceito.objects.get_or_create(
        titulo="Retificador Monofásico Não Controlado de Meia Onda com Carga RL",
        defaults={
            "definicao": "Circuito retificador que utiliza um diodo e alimenta uma carga composta por um resistor (R) e um indutor (L) em série. A presença do indutor afeta a forma de onda da corrente, prolongando a condução do diodo além do ponto de cruzamento por zero da tensão.",
            "explicacao_detalhada": "Quando um indutor é adicionado à carga de um retificador de meia onda, a corrente não se torna zero instantaneamente quando a tensão de entrada inverte a polaridade. O indutor armazena energia durante o semiciclo positivo e a libera durante o semiciclo negativo, fazendo com que o diodo conduza por um período maior do que 180 graus. Isso resulta em uma forma de onda de corrente mais suave, mas também pode levar a uma tensão reversa de pico maior no diodo."
        }
    )
    Conceito.objects.get_or_create(
        titulo="Ângulo de Extinção (phi)",
        defaults={
            "definicao": "Ângulo no qual a corrente em um diodo ou SCR se torna zero e o dispositivo desliga, especialmente em circuitos com cargas indutivas.",
            "explicacao_detalhada": "Em circuitos com indutores, a corrente não segue a tensão instantaneamente. O ângulo de extinção (phi) é o ponto no ciclo da forma de onda onde a corrente através do dispositivo semicondutor (diodo ou SCR) finalmente cai a zero, fazendo com que ele desligue. Em retificadores de meia onda com carga RL, o ângulo de extinção é maior que 180 graus devido à energia armazenada no indutor."
        }
    )

    # Fórmulas da Aula 6
    Formula.objects.get_or_create(
        nome="Tensão Média na Carga (Retificador Meia Onda - Carga RL)",
        formula_latex="V_{o_{médio}} = \frac{V_m}{2\pi} \cdot (1 - \cos(\phi))",
        descricao="Tensão média de saída para um retificador monofásico de meia onda com carga RL, onde phi é o ângulo de extinção.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Tensão Eficaz na Carga (Retificador Meia Onda - Carga RL)",
        formula_latex="V_{o_{rms}} = V_m \sqrt{\frac{1}{2\pi} \left( \frac{\phi}{2} - \frac{\sin(2\phi)}{4} \right)}",
        descricao="Tensão eficaz de saída para um retificador monofásico de meia onda com carga RL, onde phi é o ângulo de extinção.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Impedância da Carga RL",
        formula_latex="Z = \sqrt{R^2 + (\omega L)^2}",
        descricao="Impedância total de uma carga RL em série, onde R é a resistência, L é a indutância e omega é a frequência angular.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Ângulo de Fase da Carga RL",
        formula_latex="\theta = \tan^{-1}\left(\frac{\omega L}{R}\right)",
        descricao="Ângulo de fase de uma carga RL em série, onde R é a resistência, L é a indutância e omega é a frequência angular.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Corrente de Carga (Retificador Meia Onda - Carga RL)",
        formula_latex="i_o(\omega t) = \frac{V_m}{Z} \cdot \left( \sin(\omega t - \theta) + \sin(\theta) \cdot e^{-\frac{R}{\omega L} \cdot \omega t} \right)",
        descricao="Expressão da corrente de carga para um retificador monofásico de meia onda com carga RL, considerando os regimes forçado e natural.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Equação para Ângulo de Extinção (Retificador Meia Onda - Carga RL)",
        formula_latex="\sin(\phi - \theta) + \sin(\theta) \cdot e^{-\frac{R}{\omega L} \cdot \phi} = 0",
        descricao="Equação transcendental para determinar o ângulo de extinção (phi) da corrente em um retificador de meia onda com carga RL.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Corrente Média na Carga (Retificador Meia Onda - Carga RL)",
        formula_latex="I_{o_{médio}} = \frac{1}{2\pi} \int_{0}^{\phi} i_o(\omega t) \cdot d(\omega t)",
        descricao="Corrente média na carga para um retificador monofásico de meia onda com carga RL, calculada pela integral da corrente instantânea.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Corrente Eficaz na Carga (Retificador Meia Onda - Carga RL)",
        formula_latex="I_{o_{rms}} = \sqrt{\frac{1}{2\pi} \int_{0}^{\phi} i_o^2(\omega t) \cdot d(\omega t)}",
        descricao="Corrente eficaz na carga para um retificador monofásico de meia onda com carga RL, calculada pela integral do quadrado da corrente instantânea.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Tensão de Pico Reversa no Diodo (Retificador Meia Onda - Carga RL)",
        formula_latex="V_{D_{pico}} = V_m \text{ (para } \pi < \phi \le 3\pi/2 \text{)}",
        descricao="Tensão de pico reversa no diodo para um retificador monofásico de meia onda com carga RL, para um determinado intervalo do ângulo de extinção.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Tensão de Pico Reversa no Diodo (Retificador Meia Onda - Carga RL - Caso 2)",
        formula_latex="V_{D_{pico}} = V_m \cdot \sin(\phi) \text{ (para } 3\pi/2 < \phi \le 2\pi \text{)}",
        descricao="Tensão de pico reversa no diodo para um retificador monofásico de meia onda com carga RL, para outro intervalo do ângulo de extinção.",
        aula_relacionada=aula
    )
    Formula.objects.get_or_create(
        nome="Tensão Eficaz Reversa no Diodo (Retificador Meia Onda - Carga RL)",
        formula_latex="V_{D_{rms}} = \sqrt{\frac{1}{2\pi} \int_{\phi}^{2\pi} V_m^2 \cdot \sin^2(\omega t) \cdot d(\omega t)}",
        descricao="Tensão eficaz reversa no diodo para um retificador monofásico de meia onda com carga RL, calculada pela integral do quadrado da tensão instantânea no período de bloqueio.",
        aula_relacionada=aula
    )

    # Exemplo da Aula 6
    Exemplo.objects.get_or_create(
        titulo="Exemplo de Retificador de Meia Onda - Carga RL",
        descricao="Um retificador monofásico não-controlado de meia onda tem um fonte de 120VRMS em 60Hz e uma carga RL, onde R = 10Ω e L = 15mH. Determine: a) A expressão da corrente na carga; b) A corrente média na carga; c) A potência absorvida pelo resistor; d) O fator de potência do circuito.",
        passos_resolucao="""
(A solução detalhada para este exemplo seria extraída do gabarito e/ou da explicação do professor, incluindo cálculos passo a passo para cada item.)
        """,
        aula_relacionada=aula
    )

def populate_db_with_detailed_content():
    populate_aula_1a()
    populate_aula_1b()
    populate_aula_2()
    populate_aula_3()
    populate_aula_4()
    populate_aula_5()
    populate_aula_6()

    # Adicionar mais funções para popular as outras aulas e exercícios
    # ...

if __name__ == '__main__':
    populate_db_with_detailed_content()
    print("Banco de dados populado com sucesso com conteúdo detalhado!")


