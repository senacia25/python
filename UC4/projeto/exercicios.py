#===EX.1
t = 12 
prob_vermelha = 5 / t 
prob_com_repos = prob_vermelha * prob_vermelha
p_sem_repos = (5 - 1) / (t - 1) 
prob_sem_repos = prob_vermelha * p_sem_repos

print(f"\nProbabilidade de tirar vermelha: {prob_vermelha:3f} ou {prob_vermelha:.2%} ")
print(f"Probabilidade de sair duas vermelhas na sequência COM reposição: {prob_com_repos:.3f} ou ({prob_com_repos:.2%}) ")
print(f"Probabilidade de sair duas vermelhas na sequência SEM reposição: {prob_sem_repos:.3f} ou ({prob_sem_repos:.2%}) ")


#===EX.2
d = 6
prob_dados = 3 / d
print(f"\nA probabilidade de sair um número maior que 3 ao lançar um dado de 6 lados é: {prob_dados} ou ({prob_dados:.2%})") # igual :.2f ou 


#===EX.3
m = 4
prob_moeda = 2 / m
print(f"\nA probabilidade de sair exatamente uma cara ao lançar duas moedas é: {prob_moeda} ou ({prob_moeda:.2%})")


#===EX.4
prob_verde = 2 / (5 - 1)
print(f"\nProbabilidade da próxima ser verde dado que a primeira foi vermelha: {prob_verde:.2f} ({prob_verde:.2%})")


#===EX.5
import pandas as pd

dados = pd.Series([10, 15, 20, 20, 25, 30, 35])

media = dados.mean()
mediana = dados.median()
moda = dados.mode()

print("Média:", media)
print("Mediana:", mediana)
print("Moda:", list(moda))  # Pode ter mais de uma moda


#===EX.6
dados = pd.Series([2, 4, 4, 4, 5, 5, 7, 9])

variancia = dados.var()
desvio_padrao = dados.std()

print("Variância:", variancia)
print("Desvio padrão:", desvio_padrao)


#===EX.7
dados = pd.Series([5, 7, 8, 5, 10, 12, 15])

media = dados.mean()
mediana = dados.median()
minimo = dados.min()
maximo = dados.max()
amplitude = maximo - minimo

print("Média:", media)
print("Mediana:", mediana)
print("Valor mínimo:", minimo)
print("Valor máximo:", maximo)
print("Amplitude:", amplitude)


#===EX.8
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 100)
y = np.sin(x) + np.log(x)

plt.plot(x, y)
plt.title("y = sin(x) + log(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()


#===EX.9
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 6])

modelo = LinearRegression()
modelo.fit(X, y)

coef_angular = modelo.coef_[0]
intercepto = modelo.intercept_

print("Coeficiente angular (inclinação):", coef_angular)
print("Interpretação: A cada hora de estudo, a nota aumenta em média", round(coef_angular, 2))


#===EX.10
X = np.array([50, 60, 70, 80, 90]).reshape(-1, 1)
y = np.array([150, 200, 210, 240, 280])

modelo = LinearRegression()
modelo.fit(X, y)

preco_estimado = modelo.predict([[100]])[0]

print("Coeficiente angular:", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)
print("Preço estimado para 100 m²:", round(preco_estimado, 2), "mil reais")


#===EX.11
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(42)
dados = np.random.normal(loc=60, scale=15, size=1000)

# Matplotlib
plt.hist(dados, bins=30, edgecolor='black')
plt.title("Histograma com Matplotlib")
plt.xlabel("Valor")
plt.ylabel("Frequência")
plt.show()

# Seaborn
sns.histplot(dados, kde=True, bins=30)
plt.title("Histograma com Seaborn")
plt.xlabel("Valor")
plt.ylabel("Frequência")
plt.show()


#===EX.12
import seaborn as sns
import pandas as pd

dados = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 4, 5, 4, 6]
})

sns.scatterplot(data=dados, x='X', y='Y')
plt.title("Gráfico de Dispersão com Seaborn")
plt.grid(True)
plt.show()


#===EX.13
dados = [7, 8, 5, 6, 12, 14, 15, 8, 9, 10]

sns.boxplot(data=dados)
plt.title("Boxplot com Seaborn")
plt.xlabel("Valores")
plt.show()


