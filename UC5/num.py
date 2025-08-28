import pandas as pd
import numpy as np
from sqlalchemy import create_engine

#conectando banco de dados
engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

#lendo dados
df = pd.read_sql("SELECT preco_custo, preco_venda, estoque_atual FROM produtos", con=engine) #df dataframe

#convertendo colunas em array
preco_custo = df["preco_custo"].to_numpy()
preco_venda = df["preco_venda"].to_numpy()
estoque = df["estoque_atual"].to_numpy()

print(f"Preço medio de venda: {np.mean(preco_custo):.2f}") # media numpy
print("Preço mediano de venda: ", np.median(preco_venda)) # mediano
print(f"Desvio padrão do preço de venda: { np.std(preco_custo):.2f}") # desvio padrão
print("Produto mais caro: ", np.max(preco_custo)) # maximo, maior


#Calculando lucro unitario
lucro_unitario = preco_venda - preco_custo
print("Lucro unitário: ", lucro_unitario)

#Lucro total
lucro_total = lucro_unitario * estoque
print(f"Lucro total por produto em estoque: {lucro_total}")

#Filtrando
indices = lucro_unitario < 10
produtos_com_lucro_baixo = df[indices]
print(produtos_com_lucro_baixo[['preco_custo', 'preco_venda', 'estoque_atual']])

#Indice de rentabilidade
indice_rentbilidade = (lucro_unitario / preco_custo) * 100  # colocar em parenteses para preferencia de calculo primiro vai dividir
df["rentabilidade"] = np.round(indice_rentbilidade, 2) # round = arrendondar
print(df[['preco_custo', "preco_venda", "rentabilidade"]])



#PRATICA
#analizar os produtos em estoque e calcular, produtos com rentabilidade abaixo da media.


