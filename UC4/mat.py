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

#==================
#==================

import numpy as np
from sklearn.linear_model import LinearRegression

# Dados fictícios
x = np.array([1,2,3,4,5]).reshape(-1,1) # variável independentes
y = np.array([2,4,5,4,5]) # variável dependente

# Criar e treinar o modelo
modelo = LinearRegression()
modelo.fit(x, y)

# Coeficiente
a = modelo.coef_[0] # Inclinação
b = modelo.intercept_ #interceptor
print(f"Equação da reta : y = {a:.2f}x + {b:.2f}")

# Previsão
x_novo = np.array([[6]])
y_previsto = modelo.predict(x_novo)
print(f"Para x=6, y previsto é {y_previsto[0]:.2f}")
