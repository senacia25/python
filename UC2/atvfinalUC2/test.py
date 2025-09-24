# from collections import Counter

# # Lista dos resultados dos últimos 27 concursos
# resultados_27_concursos = [
#     [1, 5, 6, 8, 9, 10, 12, 13, 15, 16, 18, 19, 23, 24, 25],
#     [1, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 17, 21, 22, 24],
#     [2, 3, 5, 6, 8, 12, 15, 16, 17, 18, 20, 21, 23, 24, 25],
#     [3, 5, 6, 7, 8, 10, 12, 15, 16, 17, 19, 20, 23, 24, 25],
#     [1, 3, 4, 5, 6, 11, 14, 15, 18, 20, 21, 22, 23, 24, 25],
#     [1, 4, 6, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 25],
#     [2, 3, 4, 5, 6, 7, 9, 12, 13, 14, 17, 18, 19, 23, 25],
#     [2, 3, 5, 7, 10, 11, 12, 13, 15, 18, 19, 21, 23, 24, 25],
#     [1, 2, 3, 5, 6, 11, 13, 16, 17, 19, 21, 22, 23, 24, 25],
#     [1, 4, 5, 7, 8, 10, 12, 13, 14, 18, 20, 21, 22, 23, 24],
#     [1, 3, 5, 6, 7, 8, 11, 12, 13, 15, 17, 18, 21, 22, 24],
#     [1, 3, 4, 6, 9, 10, 12, 13, 14, 18, 19, 21, 23, 24, 25],
#     [3, 4, 5, 6, 7, 8, 9, 13, 14, 16, 18, 19, 20, 21, 25],
#     [1, 5, 6, 7, 9, 10, 12, 15, 17, 18, 19, 21, 23, 24, 25],
#     [1, 4, 5, 6, 9, 10, 11, 12, 14, 15, 17, 18, 21, 22, 24],
#     [1, 3, 4, 6, 11, 13, 14, 15, 16, 17, 18, 20, 21, 22, 25],
#     [1, 2, 4, 6, 7, 8, 11, 14, 15, 16, 17, 18, 19, 21, 22],
#     [1, 2, 9, 10, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25],
#     [2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 18, 19, 21, 23, 25],
#     [1, 2, 3, 4, 6, 8, 11, 12, 16, 17, 18, 19, 22, 23, 25],
#     [1, 2, 3, 4, 6, 8, 11, 12, 16, 17, 18, 19, 22, 23, 25],
#     [1, 3, 5, 6, 7, 12, 14, 15, 17, 18, 19, 20, 22, 23, 25],
#     [2, 3, 4, 5, 7, 8, 9, 10, 11, 14, 16, 18, 20, 23, 25],
#     [1, 2, 4, 6, 9, 10, 11, 12, 16, 17, 18, 20, 22, 23, 25],
#     [1, 2, 3, 5, 6, 7, 11, 12, 13, 15, 16, 19, 22, 23, 25],
#     [1, 2, 3, 5, 6, 9, 10, 13, 15, 17, 19, 21, 22, 23, 25],
#     [2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 19, 21, 23, 24, 25],
# ]

# # Contar frequência dos números
# frequencias = Counter()
# for concurso in resultados_27_concursos:
#     frequencias.update(concurso)

# # Ordenar do mais frequente ao menos
# frequencia_ordenada = sorted(frequencias.items(), key=lambda x: (-x[1], x[0]))

# # Mostrar resultados
# for numero, freq in frequencia_ordenada:
#     print(f"Número {numero:2d} apareceu {freq:2d} vezes")



# import numpy as np
# from collections import Counter

# # Últimos 9 jogos da Lotofácil até o concurso 3487
# jogos = [
#     [2, 4, 5, 7, 10, 12, 13, 15, 16, 17, 18, 19, 21, 22, 23],  # 3487
#     [2, 6, 7, 8, 9, 10, 11, 12, 16, 17, 18, 19, 22, 24, 25],   # 3486
#     [2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 15, 18, 20, 22, 25],    # 3485
#     [1, 3, 4, 5, 7, 8, 9, 11, 13, 14, 15, 17, 23, 24, 25],     # 3484
#     [2, 4, 7, 8, 9, 12, 13, 14, 15, 17, 18, 20, 22, 24, 25],   # 3483
#     [1, 2, 4, 5, 9, 10, 13, 14, 15, 17, 19, 20, 22, 24, 25],   # 3482
#     [1, 2, 3, 4, 5, 7, 9, 10, 13, 14, 19, 21, 22, 23, 24],     # 3481
#     [3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23],   # 3480
#     [1, 5, 6, 8, 9, 10, 12, 13, 15, 16, 18, 19, 23, 24, 25]    # 3479
# ]

# # Contar frequência de cada número
# todos = sum(jogos, [])
# contagem = Counter(todos)

# # Criar pesos para cada número de 1 a 25 com +1 para evitar zero
# peso = {num: contagem.get(num, 0) + 1 for num in range(1, 26)}
# nums = np.array(list(peso.keys()))
# pesos = np.array([peso[n] for n in nums], dtype=float)
# pesos /= pesos.sum()

# # Simulação Monte Carlo
# n_sim = 100_000
# resultados = []

# for _ in range(n_sim):
#     sorteio = np.random.choice(nums, size=15, replace=False, p=pesos)
#     resultados.extend(sorteio)

# # Contagem final das simulações
# sim_contagem = Counter(resultados)
# mais_sugeridos = sim_contagem.most_common(15)
# mais_sugeridos_sorted = sorted([num for num, _ in mais_sugeridos])

# print("🔮 Números mais prováveis para o próximo sorteio:")
# print(mais_sugeridos_sorted)

#=============
#=============
#=============

import random

# Gerar 6 números aleatórios para a Mega-Sena (entre 1 e 60)
numeros_mega_sena = sorted(random.sample(range(1, 61), 6))
print(numeros_mega_sena)
