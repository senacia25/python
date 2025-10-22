import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("UC6/vendas_simuladas.csv")

# Converter coluna Data para datetime
df["Data"] = pd.to_datetime(df["Data"])

# Criar coluna com o nome do dia da semana
df["Dia_da_Semana"] = df["Data"].dt.day_name()

# -------------------------------
# 1. Vendas totais por dia da semana
# -------------------------------
vendas_por_dia = df.groupby("Dia_da_Semana")["Quantidade"].sum()

# Ordenar os dias da semana de segunda a domingo para o gráfico
ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
vendas_por_dia = vendas_por_dia.reindex(ordem_dias)

print("🔹 Vendas totais por dia da semana:\n")
print(vendas_por_dia)

# Gráfico vendas por dia da semana
plt.figure(figsize=(8,5))
vendas_por_dia.plot(kind='bar', color='skyblue')
plt.title("Total de Vendas por Dia da Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Produtos com menor saída no período
# -------------------------------
vendas_por_produto = df.groupby("Produto")["Quantidade"].sum().sort_values()

print("\n🔹 Produtos com menor saída total no período:\n")
print(vendas_por_produto)

# -------------------------------
# 3. Vendas médias por produto por dia da semana
# -------------------------------
media_por_produto_dia = df.groupby(["Produto", "Dia_da_Semana"])["Quantidade"].mean().unstack()

# Reordenar colunas dos dias da semana
media_por_produto_dia = media_por_produto_dia[ordem_dias]

print("\n🔹 Média diária de vendas por produto e dia da semana:\n")
print(media_por_produto_dia.round(2))
