# Bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#==== 1. A

# Ler CSV
dados = "UC4/dados1.csv"
df = pd.read_csv(dados, parse_dates=["Data"])

# Verificar dimensões e tipos de dados
print("Formato do dataset:", df.shape)
print("\nInformações do dataset:")
print(df.info())

# Visualizar primeiras linhas
print("\nPrimeiras linhas:")
print(df.head())

# Verificar valores nulos
print("\nValores nulos por coluna:")
print(df.isnull().sum())

#==== 1. B

# Estatísticas básicas com describe
print(df.describe())

# Colunas de interesse numérico
colunas_numericas = ['Passageiros', 'Distância (km)', 'Ocupação (%)', 'Receita (R$)']

# Média, mediana, desvio padrão e variância
for coluna in colunas_numericas:
    print(f"\n{coluna}")
    print("Média:", df[coluna].mean())
    print("Mediana:", df[coluna].median())
    print("Desvio padrão:", df[coluna].std())
    print("Variância:", df[coluna].var())

# Percentis da Receita
print("\nPercentis da Receita (R$):")
print(df["Receita (R$)"].quantile([0.25, 0.5, 0.75]))

# Companhia com maior receita total
receita_por_companhia = df.groupby("Companhia")['Receita (R$)'].sum().sort_values(ascending=False)
print("\nCompanhia com maior receita total:")
print(receita_por_companhia.head(1))

# Companhia com maior número de passageiros
passageiros_por_companhia = df.groupby("Companhia")['Passageiros'].sum().sort_values(ascending=False)
print("\nCompanhia com maior número de passageiros:")
print(passageiros_por_companhia.head(1))

# Contagem de voos por companhia
voos_por_companhia = df['Companhia'].value_counts()
print("\nNúmero de voos por companhia:")
print(voos_por_companhia)

# Receita média por companhia
print("\nReceita média por companhia:")
print(df.groupby("Companhia")['Receita (R$)'].mean().sort_values(ascending=False))

# Receita média por aeroporto de origem
print("\nReceita média por aeroporto de origem:")
print(df.groupby("Aeroporto Origem")['Receita (R$)'].mean().sort_values(ascending=False))

#==== 1. C

# Histograma da distribuição de passageiros
sns.histplot(df['Passageiros'], bins=30, kde=True)
plt.title("Distribuição de Passageiros")
plt.xlabel("Número de Passageiros")
plt.ylabel("Frequência")
plt.show()

# Boxplot da ocupação (%) por companhia
sns.boxplot(data=df, x='Companhia', y='Ocupação (%)')
plt.title("Boxplot da Ocupação por Companhia Aérea")
plt.xlabel("Companhia Aérea")
plt.ylabel("Ocupação (%)")
plt.show()

# Gráfico de barras da receita média por companhia
receita_media = df.groupby("Companhia")['Receita (R$)'].mean().sort_values(ascending=False).reset_index()
sns.barplot(data=receita_media, x='Companhia', y='Receita (R$)')
plt.title("Receita Média por Companhia")
plt.ylabel("Receita Média (R$)")
plt.xlabel("Companhia")
plt.show()

# Scatterplot de Distância x Receita
sns.scatterplot(data=df, x='Distância (km)', y='Receita (R$)', hue='Companhia')
plt.title("Distância x Receita por Companhia")
plt.xlabel("Distância (km)")
plt.ylabel("Receita (R$)")
plt.show()

# Heatmap de correlação entre variáveis numéricas
corr = df[['Passageiros', 'Distância (km)', 'Ocupação (%)', 'Receita (R$)']].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Mapa de Calor das Correlações")
plt.show()

#==== 1. D

print("\n\t============Respostas=============\n")

# Companhia com maior número de voos
print("Companhia com maior número de voos:", voos_por_companhia.idxmax())

# Correlação distância e receita
corr_dist_receita = df[['Distância (km)', 'Receita (R$)']].corr().iloc[0,1]
print("\nCorrelação Distância x Receita:", round(corr_dist_receita, 2))

# Correlação ocupação e receita
corr_ocup_receita = df[['Ocupação (%)', 'Receita (R$)']].corr().iloc[0,1]
print("Correlação Ocupação x Receita:", round(corr_ocup_receita, 2))

# Aeroportos de origem com mais voos
print("\nTop 5 aeroportos de origem com mais voos:")
print(df['Aeroporto Origem'].value_counts().head(5))

# Respostas:

# 1. Qual companhia tem maior participação em número de voos?
#   R - A Azul é a companhia que mais aparece nos dados — foi a que teve o maior número de voos.

# 2. A distância influencia a receita?
#   R -  Até influencia um pouco, mas bem pouco mesmo. A correlação entre distância e receita foi de 0,11, o que é uma ligação fraca. Ou seja, voos mais longos tendem a gerar mais receita, mas não é uma regra forte. Outros fatores como o preço das passagens ou a ocupação dos voos acabam pesando mais.

# 3. Os voos com maior ocupação são necessariamente os de maior receita?
#   R -  Nem sempre. A correlação entre ocupação e receita também foi baixa (0,13), o que mostra que um voo cheio não garante uma receita alta. Às vezes o voo tá lotado, mas com passagens mais baratas. Então, ocupação ajuda, mas não é o único fator que influencia a receita.

# 4. Quais aeroportos de origem concentram mais voos?
#   R - 
#       CGH (Congonhas) – 32 voos
#       GIG (Galeão) – 28 voos
#       SDU (Santos Dumont) – 22 voos
#       GRU (Guarulhos) – 20 voos
#       BSB (Brasília) – 18 voos

