import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

query = """ SELECT
        p.nome_produto,
        SUM(i.quantidade) AS total_vendido
        FROM itens_pedido i
        JOIN produtos p ON i.produto_id = p.produto_id
        GROUP BY p.nome_produto
        ORDER BY total_vendido DESC
        LIMIT 10 """
        
df = pd.read_sql(query, con=engine)

#MatPlotLib
plt.figure(figsize= (10,6))
plt.bar(df['nome_produto'], df['total_vendido'], color= 'violet')
plt.title("TOP 10 PRODUTOS MAIS VENDIDOS!")
plt.xlabel("Produto")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=35, ha='right')
plt.show()

#Gráfico de pizza
plt.figure(figsize=(8,8))
plt.pie(df['total_vendido'], labels=df['nome_produto'], autopct='%1.1f%%')
plt.title("DISTRIBUIÇÃO DE VENDAS DOS TOP 10 PRODUTOS")
plt.show()



query2 = """
SELECT
    data_pedido AS mes,
    COUNT(*) AS total_pedidos
FROM pedidos
GROUP BY mes
ORDER BY mes
limit 10
"""

df_meses = pd.read_sql(query2, con=engine)
plt.figure(figsize=(10,6))
plt.plot(df_meses['mes'], df_meses['total_pedidos'], marker='o', linestyle='-')
plt.title("EVOLUÇÃO DOS PEDIDOS POR MÊS")
plt.xlabel("MÊS")
plt.ylabel("TOTAL PEDIDOS")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()