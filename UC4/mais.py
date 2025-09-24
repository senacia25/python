# import pandas as pd

# dados = "UC4/dados.csv"
# df_dados = pd.read_csv(dados, parse_dates=["Data"])

# print(df_dados.head())
# print(df_dados.describe())
# print(df_dados.info())

# col = ["Vendas", "Preço Unitário", "Receita Total"]
# print(df_dados[col].head())
# #outra forma de ler as colunas especificas
# col = df_dados[["Vendas", "Preço Unitário", "Receita Total"]]
# print(col.head())

# for col in ["Vendas", "Preço Unitário", "Receita Total"]:
#     print(f"\n\t*{col}*")
#     print("Média", df_dados[col].mean())
#     print("Mediana", df_dados[col].median())
#     print("Desvio padrão", df_dados[col].std())
#     print("Variância", df_dados[col].var())
   
   
# produto_maior_receita = df_dados.groupby("Produto")["Receita Total"].sum().idxmax()
# print(produto_maior_receita)

# #outro
# produto_maior_receita = df_dados.groupby("Produto")["Receita Total"].sum()
# produto_nome = produto_maior_receita.idxmax()
# produto_valor = produto_maior_receita.max()

# print(f"Produto com maior receita: {produto_nome}")
# print(f"Valor da receita: {produto_valor}")

#=================
#=================

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# dados = "UC4/dados.csv"
# df_dados = pd.read_csv(dados, parse_dates=["Data"])

# quantidade_por_produto = df_dados["Produto"].value_counts()
# print(quantidade_por_produto)

# media_receita = df_dados.groupby(["Produto", "Região"])["Receita Total"].mean()
# print(media_receita)

# # Histograma da Vendas com KDE
# plt.figure(figsize=(9, 6))
# sns.histplot(df_dados["Vendas"], kde=True, color="darkorange", bins=30) # define quantos "baldes" ou faixas (bins) o histograma terá para agrupar os dados.
# plt.title("Histograma da Coluna Vendas com KDE", fontsize=16) # define o tamanho da fonte (em pontos) do texto no gráfico.
# plt.xlabel("Vendas", fontsize=14)
# plt.ylabel("Frequência", fontsize=14)
# plt.tight_layout()
# plt.show(block=False)

# # Boxplot da Receita Total por Região
# plt.figure(figsize=(9, 6))
# sns.boxplot(data=df_dados, x="Região", y="Receita Total", palette="Set1") # define a paleta de cores usada no gráfico. "Set2" é uma paleta de cores pastel do Seaborn, com tons suaves e distintos. "dark cores mais escuras"
# plt.title("Boxplot da Receita Total por Região", fontsize=16)
# plt.xlabel("Região", fontsize=14)
# plt.ylabel("Receita Total", fontsize=14)
# plt.tight_layout()
# plt.show(block=False)


# # Scatterplot da relação entre Vendas e Receita Total por Produto
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=df_dados, x="Vendas", y="Receita Total", hue="Produto", palette="dark", s=70)
# plt.title("Relação entre Vendas e Receita Total por Produto", fontsize=16)
# plt.xlabel("Vendas", fontsize=14)
# plt.ylabel("Receita Total", fontsize=14)
# plt.legend(title="Produto", bbox_to_anchor=(1.05, 1), loc="upper left")  # legenda fora do gráfico
# plt.tight_layout()
# plt.show(block=False)


# # Seleciona apenas as colunas numéricas de interesse
# colunas_numericas = ["Vendas", "Preço Unitário", "Receita Total"]
# corr = df_dados[colunas_numericas].corr()

# # Plot do heatmap
# plt.figure(figsize=(8, 6))
# sns.heatmap(corr, annot=True, cmap="magma", fmt=".2f", linewidths=0.5)
# plt.title("Mapa de Calor - Correlação entre Variáveis Numéricas", fontsize=16)
# plt.tight_layout()
# plt.show(block=False)


# input("Pressione Enter para fechar tudo...") 
# plt.close('all') 


##======extra=======
#=======ploty.express ele deixa mais interativo, abriu no navegador

# import plotly.express as px

# # Histograma interativo da Vendas
# fig_hist = px.histogram(df_dados, x="Vendas", nbins=30, marginal="rug", 
#                         title="Histograma da Coluna Vendas com KDE (Interativo)")
# fig_hist.update_layout(bargap=0.1)
# fig_hist.show()

# # Boxplot interativo da Receita Total por Região
# fig_box = px.box(df_dados, x="Região", y="Receita Total", color="Região",
#                  title="Boxplot da Receita Total por Região (Interativo)")
# fig_box.show()

#=================
#=================

# import pandas as pd

# dados = "UC4/dados.csv"
# df_dados = pd.read_csv(dados, parse_dates=["Data"])

# df_dados["Mes"] = df_dados["Data"].dt.to_period("M") # M de mês

# vendas_mes = df_dados.groupby("Mes")["Vendas"].sum()
# print("\n===VENDAS POR MÊS===\n",vendas_mes)


# import pandas as pd
# import matplotlib.pyplot as plt

# # Carregar o arquivo CSV e processar os dados
# dados = "UC4/dados.csv"
# df_dados = pd.read_csv(dados, parse_dates=["Data"])

# # Criar uma coluna de período mensal
# df_dados["Mes"] = df_dados["Data"].dt.to_period("M")

# # Agrupar por mês e somar as vendas
# vendas_mes = df_dados.groupby("Mes")["Vendas"].sum()

# # Plotando o gráfico
# plt.figure(figsize=(10, 6))
# vendas_mes.plot(kind="line", marker='o', color='b')
# plt.title("Evolução das Vendas por Mês", fontsize=14)
# plt.xlabel("Mês", fontsize=12)
# plt.ylabel("Vendas", fontsize=12)
# plt.grid(True)
# plt.show()


# # #calcule a media movel de 7 dias da receita total e plote em um grafico e de linha para detectar tendencia

# # Ordenar o dataframe pela data
# df_dados = df_dados.sort_values("Data")

# # Calcular a média móvel de 7 dias da Receita Total
# df_dados["Media_Movel_7d"] = df_dados["Receita Total"].rolling(7).mean()

# # Plotar a receita diária e a média móvel para detectar tendências
# plt.figure(figsize=(12, 6))
# plt.plot(df_dados["Data"], df_dados["Receita Total"], label="Receita Total Diária", marker='o', color="darkblue", alpha=0.5)
# plt.plot(df_dados["Data"], df_dados["Media_Movel_7d"], label="Média Móvel 7 dias", color="red",  linewidth=2)
# plt.title("Receita Total Diária e Média Móvel de 7 Dias", fontsize=14)
# plt.xlabel("Data", fontsize=12)
# plt.ylabel("Receita Total", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()

import pandas as pd

dados = "UC4/dados.csv"
df_dados = pd.read_csv(dados, parse_dates=["Data"])

vendas_por_regiao_produto = df_dados.groupby(["Região", "Produto"])["Vendas"].sum()

produto_mais_vendido_por_regiao = vendas_por_regiao_produto.groupby("Região").idxmax()

print(produto_mais_vendido_por_regiao)

vendas_por_regiao_produto = df_dados.groupby(["Região", "Produto"])["Vendas"].sum().reset_index()

print(vendas_por_regiao_produto)


















# # Exibir o produto mais vendido por região
# for regiao, produto in produto_mais_vendido_por_regiao.items():
#     produto_vendido = vendas_por_regiao_produto[produto]
#     print(f"Na região {regiao}, o produto mais vendido foi {produto[1]} com {produto_vendido} unidades vendidas.")

