import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df_vendas = pd.read_csv("UC6/vendas.csv")
df_estoque = pd.read_csv("UC6/estoque.csv")

# Converter datas
df_vendas["Data"] = pd.to_datetime(df_vendas["Data"])
df_estoque["Validade"] = pd.to_datetime(df_estoque["Validade"])

# ------------------------------------------
# 1. Produtos com menor saída por mês
# ------------------------------------------
df_vendas["Mes"] = df_vendas["Data"].dt.to_period("M")
vendas_mensais = df_vendas.groupby(["Mes", "Produto"])["Quantidade"].sum().reset_index()

# Produto menos vendido por mês
menor_saida_por_mes = vendas_mensais.sort_values(["Mes", "Quantidade"]).groupby("Mes").first().reset_index()

print("🔹 Produtos com menor saída por mês:\n")
print(menor_saida_por_mes)

# ------------------------------------------
# 2. Gráfico de vendas totais por semana
# ------------------------------------------
df_vendas["Semana"] = df_vendas["Data"].dt.to_period("W").apply(lambda r: r.start_time)
vendas_por_semana = df_vendas.groupby("Semana")["Quantidade"].sum().reset_index()

# Gráfico
plt.figure(figsize=(12, 6))
plt.plot(vendas_por_semana["Semana"], vendas_por_semana["Quantidade"], marker='o', linestyle='-')
plt.title("📈 Total de Vendas por Semana")
plt.xlabel("Semana")
plt.ylabel("Quantidade Vendida")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------
# 3. Possível desperdício: validade próxima e estoque alto
# ------------------------------------------
# Simular data de hoje
hoje = pd.to_datetime("2025-10-22")
df_estoque["Dias_para_validade"] = (df_estoque["Validade"] - hoje).dt.days

# Critérios: validade em até 5 dias E estoque > 15
possivel_desperdicio = df_estoque[
    (df_estoque["Dias_para_validade"] <= 5) & 
    (df_estoque["Estoque_Atual"] > 15)
]

print("\n⚠️ Produtos com possível desperdício (validade próxima e estoque alto):\n")
print(possivel_desperdicio)
