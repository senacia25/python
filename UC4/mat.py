# import statistics
# import numpy as np

# dados = [10, 20, 20 ,30, 40, 50]

# print("Média", statistics.mean(dados))
# print("Mediana", statistics.median(dados))
# print("Moda", statistics.mode(dados))
# print(f"Desvio padrão { np.std(dados):.2f}")
# print(f"Variância { np.var(dados):.2f}")

#================
#================

# import matplotlib.pyplot as plt
# from collections import Counter

# dados = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
# frequencia = Counter(dados)

# plt.bar(frequencia.keys(), frequencia.values())
# plt.title("Histograma de dados")
# plt.xlabel("Valor")
# plt.ylabel("frequência")
# plt.show()

#================
#================

# import numpy as np
# import matplotlib.pyplot as plt

# # Valores de x
# x = np.linspace(0.1, 15, 400)  # Começa em 0.1 para evitar log(0) # linspace criar numero automaticos apartir do 0.1 até 5 , 400 determina a quantidade de números criados até o 5

# # Funções
# y_linear = x
# y_polinomial = x**3 - 3*x**2 + 2*x  # exemplo de polinômio cúbico
# y_logaritmica = np.log(x)
# y_exponencial = np.exp(x/2)  # dividir por 2 para não explodir muito rápido

# # Criar gráfico
# plt.figure(figsize=(10,6))

# plt.plot(x, y_linear, label='Linear: y = x', color='blue', linewidth=2)
# plt.plot(x, y_polinomial, label='Polinomial: y = x³ - 3x² + 2x', color='green', linewidth=2)
# plt.plot(x, y_logaritmica, label='Logarítmica: y = log(x)', color='orange', linewidth=2)
# plt.plot(x, y_exponencial, label='Exponencial: y = e^(x/2)', color='red', linewidth=2)

# # Personalização
# plt.title('Comparação de Funções', fontsize=16)
# plt.xlabel('x', fontsize=14)
# plt.ylabel('y', fontsize=14)
# plt.legend(fontsize=12)
# plt.grid(True)
# #plt.ylim(-5, 15)  # Ajustar para melhor visualização
# plt.show()

#================
#================

# import numpy as np

# # x = [1, 2, 3, 4, 5]
# # y = [2, 4, 5, 4-, 5]

# x = np.array ([-1, 0, 1 ])
# #y = np.array ([1, 0, -1]) 
# y = np.array ([1, 0, 1]) #y não é linearmente relacionada com x

# corr = np.corrcoef(x, y)[0, 1]
# print("Correlação de person: ", corr)

#===============
#===============

# import numpy as np
# from sklearn.linear_model import LinearRegression

# # Dados fictícios
# x = np.array([1,2,3,4,5]).reshape(-1,1) # variável independentes
# y = np.array([2,4,5,4,5]) # variável dependente

# # Criar e treinar o modelo
# modelo = LinearRegression()
# modelo.fit(x, y)

# # Coeficiente
# a = modelo.coef_[0] # Inclinação
# b = modelo.intercept_ #interceptor
# print(f"Equação da reta : y = {a:.2f}x + {b:.2f}")

# # Previsão
# x_novo = np.array([[6]])
# y_previsto = modelo.predict(x_novo)
# print(f"Para x=6, y previsto é {y_previsto[0]:.2f}")

#===============
#===============

# import numpy as np
# from scipy.stats import pearsonr

# x = np.random.rand(100)
# y = 2 * x + np.random.normal(0, 0.1, 100)

# correlacao, _ = pearsonr(x, y)
# print("Correlação de Pearson:", correlacao)

#==============
#==============

# import numpy as np

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 5, 4, 5]

# corr = np.corrcoef(x, y)[0, 1]
# print("Correlação de Pearson:", corr)


#================
#================


# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression


# # Exemplo de dados fictícios
# # Altura em metros, Peso em kg
# dados = pd.DataFrame({
#     "altura": [1.60, 1.70, 1.80, 1.90, 1.65, 1.75],
#     "peso":   [55, 65, 80, 95, 60, 78]
# })

# # Cálculo do IMC real
# dados["IMC_real"] = dados["peso"] / (dados["altura"]**2)

# # --------------------------
# # 1) Regressão linear simples com altura e peso
# # --------------------------
# X1 = dados[["peso", "altura"]]  # variáveis explicativas
# y = dados["IMC_real"]

# modelo1 = LinearRegression()
# modelo1.fit(X1, y)

# dados["IMC_pred_simples"] = modelo1.predict(X1)

# # --------------------------
# # 2) Regressão linear com transformação (peso / altura²)
# # --------------------------
# X2 = (dados["peso"] / (dados["altura"]**2)).values.reshape(-1, 1)

# modelo2 = LinearRegression()
# modelo2.fit(X2, y)

# dados["IMC_pred_transformado"] = modelo2.predict(X2)

# # Mostrar resultados
# print(dados)
# print("\nCoeficientes modelo simples:", modelo1.coef_, "Intercepto:", modelo1.intercept_)
# print("Coeficiente modelo transformado:", modelo2.coef_, "Intercepto:", modelo2.intercept_)

#==========
#==========
# # Ver versão
# import sklearn
# print(sklearn.__version__)
#==========
#==========

# # Imports principais (execute primeiro)
# import random
# import math
# from collections import Counter
# import numpy as np
# import matplotlib.pyplot as plt

# # Bibliotecas de ciência de dados/IA
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB, GaussianNB
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import make_classification
# from sklearn.metrics import roc_curve, auc

# # Bibliotecas científicas
# from scipy import stats
# from scipy import integrate

# # Reprodutibilidade
# random.seed(42)
# np.random.seed(42)
# # Solução
# urna = ["vermelha"] * 3 + ["azul"] * 2

# # 1) Teórica
# p_teorica = 3 / 5

# # 2) Simulação
# n = 10_000                                          # outra forma n = 10000
# sorteios = [random.choice(urna) for _ in range(n)]  # outra forma for i in range(n)]
# p_exp = sorteios.count("vermelha") / n

# print(f"Probabilidade teórica (vermelha): {p_teorica:.4f}")
# print(f"Probabilidade experimental (vermelha): {p_exp:.4f}")
# print(f"Erro absoluto: {abs(p_teorica - p_exp):.4f}")

# # Solução
# lados = [1,2,3,4,5,6]
# p_teorica = 3 / 6  # {2,4,6}

# N = 100_000
# rolagens = np.random.choice(lados, size=N, replace=True)
# p_exp = np.isin(rolagens, [2,4,6]).mean()

# print(f"Probabilidade teórica (par): {p_teorica:.4f}")
# print(f"Probabilidade experimental (par): {p_exp:.4f}")
# print(f"Erro absoluto: {abs(p_teorica - p_exp):.4f}")

#====================
#====================

# import numpy as np
# import matplotlib.pyplot as plt

# horas_dormidas = np.array([4, 5, 6, 7, 8, 9])
# desempenho = np.array([50, 55, 65, 75, 80, 85])

# # Cálculo da correlação de Pearson
# correlacao = np.corrcoef(horas_dormidas, desempenho)[0, 1]
# print(f"Coeficiente de correlação: {correlacao:.2f}")


# plt.scatter(horas_dormidas, desempenho, color='red')
# plt.plot(horas_dormidas, desempenho, color='blue')
# plt.title('Relação entre Horas Dormidas e Desempenho')
# plt.xlabel('Horas Dormidas')
# plt.ylabel('Desempenho')
# plt.grid(True) #plt.grid() mesma coisa sem precisar especificar true e pode personalizar como a baixo
# #plt.grid(True, linestyle='aa', color='green', alpha=0.7)
# plt.show()

#====================
#====================

# from scipy import stats
# import numpy as np

# grupo_A = np.random.normal(70, 10, 30)
# grupo_B = np.random.normal(65, 10, 30)

# t_stat, p_val = stats.ttest_ind(grupo_A, grupo_B)
# print("t =", t_stat, "p-valor =", p_val)

#====================
#=====teste t===============

# import numpy as np
# from scipy import stats

# # --- Parte 1 ---
# notas_iniciais = [72, 68, 71, 69, 73, 74, 70, 67, 72, 71]

# media_inicial = np.mean(notas_iniciais)
# desvio_inicial = np.std(notas_iniciais, ddof=1)  # ddof=1 para amostral
# print("Média inicial:", media_inicial)
# print("Desvio padrão inicial:", desvio_inicial)

# # Teste t (H0: média = 70)
# t_stat, p_valor = stats.ttest_1samp(notas_iniciais, popmean=70)
# print("t =", t_stat, "p =", p_valor)

# # --- Parte 2 ---
# notas_novas = [75, 78, 77, 74, 76, 79, 80, 81, 77, 76, 78, 75]

# media_nova = np.mean(notas_novas)
# desvio_novo = np.std(notas_novas, ddof=1)
# print("\nMédia nova:", media_nova)
# print("Desvio padrão novo:", desvio_novo)

# # Teste t (H0: média = 70)
# t_stat2, p_valor2 = stats.ttest_1samp(notas_novas, popmean=70)
# print("t =", t_stat2, "p =", p_valor2)

#====================
#=======teste t =============
#EX
# import numpy as np
# from scipy import stats

# notas_alunos = [82, 76, 88, 91, 69, 73, 85, 79, 90, 77, 84, 80]

# media_inicial = np.mean(notas_alunos)
# desvio_inicial = np.std(notas_alunos, ddof=1)
# print(f"Média inicial: {media_inicial:.5f} \nDesvio padrão inicial: {desvio_inicial:.5f}")

# t_star, p_valor = stats.ttest_1samp(notas_alunos, popmean=75)
# print(f"t = {t_star:.5f}, p = {p_valor:.5f}")

#====================
#====================

# from scipy import stats
# import numpy as np
# antes = np.random.normal(70, 5, 20)
# depois = antes - np.random.normal(2, 2, 20)  # melhoraram em média 2 pontos

# t_stat, p_val = stats.ttest_rel(antes, depois)
# print("t =", t_stat, "p-valor =", p_val)
# diferencas = antes - depois
# print("Média da variação de peso:", np.mean(diferencas))

#====================
#====================

# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(42)

# # Simulando lançamentos de moeda (1 = cara, 0 = coroa)
# n_experimentos = 10000
# lancamentos = np.random.choice([0, 1], size=n_experimentos, p=[0.5, 0.5])

# # Média acumulada
# medias_acumuladas = np.cumsum(lancamentos) / np.arange(1, n_experimentos + 1)

# plt.plot(medias_acumuladas, label="Média acumulada")
# plt.axhline(0.5, color="red", linestyle="--", label="Probabilidade real (0.5)")
# plt.xlabel("Número de lançamentos")
# plt.ylabel("Proporção de caras")
# plt.legend()
# plt.grid(color="orange")
# plt.show()

#====================
#====================

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from scipy import stats

# def estatisticas_descritivas(csv_path):
#     # Carregar dataset
#     df = pd.read_csv(csv_path)
#     print(f"\n📂 Dataset carregado com {df.shape[0]} linhas e {df.shape[1]} colunas.\n")
    
#     # Selecionar apenas colunas numéricas
#     num_cols = df.select_dtypes(include=np.number).columns
    
#     if len(num_cols) == 0:
#         print("⚠️ O dataset não possui colunas numéricas para análise.")
#         return
    
#     resultados = {}
    
#     for col in num_cols:
#         dados = df[col].dropna()  # remover NaN
        
#         estatisticas = {
#             "média": np.mean(dados),
#             "mediana": np.median(dados),
#             "moda": stats.mode(dados, keepdims=True).mode[0],
#             "variância": np.var(dados, ddof=1),  # ddof=1 para variância amostral
#             "desvio padrão": np.std(dados, ddof=1),
#             "assimetria": stats.skew(dados),
#             "curtose": stats.kurtosis(dados)
#         }
#         resultados[col] = estatisticas
        
#         print(f"\n📊 Estatísticas para '{col}':")
#         for k, v in estatisticas.items():
#             print(f"   {k:15}: {v:.4f}")
        
#         # Histogramas
#         plt.figure(figsize=(10,4))
#         plt.subplot(1,2,1)
#         sns.histplot(dados, kde=True, bins=20, color="skyblue")
#         plt.title(f"Histograma - {col}")
        
#         # Boxplot
#         plt.subplot(1,2,2)
#         sns.boxplot(x=dados, color="lightgreen")
#         plt.title(f"Boxplot - {col}")
        
#         plt.tight_layout()
#         plt.show()
    
#     return pd.DataFrame(resultados).T


# # ----------------- EXEMPLO DE USO -----------------
# estatisticas = estatisticas_descritivas("UC4/dataset_exemplo.csv")
# print(estatisticas)

#====================
#====================

# import numpy as np
# import pandas as pd
# from scipy.stats import skew, kurtosis

# # Definir a seed para reprodutibilidade
# np.random.seed(42)

# # Gerar dados normais centrados em 2, com baixa variância
# dados_normais = np.random.normal(loc=2, scale=0.2, size=1000)

# # Gerar outliers positivos com distribuição exponencial (assimetria positiva)
# outliers = np.random.exponential(scale=10, size=20)

# # Combinar os dados
# dados_com_outliers = np.concatenate([dados_normais, outliers])

# # Criar DataFrame
# df = pd.DataFrame({
#     'id': range(1, len(dados_com_outliers) + 1),
#     'valor': dados_com_outliers
# })

# # Calcular skewness e kurtosis
# skew_val = skew(dados_com_outliers)
# kurt_val = kurtosis(dados_com_outliers)

# print("Skewness:", skew_val)
# print("Kurtosis:", kurt_val)

# # Salvar o arquivo CSV
# df.to_csv("UC4/dados_skew_kurtosis.csv", index=False)
# print("Arquivo 'dados_skew_kurtosis.csv' criado com sucesso!")

#====================
#====================

# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# # Carrega o arquivo CSV gerado anteriormente
# df = pd.read_csv('UC4/dados_skew_kurtosis.csv')

# # Tamanho da figura
# plt.figure(figsize=(14, 6))

# # Histograma
# plt.subplot(1, 2, 1)
# sns.histplot(df['valor'], bins=50, kde=True, color='skyblue')
# plt.title('Histograma com KDE (Distribuição dos Dados)')
# plt.xlabel('Valor')
# plt.ylabel('Frequência')

# # Boxplot
# plt.subplot(1, 2, 2)
# sns.boxplot(x=df['valor'], color='lightgreen')
# plt.title('Boxplot dos Dados')

# # Mostrar os gráficos
# plt.tight_layout()
# plt.show()

#====================
#====================

#EX:

# import numpy as np 
# import matplotlib.pyplot as plt

# # Garantir reprodutibilidade
# np.random.seed(42)

# # Parâmetro da distribuição exponencial
# lambda_param = 2
# valor_esperado = 1 / lambda_param  # E[X] = 1/λ = 0.5

# # Número total de experimentos (amostras)
# n_experimentos = 10000

# # Gerar amostras da distribuição exponencial
# # scale = 1/λ porque np.random.exponential usa o parâmetro de escala (θ = 1/λ)
# amostras = np.random.exponential(scale=1/lambda_param, size=n_experimentos)

# # Calcular a média acumulada (média amostral a cada novo ponto)
# medias_acumuladas = np.cumsum(amostras) / np.arange(1, n_experimentos + 1)

# # Plotando o gráfico
# plt.figure(figsize=(10, 5))
# plt.plot(medias_acumuladas, label="Média acumulada")
# plt.axhline(valor_esperado, color="red", linestyle="--", label=f"Valor esperado (E[X] = {valor_esperado})")
# plt.xlabel("Número de amostras")
# plt.ylabel("Média acumulada")
# plt.title("Lei dos Grandes Números - Distribuição Exponencial (λ = 2)")
# plt.legend()
# plt.grid(True, color="purple", linestyle="--", alpha=0.9)
# plt.tight_layout()  # garante que nada do grafico fique cortado
# plt.show()

# # O QUE MUDA É O PLT.AXHLINE, ABAIXO 1 SOBRE LAMBDA O OUTRO FOI CRIADO UMA VARIAVEL, DÁ NA MESMA
# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(42)

# # Parâmetros
# lambda_ = 2
# n_experimentos = 10000

# # Gerando amostras da distribuição exponencial com lambda=2
# # Escala da exponencial é 1/lambda
# amostras = np.random.exponential(scale=1/lambda_, size=n_experimentos)

# # Média acumulada
# medias_acumuladas = np.cumsum(amostras) / np.arange(1, n_experimentos + 1)

# # Plotando
# plt.figure(figsize=(10, 5))
# plt.plot(medias_acumuladas, label="Média acumulada")
# plt.axhline(1/lambda_, color="red", linestyle="--", label="Valor esperado (0.5)")
# plt.xlabel("Número de amostras")
# plt.ylabel("Média acumulada")
# plt.title("Lei dos Grandes Números para Distribuição Exponencial (λ = 2)")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()  # garante que nada do grafico fique cortado
# plt.show()

#====================
#====================

####nova print(\n = pula linha , \t = dá espaço )

#EX:

# import numpy as np
# from collections import Counter

# np.random.seed(42)

# # Espaço amostral dos lançamentos
# resultados = ['B', 'C']

# # Número de experimentos
# n_experimentos = 10000

# # Simulando 10.000 lançamentos de 2 moedas
# moeda1 = np.random.choice(resultados, size=n_experimentos)
# moeda2 = np.random.choice(resultados, size=n_experimentos)

# # Combinando os resultados em tuplas (moeda1, moeda2)
# #lancamentos = list(zip(moeda1, moeda2))
# lancamentos = [(str(m1), str(m2)) for m1, m2 in zip(moeda1, moeda2)]  # aparece mais simples ao executar


# # Contando as frequências empíricas
# contagem = Counter(lancamentos)

# # Frequência empírica (proporção)
# frequencias_empiricas = {k: v / n_experimentos for k, v in contagem.items()}

# # Probabilidade teórica (uniforme)
# prob_teorica = 1 / 4

# print("Frequências empíricas:")
# for resultado, freq in frequencias_empiricas.items():
#     print(f"{resultado}: {freq:.4f} (teórica: {prob_teorica:.4f})")


# # # outra forma

# import random
# from collections import Counter

# # Definindo o espaço amostral
# espaco_amostral = [('B', 'B'), ('C', 'C'), ('B', 'C'), ('C', 'B')]

# # Probabilidade teórica para cada evento (moeda justa)
# prob_teorica = 1 / 4

# # Simulando 10.000 lançamentos de dois lançamentos de moeda
# resultados = []
# for _ in range(10000):
#     lancamento1 = random.choice(['B', 'C'])
#     lancamento2 = random.choice(['B', 'C'])
#     resultados.append((lancamento1, lancamento2))

# # Contando as frequências empíricas
# frequencias_empiricas = Counter(resultados)

# # Exibindo resultados
# print("Evento\tFreq. Empírica\tProb. Teórica")
# for evento in espaco_amostral:
#     freq = frequencias_empiricas[evento] / 10000
#     print(f"{evento}\t{freq:.4f}\t\t{prob_teorica:.4f}")


# #forma prof

# import random
# from collections import Counter

# espaco_amostral = [(a,b) for a in ['B','C'] for b in ['B','C']]
# print("Espacço amostral", espaco_amostral)

# resultado = [(random.choice(['B','C']), random.choice(['B','C'])) for _ in range(10000)]
# #print(resultado)
# frequencia = Counter(resultado)
# print(frequencia)


#EX:
#dica pares =  
# pares = [x for x in range(1,7) if x % 2 == 0]
#random.randint(1,6) 

import random

lancamentos = 10000
pares = 0

for _ in range(lancamentos):
    if random.randint(1, 6) % 2 == 0:
        pares += 1

prob_simulada = pares / lancamentos

print(f"Probabilidade simulada: {prob_simulada}")


#form prof

pares = [x for x in range(1,7) if x % 2 == 0]
prob_teorica = len(pares) / 6

simulacao = [random.randint(1,6) for _ in range(10000)]
freq_par = sum(1 for x in simulacao if x % 2 == 0) / len(simulacao)

print(f"Probalidade teórica: {prob_teorica}, Simulada: {freq_par}")