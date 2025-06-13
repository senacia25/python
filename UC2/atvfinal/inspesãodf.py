import pandas as pd
#1
produtos_mercado = "UC2/atvfinal/produtos_mercado.csv"
df_pdmrc = pd.read_csv(produtos_mercado)

print(f"\n===== O Dataframe tem =====\n -{df_pdmrc.shape[0]}- Linhas e -{df_pdmrc.shape[1]}- Colunas")

#2
print("\n===== Nome de todas as colunas =====\n",df_pdmrc.columns.tolist())

#3
print("\n===== Tipos de dados =====\n",df_pdmrc.info())

#4
sete_linhas = df_pdmrc.iloc[0:7]
print(f"\n===== As 7 primeiras linhas são =====\n{sete_linhas}")

#5
tres_ultimas = df_pdmrc.iloc[497:501]
print(f"\n===== As três últimas linhas são =====\n{tres_ultimas}")
print(df_pdmrc.tail(3))

#6
print("\n===== Resumo estatístico das colunas nméricas =====\n",df_pdmrc.describe())


