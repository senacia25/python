import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

#mysql+pymysql://  - Define que estamos usando mysql com driver PyMysql
#root - Nome do usuario
#sua_senha: senha do banco
#localhost - onde está o servidor (se for remoto, muda)
#sistema_vendas - nome do banco de dados que vamos consumir.

# df_produtos = pd.read_sql("SELECT * FROM produtos", con=engine)
# print(df_produtos.head()) 
# print("=========")
# print(df_produtos.columns) 
# print("=========")
# print(df_produtos.info()) 
# print("=========")
# print(df_produtos.describe()) 
# print("=========")

# #limpeza e trasnformação
# print(df_produtos.isnull().sum())
# print("=========")

# df_produtos["dimensoes"] = df_produtos["dimensoes"].fillna(0)
# print(df_produtos.isnull().sum())

# #filtros, seleção e agrupamento

# #estamos filtrando o dataframe para selecionar apenas os "Ativos"
# ativos = df_produtos[df_produtos["status_produto"] == "Ativo"] # select * from produtor where status_produto = "Ativo"

# #filtrar o dataframe para escolher somente os produtos que estao abaixo do estoque minimo
# abaixo_mim = ativos[ativos["estoque_atual"] < ativos ["estoque_minimo"]] # and estoque_atual < estoque_minimo

# print("=========")
# print(abaixo_mim[["nome_produto", "estoque_atual", "estoque_minimo"]])# select ""(print)colunas""" from produtor...


# df = pd.read_sql("""SELECT c.nome_categoria, p.preco_venda
#                  FROM produtos p
#                  JOIN categorias c ON p.
#                  categoria_id = c.
#                  categoria_id""", con=engine)

# medio_por_categoria = df.groupby("nome_categoria")["preco_venda"].mean()
# print("==========")
# print(medio_por_categoria)



#pratica
# print("==========")

# # Carregando os dados
# itens_pedido = pd.read_sql("SELECT * FROM itens_pedido", engine)
# produtos = pd.read_sql("SELECT * FROM produtos", engine)

# # Juntando os dados de produtos com os itens vendidos
# df = itens_pedido.merge(produtos, on='produto_id')

# # Calculando o total vendido por item (descontando o desconto do item)
# df['valor_total_item'] = df['quantidade'] * (df['preco_unitario'] - df['desconto_item'])

# # Agrupando por produto
# resumo_vendas = df.groupby(['produto_id', 'nome_produto']) \
#                   .agg(quantidade_vendida=('quantidade', 'sum'),
#                        total_vendido=('valor_total_item', 'sum')) \
#                   .reset_index()

# # Ordenando pelos mais vendidos em quantidade
# resumo_vendas = resumo_vendas.sort_values(by='quantidade_vendida', ascending=False)

# # Mostrando resultado
# print(resumo_vendas)



# # outra forma

# query = """SELECT p.nome_produto,
#         SUM(i.quantidade) AS total_vendido,
#         SUM(i.quantidade * i.preco_unitario) AS total_faturado
#         FROM itens_pedido i
#         JOIN produtos p ON i.produto_id = p.produto_id
#         GROUP BY p.nome_produto
#         ORDER BY total_vendido DESC"""

# df_vendas = pd.read_sql(query, con=engine)
# print(df_vendas.head(10))


# JOIN produtos p ON i.produto_id = p.produto_id	Junta os itens vendidos com os dados do produto
# SUM(i.quantidade)	Soma o total de unidades vendidas por produto
# SUM(i.quantidade * i.preco_unitario)	Calcula o total faturado por produto
# GROUP BY p.nome_produto	Agrupa os resultados por nome de produto
# ORDER BY total_vendido DESC	Ordena pelos mais vendidos primeiro
# 🐼 Integração com pandas:

# A linha:

# df_vendas = pd.read_sql(query, con=engine)

# Roda a query SQL direto no banco e já traz o resultado como um DataFrame pandas, pronto pra usar!

# 📈 Exemplo de saída esperada:
# nome_produto	total_vendido	total_faturado
# Arroz Integral 5kg	420	7,800.00
# Feijão Carioca 1kg	390	3,200.00
# ...	...	...
# 🔧 Melhorias possíveis:

# Descontar desconto_item no cálculo do faturamento:

# SUM(i.quantidade * (i.preco_unitario - i.desconto_item)) AS total_faturado


# Incluir produto_id no GROUP BY para evitar erros se houver produtos com mesmo nome:

# GROUP BY p.produto_id, p.nome_produto

# 💡 Versão melhorada:
# SELECT 
#     p.produto_id,
#     p.nome_produto,
#     SUM(i.quantidade) AS total_vendido,
#     SUM(i.quantidade * (i.preco_unitario - i.desconto_item)) AS total_faturado
# FROM itens_pedido i
# JOIN produtos p ON i.produto_id = p.produto_id
# GROUP BY p.produto_id, p.nome_produto
# ORDER BY total_vendido DESC


# Se quiser ajuda para adaptar esse relatório por categoria, período, ou outro filtro, posso te ajudar também!


# ✅ O que significam as letras antes do ponto (ex: i.quantidade, p.nome_produto)?

# Essas letras são alias (apelidos) dados às tabelas no FROM ou no JOIN da sua query.

# 🧠 Por que usar?

# Para encurtar nomes de tabelas.

# Para evitar ambiguidade quando duas tabelas têm colunas com o mesmo nome (por exemplo, produto_id aparece nas duas tabelas).

# Para deixar a query mais legível e organizada.

# 📌 Exemplo:
# FROM itens_pedido i
# JOIN produtos p ON i.produto_id = p.produto_id


# Aqui:

# i é o apelido para a tabela itens_pedido

# p é o apelido para a tabela produtos

# Então, quando você escreve:

# i.quantidade


# Você está dizendo: "coluna quantidade da tabela itens_pedido"
# E:

# p.nome_produto


# Significa: "coluna nome_produto da tabela produtos"

# 🔍 Exemplo completo:
# SELECT 
#     p.nome_produto,         -- nome do produto (tabela produtos)
#     SUM(i.quantidade)       -- soma das quantidades vendidas (tabela itens_pedido)
# FROM itens_pedido i
# JOIN produtos p ON i.produto_id = p.produto_id
# GROUP BY p.nome_produto


# Se você não usar os alias, teria que escrever:

# SELECT 
#     produtos.nome_produto,
#     SUM(itens_pedido.quantidade)
# FROM itens_pedido
# JOIN produtos ON itens_pedido.produto_id = produtos.produto_id
# ...


# Funciona do mesmo jeito, mas fica mais longo.


