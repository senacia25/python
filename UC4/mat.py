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

import numpy as np
import matplotlib.pyplot as plt

horas_dormidas = np.array([4, 5, 6, 7, 8, 9])
desempenho = np.array([50, 55, 65, 75, 80, 85])

# Cálculo da correlação de Pearson
correlacao = np.corrcoef(horas_dormidas, desempenho)[0, 1]
print(f"Coeficiente de correlação: {correlacao:.2f}")


plt.scatter(horas_dormidas, desempenho, color='red')
plt.plot(horas_dormidas, desempenho, color='blue')
plt.title('Relação entre Horas Dormidas e Desempenho')
plt.xlabel('Horas Dormidas')
plt.ylabel('Desempenho')
plt.grid(True)



plt.show()
