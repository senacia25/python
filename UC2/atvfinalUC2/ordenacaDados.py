import pandas as pd

produtos_mercado = "UC2/atvfinal/produtos_mercado.csv"
df_pdmrc = pd.read_csv(produtos_mercado)

#15
ordemAlfa = df_pdmrc.sort_values(by="Produto",ascending=True)
print("\n===== PRODUTOS ORDENADOS ALFABETICAMENTE =====\n")
print(ordemAlfa)

#16
mais_caro = df_pdmrc.sort_values(by="Preco_Kg",ascending=False)
print("\n===== 5 PRODUTOS MAIS CARO NA LISTA (ordem de frutas seria 1°-abacaxi, 2°-pessego, 3°-morange, 4°-cereja, 5°-kiwi) =====\n")
print(mais_caro.head())
#1 abacaxi 2 pessego 3 morange 4 cereja 5 kiwi

#17
ordem = df_pdmrc.sort_values(by="Data_Ultima_Reposicao",ascending=True)
print("\n===== LISTA ORDENADA PELA DATA DO MAIS RECENTE PARA O MAIS ANTIGO =====\n",ordem)

ordem1 = {}