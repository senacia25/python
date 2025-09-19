import pandas as pd

dados = "UC4/dados.csv"
df_dados = pd.read_csv(dados, parse_dates=["Data"])

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
#outro
produto_maior_receita = df_dados.groupby("Produto")["Receita Total"].sum()
produto_nome = produto_maior_receita.idxmax()
produto_valor = produto_maior_receita.max()

print(f"Produto com maior receita: {produto_nome}")
print(f"Valor da receita: {produto_valor}")
