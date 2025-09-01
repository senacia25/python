
import pandas as pd
import math
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_squared_error, r2_score 
from sqlalchemy import create_engine 
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

# Variáveis de entrada e saída
X = df[['total_vendido', 'preco_medio']]
y = df['faturamento']

# Separar em treino e teste (80% treino, 20% teste)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
modelo = LinearRegression()
modelo.fit(X_treino, y_treino)


# Prever com dados de teste
previsao = modelo.predict(X_teste)

# Avaliar
erro = mean_squared_error(y_teste, previsao)
r2 = r2_score(y_teste, previsao)

print(f"Erro médio quadrático (MSE): {erro:.2f}")
print(f"Coeficiente R²: {r2:.2f}")
print(f"Raiz quadrada do erro médio (RMSE): R$ {math.sqrt(erro):.2f}")

# Entrada do usuário
qtd = float(input("Digite a quantidade vendida: "))
preco = float(input("Digite o preço médio unitário (R$): "))

novo_dado = pd.DataFrame([[qtd, preco]], columns=['total_vendido', 'preco_medio'])

previsao_usuario = modelo.predict(novo_dado)

print(f"\nFaturamento estimado: R$ {previsao_usuario[0]:.2f}")



plt.figure(figsize=(10,6))
plt.plot(y_teste.values[:30], label="Valor real", marker='o')
plt.plot(previsao[:30], label="Previsão do modelo", marker='x')
plt.title("Comparação entre valor real e previsão de faturamento")
plt.xlabel("Índice de produto (teste)")
plt.ylabel("Faturamento (R$)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
