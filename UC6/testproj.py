import pandas as pd
import matplotlib.pyplot as plt

# Carregar o CSV de vendas
df = pd.read_csv("UC6/vendas.csv")

# Converter a coluna 'Data' para datetime
df["Data"] = pd.to_datetime(df["Data"])

# Adicionar coluna com o nome do dia da semana
df["Dia_da_Semana"] = df["Data"].dt.day_name()

# Agrupar por dia da semana e produto para ver o total vendido
vendas_por_dia_produto = df.groupby(["Dia_da_Semana", "Produto"])["Quantidade"].sum().reset_index()

# Reorganizar os dias da semana na ordem correta
dias_ordem = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
vendas_por_dia_produto["Dia_da_Semana"] = pd.Categorical(
    vendas_por_dia_produto["Dia_da_Semana"], 
    categories=dias_ordem, 
    ordered=True
)
vendas_por_dia_produto = vendas_por_dia_produto.sort_values(
    by=["Dia_da_Semana", "Quantidade"], 
    ascending=[True, False]
)

# Top 1 produto por dia da semana
top_vendidos_por_dia = vendas_por_dia_produto.groupby("Dia_da_Semana").first().reset_index()

# Plotar gráfico de barras
plt.figure(figsize=(10,6))
plt.bar(top_vendidos_por_dia["Dia_da_Semana"], top_vendidos_por_dia["Quantidade"], color="skyblue")
plt.title("Produto Mais Vendido por Dia da Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Mostrar os dados em texto
print(top_vendidos_por_dia[["Dia_da_Semana", "Produto", "Quantidade"]])
