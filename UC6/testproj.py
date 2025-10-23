# ==============================================
# PROJETO FINAL - IA PARA GESTÃO DE VENDAS E ESTOQUE
# ==============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

# -------------------------------
# CONFIGURAÇÕES DE ESTILO
# -------------------------------
sns.set_theme(style="whitegrid", palette="Set2")
plt.rcParams.update({
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "figure.facecolor": "white"
})

# -------------------------------
# 1️⃣ CARREGAR E PROCESSAR OS DADOS DE VENDAS
# -------------------------------
df = pd.read_csv("UC6/vendas_simuladas.csv")
df["Data"] = pd.to_datetime(df["Data"])

# Traduzir os nomes dos dias da semana
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

ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

# Calcular métricas de vendas e faturamento
if "Valor_Total" not in df.columns:
    precos = {
        "Hambúrguer Clássico": 20.0,
        "Cheeseburguer": 22.0,
        "Bacon Burger": 25.0,
        "Veggie Burger": 21.0,
        "Batata Frita": 10.0,
        "Onion Rings": 12.0,
        "Refrigerante": 5.0,
        "Milkshake": 12.0,
        "Água": 4.0,
        "Brownie": 8.0,
        "Sorvete": 10.0
    }
    df["Preco_Unitario"] = df["Produto"].map(precos)
    df["Valor_Total"] = df["Quantidade"] * df["Preco_Unitario"]

faturamento_por_produto = df.groupby("Produto")["Valor_Total"].sum().sort_values()
media_vendas_produto_dia = (
    df.groupby(["Produto", "Dia_da_Semana"])["Quantidade"]
    .mean().unstack().reindex(columns=ordem_dias)
)

# -------------------------------
# 2️⃣ CARREGAR E PROCESSAR O ESTOQUE
# -------------------------------
estoque = pd.read_csv("UC6/estoque.csv")
estoque["Validade"] = pd.to_datetime(estoque["Validade"])

# Combinar com faturamento
estoque_analise = estoque.merge(
    faturamento_por_produto.rename("Faturamento_Total"),
    on="Produto",
    how="left"
)

# Calcular índice de giro e dias para vencer
estoque_analise["Indice_Giro"] = estoque_analise["Faturamento_Total"] / estoque_analise["Estoque_Atual"]
hoje = datetime.today()
estoque_analise["Dias_Para_Vencer"] = (estoque_analise["Validade"] - hoje).dt.days

# Gerar alertas inteligentes
def gerar_alerta(row):
    if row["Dias_Para_Vencer"] <= 3:
        return "⚠️ Validade próxima"
    elif row["Estoque_Atual"] < 15:
        return "📉 Estoque baixo"
    elif row["Indice_Giro"] > 50:
        return "🔥 Alta demanda"
    else:
        return "✅ Ok"

estoque_analise["Alerta"] = estoque_analise.apply(gerar_alerta, axis=1)

# -------------------------------
# 3️⃣ MODELO DE IA - PREVISÃO DE ESTOQUE IDEAL (CORRIGIDO)
# -------------------------------

# Criar DataFrame com média de vendas por produto
media_vendas_df = media_vendas_produto_dia.mean(axis=1).rename("Media_Vendas").reset_index()

# Unir com o estoque
estoque_analise = estoque_analise.merge(media_vendas_df, on="Produto", how="left")

# Substituir médias ausentes (produtos sem venda) por 0
estoque_analise["Media_Vendas"] = estoque_analise["Media_Vendas"].fillna(0)

# Treinar modelo linear simples
X = estoque_analise[["Media_Vendas"]]
y = estoque_analise["Estoque_Atual"]

modelo = LinearRegression().fit(X, y)

# Prever estoque ideal
estoque_analise["Estoque_Previsto"] = modelo.predict(X)

# -------------------------------
# 4️⃣ RELATÓRIO EXECUTIVO
# -------------------------------
print("\n==============================")
print("📊 RELATÓRIO INTELIGENTE - STATUS DO NEGÓCIO")
print("==============================")
print(f"📅 Data de Análise: {hoje.strftime('%d/%m/%Y')}")
print(f"💰 Faturamento total: R$ {faturamento_por_produto.sum():,.2f}")
print(f"📦 Produtos com alerta: {len(estoque_analise[estoque_analise['Alerta'] != '✅ Ok'])}")

print("\n🔹 ALERTAS DE ESTOQUE E VALIDADE:\n")
print(estoque_analise[["Produto", "Estoque_Atual", "Validade", "Dias_Para_Vencer", "Alerta"]])

print("\n🔹 PREVISÃO DE ESTOQUE IDEAL (IA):\n")
print(estoque_analise[["Produto", "Estoque_Atual", "Estoque_Previsto", "Alerta"]].round(1))

# -------------------------------
# 5️⃣ GRÁFICOS INTELIGENTES
# -------------------------------
plt.figure(figsize=(10,5))
sns.barplot(x="Produto", y="Dias_Para_Vencer", hue="Alerta", data=estoque_analise, dodge=False, palette="coolwarm")
plt.title("Dias Restantes para Validade por Produto")
plt.xlabel("Produto")
plt.ylabel("Dias para Vencer")
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x="Produto", y="Estoque_Atual", hue="Alerta", data=estoque_analise, dodge=False, palette="viridis")
plt.title("Nível de Estoque e Situação de Alerta")
plt.xlabel("Produto")
plt.ylabel("Estoque Atual")
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x="Produto", y="Indice_Giro", data=estoque_analise, palette="crest")
plt.title("Índice de Giro por Produto (R$ / unidade)")
plt.xlabel("Produto")
plt.ylabel("Giro Financeiro")
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x="Estoque_Atual", y="Estoque_Previsto", hue="Alerta", data=estoque_analise, palette="coolwarm", s=100)
plt.title("Previsão de Estoque Ideal x Atual (IA)")
plt.xlabel("Estoque Atual")
plt.ylabel("Estoque Previsto (IA)")
plt.tight_layout()
plt.show()

print("\n✅ Análise concluída com sucesso!")
