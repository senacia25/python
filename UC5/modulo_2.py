import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

#mysql+pymysql://  - Define que estamos usando mysql com driver PyMysql
#root - Nome do usuario
#sua_senha: senha do banco
#localhost - onde está o servidor (se for remoto, muda)
#sistema_vendas - nome do banco de dados que vamos consumir.

df_produtos = pd.read_sql("SELECT * FROM produtos", con=engine)
# print(df_produtos.head()) 
# print("=========")
# print(df_produtos.columns) 
# print("=========")
# print(df_produtos.info()) 
# print("=========")
# print(df_produtos.describe()) 
# print("=========")

#limpeza e trasnformação
print(df_produtos.isnull().sum())
print("=========")

df_produtos["dimensoes"] = df_produtos["dimensoes"].fillna(0)
print(df_produtos.isnull().sum())

#filtros, seleção e agrupamento

#estamos filtrando o dataframe para selecionar apenas os "Ativos"
ativos = df_produtos[df_produtos["status_produto"] == "Ativo"] # select * from produtor where status_produto = "Ativo"

#filtrar o dataframe para escolher somente os produtos que estao abaixo do estoque minimo
abaixo_mim = ativos[ativos["estoque_atual"] < ativos ["estoque_minimo"]] # and estoque_atual < estoque_minimo

print("=========")
print(abaixo_mim[["nome_produto", "estoque_atual", "estoque_minimo"]])# select ""(print)colunas""" from produtor...


df = pd.read_sql("""SELECT c.nome_categoria, p.preco_venda
                 FROM produtos p
                 JOIN categorias c ON p.
                 categoria_id = c.
                 categoria_id""", con=engine)

medio_por_categoria = df.groupby("nome_categoria")["preco_venda"].mean()
print("==========")
print(medio_por_categoria)

