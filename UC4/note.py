
# print("Tudo certo ✔️")
# print("Deu erro ❌")
# strip().uppper() # strip tira espaço e upper tanto faz se escreve em maiusculo ou minusculo

# print("ok", "\u2714") #sinal de certo

# import time
# time.sleep(1)  #pausa por 1 ou mais segundos antes do codigo continuar

# # Importando bibliotecas
# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA
# import numpy as np

# # 1. Simulando 100 vetores de embeddings faciais com 128 dimensões
# X = np.random.rand(100, 128)

# # 2. Criando rótulos para representar 5 pessoas diferentes
# y = np.random.randint(0, 5, 100)
# # Cada número em y representa uma pessoa (0 a 4)

# # 3. Reduzindo os embeddings de 128 para 2 dimensões com PCA
# pca = PCA(n_components=2)
# X_pca = pca.fit_transform(X)

# # 4. Visualizando os embeddings no espaço 2D com cores por pessoa
# plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='rainbow')
# plt.title("Agrupamento de Embeddings Faciais")
# plt.xlabel("Componente Principal 1")
# plt.ylabel("Componente Principal 2")
# plt.show()



# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA
# import numpy as np

# # 1. Simulando embeddings faciais: 100 vetores de 128 dimensões
# X = np.random.rand(100, 128)  # Dados simulados (100 rostos, 128 características cada)

# # 2. Criando rótulos para 5 pessoas diferentes (0 a 4)
# y = np.random.randint(0, 5, 100)

# # 3. Reduzindo a dimensionalidade dos embeddings de 128 para 2 com PCA
# pca = PCA(n_components=2)
# X_pca = pca.fit_transform(X)

# # 4. Criando o gráfico de dispersão (scatter plot)
# plt.figure(figsize=(10, 7))
# scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='rainbow', alpha=0.7)

# # 5. Título e legendas dos eixos
# plt.title("Agrupamento de Embeddings Faciais após Redução com PCA", fontsize=16)
# plt.xlabel("Componente Principal 1", fontsize=14)
# plt.ylabel("Componente Principal 2", fontsize=14)

# # 6. Criando a legenda para as 5 pessoas diferentes
# # Para isso, pegamos as cores únicas usadas no scatter
# handles, labels = scatter.legend_elements()
# labels = [f'Pessoa {i}' for i in range(5)]
# plt.legend(handles, labels, title="Classes (Pessoas)", fontsize=12, title_fontsize=13)

# # 7. Mostrar o gráfico
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.show()

