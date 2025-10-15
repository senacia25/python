import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando o CSV
data = pd.read_csv("UC4/projeto/industria.csv", parse_dates=["Data"])

# Visualizando os dados
print(data.head())


#===EX.1
# Receita total por fábrica
receita_por_fabrica = data.groupby("Fabrica")["Receita"].sum().sort_values(ascending=False)

# Gráfico de barras
sns.barplot(x=receita_por_fabrica.index, y=receita_por_fabrica.values)
plt.title("Receita Total por Fábrica")
plt.ylabel("Receita Total")
plt.xlabel("Fábrica")
plt.show()

# Perguntas
fabrica_maior_receita = receita_por_fabrica.idxmax()
fabrica_menor_receita = receita_por_fabrica.idxmin()
diferenca = receita_por_fabrica.max() - receita_por_fabrica.min()

print(f"Fábrica com maior receita: {fabrica_maior_receita}")
print(f"Diferença entre maior e menor receita: R${diferenca}")


#===EX.2
# Receita média por produto
receita_media_produto = data.groupby("Produto")["Receita"].mean().sort_values(ascending=False)

# Gráfico de barras
sns.barplot(x=receita_media_produto.index, y=receita_media_produto.values)
plt.title("Receita Média por Produto")
plt.ylabel("Receita Média")
plt.xlabel("Produto")
plt.show()

# Perguntas
produto_maior_receita_media = receita_media_produto.idxmax()
produto_menor_receita_media = receita_media_produto.idxmin()

print(f"Produto com maior receita média: {produto_maior_receita_media}")
print(f"Produto com menor receita média: {produto_menor_receita_media}")


#===EX.3
# Criar coluna "Mes"
data["Mes"] = data["Data"].dt.to_period("M").astype(str)

# Quantidade total vendida por mês
quantidade_vendida_mes = data.groupby("Mes")["Quantidade_Vendida"].sum()

# Gráfico de linha
quantidade_vendida_mes.plot(kind="line", marker="o")
plt.title("Quantidade Vendida Total por Mês")
plt.ylabel("Quantidade Vendida")
plt.xlabel("Mês")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Perguntas
mes_maior_venda = quantidade_vendida_mes.idxmax()
print(f"Mês com maior quantidade vendida: {mes_maior_venda}")


#===EX.4
# Criar coluna "Lucro"
data["Lucro"] = data["Receita"] - data["Custo"]

# Lucro médio por fábrica
lucro_medio_fabrica = data.groupby("Fabrica")["Lucro"].mean().sort_values(ascending=False)

# Gráfico de barras
sns.barplot(x=lucro_medio_fabrica.index, y=lucro_medio_fabrica.values)
plt.title("Lucro Médio por Fábrica")
plt.ylabel("Lucro Médio")
plt.xlabel("Fábrica")
plt.show()

# Perguntas
fabrica_mais_lucrativa = lucro_medio_fabrica.idxmax()
lucros_negativos = data[data["Lucro"] < 0]

print(f"Fábrica mais lucrativa em média: {fabrica_mais_lucrativa}")
print(f"Existe algum lucro negativo? {'Sim' if not lucros_negativos.empty else 'Não'}")


#===EX.5
# Tabela de receita total por fábrica e produto
pivot_receita = pd.pivot_table(data, values="Receita", index="Fabrica", columns="Produto", aggfunc="sum", fill_value=0)

# Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(pivot_receita, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Receita Total por Fábrica e Produto")
plt.xlabel("Produto")
plt.ylabel("Fábrica")
plt.show()

# Perguntas
for fabrica in pivot_receita.index:
    produto_mais_receita = pivot_receita.loc[fabrica].idxmax()
    print(f"Produto que gera mais receita na {fabrica}: {produto_mais_receita}")

faltantes = pivot_receita == 0
if faltantes.any().any():
    print("\nProdutos que não foram vendidos em algumas fábricas:")
    print(pivot_receita.where(faltantes).dropna(how='all').dropna(axis=1, how='all'))
else:
    print("\nTodos os produtos foram vendidos em todas as fábricas.")

