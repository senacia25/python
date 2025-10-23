import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("UC6/vendas_simuladas.csv")

# Converter coluna Data para datetime
df["Data"] = pd.to_datetime(df["Data"])

# Traduzir os nomes dos dias da semana do inglês para português
traducao_dias = {
    "Monday": "Segunda",
    "Tuesday": "Terça",
    "Wednesday": "Quarta",
    "Thursday": "Quinta",
    "Friday": "Sexta",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}

df["Dia_da_Semana"] = df["Data"].dt.day_name().map(traducao_dias)

# Ordem dos dias da semana para exibição
ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

# -------------------------------
# 1. Vendas totais por dia da semana (quantidade)
# -------------------------------
vendas_por_dia = df.groupby("Dia_da_Semana")["Quantidade"].sum().reindex(ordem_dias)

print("🔹 Vendas totais por dia da semana (Quantidade):\n")
print(vendas_por_dia)

# -------------------------------
# 2. Produtos com menor saída no período (quantidade)
# -------------------------------
vendas_por_produto = df.groupby("Produto")["Quantidade"].sum().sort_values()

print("\n🔹 Produtos com menor saída total no período (Quantidade):\n")
print(vendas_por_produto)

# -------------------------------
# 3. Faturamento total por dia da semana (R$)
# -------------------------------
if "Valor_Total" not in df.columns:
    print("\n⚠️ Coluna 'Valor_Total' não encontrada no dataset. Calculando valores fictícios com preços médios.")
    precos = {
        "Hambúrguer Clássico": 20.0,
        "Cheeseburguer": 22.0,
        "Batata Frita": 10.0,
        "Refrigerante": 5.0,
        "Milkshake": 12.0,
        "Sobremesa Especial": 15.0
    }
    df["Preco_Unitario"] = df["Produto"].map(precos)
    df["Valor_Total"] = df["Quantidade"] * df["Preco_Unitario"]

faturamento_por_dia = df.groupby("Dia_da_Semana")["Valor_Total"].sum().reindex(ordem_dias)

print("\n🔹 Faturamento total por dia da semana (R$):\n")
print(faturamento_por_dia.round(2))

# -------------------------------
# 4. Faturamento total por produto (R$)
# -------------------------------
faturamento_por_produto = df.groupby("Produto")["Valor_Total"].sum().sort_values()

print("\n🔹 Faturamento total por produto (R$):\n")
print(faturamento_por_produto.round(2))

# -------------------------------
# 5. Média diária de vendas por produto e dia da semana (quantidade)
# -------------------------------
media_vendas_produto_dia = (
    df.groupby(["Produto", "Dia_da_Semana"])["Quantidade"]
    .mean()
    .unstack()
    .reindex(columns=ordem_dias)
)

print("\n🔹 Média diária de vendas por produto e dia da semana (Quantidade):\n")
print(media_vendas_produto_dia.round(2))

# -------------------------------
# 6. Média diária de faturamento por produto e dia da semana (R$)
# -------------------------------
media_faturamento_produto_dia = (
    df.groupby(["Produto", "Dia_da_Semana"])["Valor_Total"]
    .mean()
    .unstack()
    .reindex(columns=ordem_dias)
)

print("\n🔹 Média diária de faturamento por produto e dia da semana (R$):\n")
print(media_faturamento_produto_dia.round(2))

# -------------------------------
# Gráficos
# -------------------------------

plt.figure(figsize=(8,5))
vendas_por_dia.plot(kind='bar', color='skyblue')
plt.title("Total de Vendas por Dia da Semana (Quantidade)")
plt.xlabel("Dia da Semana")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
faturamento_por_dia.plot(kind='bar', color='orange')
plt.title("Faturamento Total por Dia da Semana (R$)")
plt.xlabel("Dia da Semana")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
faturamento_por_produto.plot(kind='bar', color='green')
plt.title("Faturamento Total por Produto (R$)")
plt.xlabel("Produto")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
for produto in media_vendas_produto_dia.index:
    plt.plot(ordem_dias, media_vendas_produto_dia.loc[produto], marker='o', label=produto)
plt.title("Média Diária de Vendas por Produto e Dia da Semana (Quantidade)")
plt.xlabel("Dia da Semana")
plt.ylabel("Quantidade Média Vendida")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
for produto in media_faturamento_produto_dia.index:
    plt.plot(ordem_dias, media_faturamento_produto_dia.loc[produto], marker='o', label=produto)
plt.title("Média Diária de Faturamento por Produto e Dia da Semana (R$)")
plt.xlabel("Dia da Semana")
plt.ylabel("Faturamento Médio (R$)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
