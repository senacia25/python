import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")



#EXERCICIO PANDAS SQL 

#1 Liste os produtos com status "Descontinuado"

query = '''select * from produtos where status_produto = "Descontinuado";'''

df_descon = pd.read_sql(query, con=engine)
print(df_descon.head())


#2 Calcule o valor total do estoque (preço_venda * estoque_atual)

# SQL para isso:
# SELECT 
#     produto_id,
#     nome_produto,
#     preco_venda,
#     estoque_atual,
#     (preco_venda * estoque_atual) AS valor_total_estoque
# FROM produtos;

# Se quiser o valor total do estoque de todos os produtos somados (ou seja, o valor total geral do estoque):
# SELECT 
#     SUM(preco_venda * estoque_atual) AS valor_total_estoque_geral
# FROM produtos;

# Em Python com pandas:
# query = """
# SELECT 
#     produto_id,
#     nome_produto,
#     preco_venda,
#     estoque_atual,
#     (preco_venda * estoque_atual) AS valor_total_estoque
# FROM produtos
# """

# df_estoque = pd.read_sql(query, con=engine)
# print(df_estoque)


#3 Filtre os fornecedores da cidade de "Maringá" e status "Ativo"


#4 Agrupe os pedidos por forma de pagamento e calcule o valor médio de frete


#5  Liste os 5 produtos com menor margem de lucro (preco_venda - preco_custo)

