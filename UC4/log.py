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

# import random
# from collections import Counter

# resultados = []
# bola = ["R", "R", "R", "B", "B"]
# for _ in range(10000):
#     lancamento1 = random.choice(['B', 'C'])
#     lancamento2 = random.choice(['B', 'C'])
#     resultados.append((lancamento1, lancamento2))
# frequencias_empiricas = Counter(resultados)


# #======outra

# import random
# from collections import Counter

# urna = ['R', 'R', 'R', 'B', 'B']

# simulacoes = [random.choice(urna) for _ in range(10000)]
# frequencia = Counter(simulacoes)

# print("Frequência dos resultados:")
# print(frequencia)

# prob_R = frequencia['R'] / 10000
# prob_B = frequencia['B'] / 10000

# print(f"\nProbabilidade estimada de sair 'R': {prob_R:.4f}")
# print(f"Probabilidade estimada de sair 'B': {prob_B:.4f}")

#================ tecnica/simulação monte carlo
#================

# import numpy as np

# bolas = ['R','R','R','B','B']
# n_sim = 10000
# resultados = []

# for _ in range(n_sim):
#     np.random.shuffle(bolas)
#     sorteio = bolas[0]
#     resultados.append(sorteio)

# resultados = np.array(resultados)
# A = resultados == 'R'
# B = np.arange(n_sim) % 2 == 1

# P_sim = np.mean(A | B) #|= ou, & e
# print(f"Exercício - Probabilidade (bola vermelha ou índice ímpar) ~ {P_sim:.2f}")

#================
#================

# import numpy as np

# bolas = ['R','R','R','B','B']
# n_sim = 10000
# resultados = []

# for _ in range(n_sim):
#     np.random.shuffle(bolas)
#     sorteio = bolas[0]
#     resultados.append(sorteio)

# resultados = np.array(resultados)
# A = resultados == 'B'
# B = np.arange(n_sim) % 5 == 1

# P_sim = np.mean(A & B) 
# print(f"Exercício - Probabilidade (bola vermelha ou índice ímpar) ~ {P_sim:.2f}")

#================
#================

# import numpy as np

# bolas = ['R','R','R','B','B']
# n_sim = 10000

# sorteio = np.random.choice(bolas, size=(n_sim, 3), replace=True)

# A = np.all(sorteio == 'R', axis=1) #axis=1 = verifica se todos sao true

# P_sim = np.mean(A) 
# print(f"Exercício - Probabilidade (bola vermelha ou índice ímpar) ~ {P_sim:.2f}")

#================
# | Função                    | O que faz?                                                                                           |
# | ------------------------- | ---------------------------------------------------------------------------------------------------- |
# | `random.shuffle(lista)`   | Embaralha toda a lista original.                                                                     |
# | `random.sample(lista, n)` | Retorna uma nova lista com `n` itens aleatórios da original, **sem repetição**. A original não muda. |

#================
#================

# import random
# import numpy as np
# import statistics

# # numeros = [random.randint(1, 50)for _ in range(10)] # pode repetir alguns numeros que já sairam
# # print("Lista de números:", numeros)

# numeros = random.sample(range(1, 51), 25) # nao repeti nem um numero a sequencia
# print("Lista de números:", numeros)

# # numeros = list(range(1, 51), 10)
# # print(numeros)

# media = np.mean(numeros)
# mediana = np.median(numeros)
# moda = statistics.mode(numeros)
# # moda = statistics.multimode(numeros)

# # try:
# #     moda = statistics.mode(numeros)
# # except statistics.StatisticsError:
# #     moda = "Sem moda (todos os valores são únicos)"

# print(f"Média: {media}")
# print(f"Mediana: {mediana}")
# print(f"Moda: {moda}")

#================
#======EX==========

# import numpy as np

# n = [12, 15, 12, 18, 20, 15, 22, 19, 15, 10]

# print("Desvio padrão", np.std(n))
# print("Variância", np.var(n))
# print("media", np.mean(n))
# print("mediana", np.median(n))

##outro
# # Cálculo da variância e desvio padrão
# variancia = np.var(n, ddof=0)  # Populacional
# desvio_padrao = np.std(n, ddof=0)  # Populacional

# print("Lista de números:", n)
# print(f"Variância: {variancia}")
# print(f"Desvio padrão: {desvio_padrao}")

#================
#======EX==========

# import matplotlib.pyplot as plt
# from collections import Counter

# n = [12, 15, 12, 18, 20, 15, 22, 19, 15, 10]
# frequencia = dict(Counter(n))
# print(frequencia)

# # f = Counter(n)
# # print(f)


# # Dados para o gráfico
# valores = list(frequencia.keys())
# ocorrencias = list(frequencia.values())

# # Criar histograma
# #plt.hist(n, bins=range(min(n), max(n)+2), edgecolor="black") # outra forma
# plt.bar(valores, ocorrencias, color='red', edgecolor='black')
# plt.xlabel('Números')
# plt.ylabel('Frequência')
# plt.title('Histograma de Frequência dos Números')
# plt.grid(axis='y',color='black', alpha=0.7)
# plt.show()

#================
#================

# import numpy as np

# altura = [160, 165, 170, 175, 180, 185, 160, 170, 175, 180]
# peso = [55,  60,  65,  70,  75,  80,  58,  68,  72,  77]

# corr = np.corrcoef(altura, peso)[0, 1]
# print(f"Coeficiente de correlação de Pearson: {corr:.2f}")

#================
#=======percentil quartil=========

# import numpy as np

# numeros = [12, 15, 12, 18, 20, 15, 22, 19, 15, 10]

# q1 = np.percentile(numeros, 25) 
# q2 = np.percentile(numeros, 50) 
# q3 = np.percentile(numeros, 75) 

# print("25%:", q1)
# print("50%:", q2)
# print("75%:", q3)

## só pra testar # Filtra os valores menores ou iguais a cada percentil
## abaixo_q1 = [n for n in numeros if n <= q1]
## abaixo_q2 = [n for n in numeros if n <= q2]
## abaixo_q3 = [n for n in numeros if n <= q3]

## # Mostra os resultados
## print("25% (Q1):", q1, "-> Números:", abaixo_q1)
## print("50% (Q2):", q2, "-> Números:", abaixo_q2)
## print("75% (Q3):", q3, "-> Números:", abaixo_q3)

#================
#================

# import numpy as np
# import matplotlib.pyplot as plt
# dados = [10, 12, 12, 15, 18, 20, 22, 100,]

# # 1. Média
# media = np.mean(dados)

# # 2. Desvio padrão (padrão populacional)
# desvio_padrao = np.std(dados)

# # 3. Limites para detecção de outliers (> 2 desvios da média)
# limite_inferior = media - 2 * desvio_padrao
# limite_superior = media + 2 * desvio_padrao

# # 4. Detectar valores fora desses limites
# outliers = [x for x in dados if x < limite_inferior or x > limite_superior] # x for x dados= pecorre a lista

# #jeito prof

# outliers1 = [x for x in dados if abs(x - media) > 2 * desvio_padrao] #abs = pega o valor absoluto, ignora se a diferença é positivva ou negativa

# # 5. Exibir resultados
# print("Média:", media)
# print(f"Desvio padrão: {desvio_padrao:.2f}")
# print(f"Limite inferior: {limite_inferior:.2f}")
# print(f"Limite superior: {limite_superior:.2f}")
# print("Outliers (> 2 desvios da média):", outliers)
# print("jeito prof: não precisa fazer parte 2 e 3\nOutliers (> 2 desvios da média):", outliers1)

# plt.boxplot(dados, vert=False)
# plt.title("Boxplot dos dados com outlier")
# plt.xlabel("Valores")
# plt.grid()
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# # Dados
# dados = [10, 12, 12, 15, 18, 20, 22, 100]

# # 1. Média
# media = np.mean(dados)

# # 2. Desvio padrão (populacional)
# desvio_padrao = np.std(dados)

# # 3. Limites para detecção de outliers (> 2 desvios da média)
# limite_inferior = media - 2 * desvio_padrao
# limite_superior = media + 2 * desvio_padrao

# # 4. Detectar outliers
# outliers = [x for x in dados if x < limite_inferior or x > limite_superior]

# # 5. Exibir resultados no console
# print("Média:", media)
# print(f"Desvio padrão: {desvio_padrao:.2f}")
# print(f"Limite inferior: {limite_inferior:.2f}")
# print(f"Limite superior: {limite_superior:.2f}")
# print("Outliers (> 2 desvios da média):", outliers)

# # 6. Gráfico
# plt.figure(figsize=(10, 5))
# plt.plot(dados, 'bo-', label='Dados')
# plt.axhline(media, color='green', linestyle='--', label='Média')
# plt.axhline(limite_inferior, color='red', linestyle='--', label='Limite Inferior')
# plt.axhline(limite_superior, color='red', linestyle='--', label='Limite Superior')

# # Destacar os outliers no gráfico
# for i, valor in enumerate(dados):
#     if valor in outliers:
#         plt.plot(i, valor, 'ro', markersize=10, label='Outlier' if 'Outlier' not in plt.gca().get_legend_handles_labels()[1] else "")

# plt.title('Detecção de Outliers (> 2 desvios da média)')
# plt.xlabel('Índice')
# plt.ylabel('Valor')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

#================
#================

# import numpy as np
# import matplotlib.pyplot as plt

# # Gerar 100 números aleatórios com distribuição normal (média=50, desvio padrão=10)
# dados = np.random.normal(loc=50, scale=10, size=100) #loc: é a média da distribuição normal/ scale: é o desvio padrão/ size: é o número de elementos que você quer gerar.

# # Plotar o histograma
# plt.figure(figsize=(8, 5), facecolor='lightblue')
# plt.gca().set_facecolor('yellow')
# plt.hist(dados, bins=10, color='purple', edgecolor='blue')
# plt.title('Histograma de Dados com Distribuição Normal')
# plt.xlabel('Valor')
# plt.ylabel('Frequência')
# plt.grid(True, color='green')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# # Gerar dados
# dados = np.random.normal(loc=50, scale=10, size=100)

# # Criar figura e eixos
# fig, ax = plt.subplots(figsize=(8, 5))

# # Alterar cor de fundo da área do gráfico (atrás dos bins)
# ax.set_facecolor('pink')  # <- AQUI você muda o fundo atrás dos bins

# # Plotar histograma
# ax.hist(dados, bins=10, color='skyblue', edgecolor='black')

# # Títulos e rótulos
# ax.set_title('Histograma com Cor de Fundo Personalizada')
# ax.set_xlabel('Valor')
# ax.set_ylabel('Frequência')

# # Grade
# ax.grid(True)

# # Exibir gráfico
# plt.show()

#================
#================

# import numpy as np
# import pandas as pd
# temperaturas = np.random.randint(20, 35, size=20) #(início, fim, size=n) início: valor mínimo (inclusive),fim: valor máximo (exclusivo), size=n: quantidade de números que você quer gerar
# df_temp = pd.DataFrame(temperaturas, columns=['Temperatura'])
# df_temp['Media_Movel'] = df_temp['Temperatura'].rolling(window=3).mean()
# print(df_temp)

#================
#================

# import pandas as pd

# serie = pd.Series([10,20,5,30])
# print(serie)

# dados = {
#     'Nome':['Ana', 'Bruno', 'Carlos'],
#     'Idade':[25,30,22],
#     'Cidade':['SP', 'RJ', 'PR']
# }
# df = pd.DataFrame(dados)
# print(df)

#================
#================

# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# dados = np.random.normal(loc=50, scale=10, size=100)

# sns.histplot(dados, kde=True, bins=10, color='skyblue')#,  stat='density') # mudar a cor do kde
# # sns.kdeplot(dados, color='red', linewidth=2) # mudar a cor do kde
# plt.title('Histograma com Densidade')
# plt.show()

#================
#================

# import pandas as pd

# dados = {
#     'Nome':['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
#     'Idade':[25,30,22,65,45],
#     'Salário':[1252,2569,2548,3694,12578],
#     'Departamento':['TI','RE','TI','FINANCEIRO','ADM']
# }
# df = pd.DataFrame(dados)
# print(df.head())
# print(df.describe())
# print(df[df['Salário'] > 2000])
# print(df.groupby('Departamento') ['Salário'].mean())

#================
#================

#nao fecha o grafico
# plt.figure
# plt.show(block=False)
#precisa do close se nao, nao permanece aberto
# input("Pressione Enter para fechar tudo...") 
# plt.close('all') 

# import matplotlib.pyplot as plt 
# import numpy as np 

# x = np.linspace(0, 10, 100) 

# # Primeiro gráfico 

# plt.figure() 
# plt.plot(x, np.sin(x)) 
# plt.title("Seno") 
# plt.show(block=False)  # NÃO bloqueia o código, janela fica aberta 

# # Segundo gráfico 

# plt.figure() 
# plt.plot(x, np.cos(x)) 
# plt.title("Cosseno") 
# plt.show(block=False) 

# # Terceiro gráfico 

# plt.figure() 
# plt.plot(x, np.tan(x)) 
# plt.ylim(-10, 10) 
# plt.title("Tangente") 
# plt.show(block=False) 

# input("Pressione Enter para fechar tudo...") 
# plt.close('all') 

#================
#================

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# dados = {
#     'Nome':['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
#     'Idade':[25,30,22,65,45],
#     'Salário':[1252,2569,2548,3694,12578],
#     'Departamento':['TI','RE','TI','FINANCEIRO','ADM']
# }
# df = pd.DataFrame(dados)

# plt.figure() 
# sns.scatterplot(x="Idade", y= "Salário", hue="Departamento", data=df)
# plt.title("Idade x Salário")
# plt.show(block=False)

# #Martiz de correlação
# correlacao = df.corr(numeric_only=True)
# print("Correlação entre variáveis: ")
# print(correlacao)

# #heatmap para visualização

# plt.figure() 
# sns.heatmap(correlacao, annot=True, cmap="coolwarm")
# plt.title("Mapa de correlação")
# plt.show(block=False)

# plt.figure(figsize=(8,6))
# sns.violinplot(x="Departamento", y="Salário", data=df)
# plt.title("Distribuição de salário por departamento")
# plt.show(block=False)

# input("Pressione Enter para fechar tudo...") 
# plt.close('all') 