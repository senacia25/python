import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")



#EXERCICIO PANDAS SQL 

#1 Liste os produtos com status "Descontinuado"
print("===========EX1=============")
query = '''select * from produtos where status_produto = "Descontinuado";'''

df_descon = pd.read_sql(query, con=engine)
print(df_descon.head())


#2 Calcule o valor total do estoque (preço_venda * estoque_atual)
print("===========EX2=============")
estoque = """
SELECT 
    produto_id,
    nome_produto,
    preco_venda,
    estoque_atual,
    (preco_venda * estoque_atual) AS valor_total_estoque
FROM produtos;
"""
total = """
SELECT SUM(preco_venda * estoque_atual) AS valor_total from produtos;"""

df_estoque = pd.read_sql(estoque, con=engine)
df_total = pd.read_sql(total, con=engine)
print(df_estoque.head())
print("Valor total do estoque: ", df_total)


#3 Filtre os fornecedores da cidade de "Maringá" e status "Ativo"
print("===========EX3=============")
forn = """SELECT * FROM fornecedores WHERE cidade = "Maringá" AND status_fornecedor = "Ativo";"""
df_forn = pd.read_sql(forn, con=engine)
print(df_forn)


#4 Agrupe os pedidos por forma de pagamento e calcule o valor médio de frete
print("===========EX4=============")
media_frete = """SELECT forma_pagamento, AVG(valor_frete) AS media_frete FROM pedidos GROUP BY forma_pagamento"""
df_frete = pd.read_sql(media_frete, con=engine)
print(df_frete)

#5  Liste os 5 produtos com menor margem de lucro (preco_venda - preco_custo)
print("===========EX5=============")
margem = """SELECT nome_produto,
preco_venda, preco_custo, (preco_venda - preco_custo)
AS margem_lucro FROM produtos ORDER BY margem_lucro ASC LIMIT 5;"""

df_margem = pd.read_sql(margem, con=engine)
print(df_margem)