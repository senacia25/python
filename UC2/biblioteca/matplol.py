#MATPLOTLIB
# import matplotlib.pyplot as plt
# import numpy as np

# #Gráfico de linha
# x = [1,2,4,5,6]
# y = [9,8,4,7,6]

# plt.plot(x,y)
# plt.title("exemplo de linha")
# plt.xlabel("Eixo x")
# plt.ylabel("Eixo y")
# plt.show()

# #Gráfico de BARRA
# categoria = ["A", "B", "c"]
# valores = [10,2,30]

# plt.bar(categoria, valores)
# plt.title("Barras")
# plt.show()

# #Gráfico de PIZZA
# plt.pie(valores, labels=categoria, autopct="%1.1f%%")
# plt.title("Pizza")
# plt.show()

# #Histograma
# dados = np.random.randn(1000)
# plt.hist(dados, bins=30)
# plt.title("Histograma")
# plt.show()

# #Dispersão
# x2 = np.random.rand(50)
# y = x2 + np.random.randn(50) * 0.1

# plt.scatter(x2,y)
# plt.title("Dispersão")
# plt.show()


#=====
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0,10,100)

# #usando método de seno do numpy
# y_line = np.sin(x)

# categoria = ["Ação","Comédia","Drama","Terror"]

# valores = [20,40,50,20]

# #Dados por gráfico de dispersão
# x_scatter = np.random.rand(50)

# y_scatter = x_scatter + np.random.randn(50) * 0.1

# #Histograma
# hist_data = np.random.randn(1000)

# fig, axs = plt.subplots(2,2, figsize=(10,8))

# axs[0,0].plot(x,y_line, color="blue", linestyle="--", label="sin(x)")
# axs[0,0].set_title("Gráfico de linha")
# axs[0,0].legend()

# axs[0,1].bar(categoria, valores, color=["green","red","blue","purple"])
# axs[0,1].set_title("Gráfico de barras")

# axs[1,0].scatter(x_scatter, y_scatter, alpha=0.6, color="red")
# axs[1,0].set_title("Gráfico de dispersão")

# axs[1,1].hist(hist_data, bins=30, color="blue", edgecolor="black")
# axs[1,1].set_title("Histograma")

# fig.tight_layout()

# plt.show()


#=====

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Filme":["A","b","C","D","E"],
    "Nota":[8.5,9.5,7,6.8,5],
    "Receita":[120,80,150,50,60]
})
#Gráfivo de Barras com colunas do Dataframe
plt.bar(df["Filme"],df["Nota"])
plt.title("Nota do filme")
plt.ylabel("Nota")
plt.show()