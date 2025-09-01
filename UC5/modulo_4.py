#scikit-learn // machine learn
#*py -m* pip install scikit-learn pandas sqlalchemy pymysql 

import pandas as pd
import math
from sklearn.model_selection import train_test_split # treinar modelo
from sklearn.linear_model import LinearRegression # previsão
from sklearn.metrics import mean_squared_error, r2_score # medir o modelo, ver a qualidade de acerto. pra ver se tá proximo verdade
from sqlalchemy import create_engine #
import matplotlib.pyplot as plt

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

query = """
SELECT
    p.nome_produto,
    SUM(i.quantidade) AS total_vendido,
    AVG(i.preco_unitario) AS preco_medio,
    SUM(i.quantidade * i.preco_unitario) AS faturamento
FROM itens_pedido i 
JOIN produtos p ON p.produto_id = i.produto_id
GROUP BY p.produto_id
"""

df = pd.read_sql(query, con=engine)
print(df)

X = df[['total_vendido', 'preco_medio']] #entrada
y = df['faturamento'] #saída

# treinar o modelo

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42) # test_size 0.2 = 20%, vai aprender com 80% e treianar nos 20%

modelo = LinearRegression()
modelo.fit(X_treino, y_treino)

previsao = modelo.predict(X_teste) 

erro = mean_squared_error(y_teste, previsao)
r2 = r2_score(y_teste, previsao)

print(f"Erro médio quadrádico: {erro:.2f}")
print(f"Coeficiente R2: {r2:.2f}")
print(f"Raiz de erro médio quadrático em R$: {math.sqrt(erro):.2f}") #math matematica // errando em reais

print("\nErro de novo dado")
# prever um novo dado

novo_produto = pd.DataFrame([[500, 35.00]], columns=['total_vendido', 'preco_medio'])
previsao2 = modelo.predict(novo_produto)
print(f"Faturamento etimado para 500 unidades a R$ 35,00: é R$: {previsao2[0]:.2f}")


plt.figure(figsize=(10,6))
plt.plot(y_teste.values[:30], label="Valor real", marker='o')
plt.plot(previsao[:30], label="previsão de modelo", marker="x")
plt.title("Comparação de valor real e da previsão de faturamento")
plt.xlabel("Índice de produto no cojunto de teste")
plt.ylabel("Faturamento (R$)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()