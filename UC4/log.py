# import random

# baralho = ['A_copas','2_copas','3_copas','4_copas','5_copas','6_copas','7_copas','8_copas','9_copas','10_copas','J_copas','Q_copas','K_copas'] + \
#           ['A_ouros','2_ouros','3_ouros','4_ouros','5_ouros','6_ouros','7_ouros','8_ouros','9_ouros','10_ouros','J_ouros','Q_ouros','K_ouros'] + \
#           ['A_paus','2_paus','3_paus','4_paus','5_paus','6_paus','7_paus','8_paus','9_paus','10_paus','J_paus','Q_paus','K_paus'] + \
#           ['A_espadas','2_espadas','3_espadas','4_espadas','5_espadas','6_espadas','7_espadas','8_espadas','9_espadas','10_espadas','J_espadas','Q_espadas','K_espadas']

# simulacoes = [random.choice(baralho) for _ in range(10000)]
# cartas_copas = [carta for carta in simulacoes if "copas" in carta]

# prob = len(cartas_copas) / len(simulacoes)
# print("A probabilidade é:", prob)

#outra forma

# import random

# # Constantes
# NAIPES = ['copas', 'ouros', 'paus', 'espadas']
# VALORES = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']
# NUM_SIMULACOES = 10_000

# # Função para criar o baralho
# def criar_baralho():
#     return [f"{valor}_{naipe}" for naipe in NAIPES for valor in VALORES]

# # Função para simular sorteios
# def simular_sorteios(baralho, n=10000):
#     return [random.choice(baralho) for _ in range(n)]

# # Função para calcular a probabilidade de um naipe específico
# def calcular_probabilidade(simulacoes, naipe):
#     return sum(1 for carta in simulacoes if carta.endswith(naipe)) / len(simulacoes) #endswith pega a ultima str

# # Execução
# baralho = criar_baralho()
# simulacoes = simular_sorteios(baralho, NUM_SIMULACOES)
# prob = calcular_probabilidade(simulacoes, 'copas')

# print(f"A probabilidade de sair copas é: {prob:.4f}{baralho}")

#================
#================

# import random

# baralho = ['A_copas','2_copas','3_copas','4_copas','5_copas','6_copas','7_copas','8_copas','9_copas','10_copas','J_copas','Q_copas','K_copas'] + \
#           ['A_ouros','2_ouros','3_ouros','4_ouros','5_ouros','6_ouros','7_ouros','8_ouros','9_ouros','10_ouros','J_ouros','Q_ouros','K_ouros'] + \
#           ['A_paus','2_paus','3_paus','4_paus','5_paus','6_paus','7_paus','8_paus','9_paus','10_paus','J_paus','Q_paus','K_paus'] + \
#           ['A_espadas','2_espadas','3_espadas','4_espadas','5_espadas','6_espadas','7_espadas','8_espadas','9_espadas','10_espadas','J_espadas','Q_espadas','K_espadas']

# simulacoes = [random.choice(baralho) for _ in range(10000)]
# selecao = {"3_copas", "4_copas", "5_copas"}
# cartas_sel = [carta for carta in simulacoes if carta in selecao] # ou colocar direto ...simulacoes if ("3_copas" "4_copas" "5_copas")

# prob = len(cartas_sel) / len(simulacoes)
# print("A probabilidade é:", prob)

#================
#================

# import random

# baralho = ['A_copas','2_copas','3_copas','4_copas','5_copas','6_copas','7_copas','8_copas','9_copas','10_copas','J_copas','Q_copas','K_copas'] + \
#           ['A_ouros','2_ouros','3_ouros','4_ouros','5_ouros','6_ouros','7_ouros','8_ouros','9_ouros','10_ouros','J_ouros','Q_ouros','K_ouros'] + \
#           ['A_paus','2_paus','3_paus','4_paus','5_paus','6_paus','7_paus','8_paus','9_paus','10_paus','J_paus','Q_paus','K_paus'] + \
#           ['A_espadas','2_espadas','3_espadas','4_espadas','5_espadas','6_espadas','7_espadas','8_espadas','9_espadas','10_espadas','J_espadas','Q_espadas','K_espadas']

# simulacoes = [random.choice(baralho) for _ in range(10000)]
# cartas_sel = [carta for carta in simulacoes if carta.startswith("8_") or carta.startswith("9_")] #startswith pega a primeira str
# prob = len(cartas_sel) / len(simulacoes)
# print("A probabilidade é:", prob)

# #OUTRO JEITO
# #selecao = {'8_copas', '9_copas', '8_ouros', '9_ouros', '8_paus', '9_paus', '8_espadas', '9_espadas'}
# #cartas_sel = [carta for carta in simulacoes if carta in selecao]

#================
#================

# import random

# pares = [x for x in range(1,7) if x % 2 == 0 or x == 5] 
# prob_teorica = len(pares) / 6 

# print(f"Probalidade: {prob_teorica}")

#outra forma

# a = set(x for x in range(1,7) if x % 2 == 0) # set conjunto
# b = set(x for x in range(1,7) if x > 4)
# prob_teorica = len(a.union(b)) / 6 
# print(prob_teorica)

#================
#================

import random

resultados = []
bola = ["R", "R", "R", "B", "B"]
for _ in range(10000):
    lancamento1 = random.choice(['B', 'C'])
    lancamento2 = random.choice(['B', 'C'])
    resultados.append((lancamento1, lancamento2))
frequencias_empiricas = Counter(resultados)


#======outra

import random
from collections import Counter

urna = ['R', 'R', 'R', 'B', 'B']

simulacoes = [random.choice(urna) for _ in range(10000)]
frequencia = Counter(simulacoes)

print("Frequência dos resultados:")
print(frequencia)

prob_R = frequencia['R'] / 10000
prob_B = frequencia['B'] / 10000

print(f"\nProbabilidade estimada de sair 'R': {prob_R:.4f}")
print(f"Probabilidade estimada de sair 'B': {prob_B:.4f}")
