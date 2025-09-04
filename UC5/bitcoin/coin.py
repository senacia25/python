import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_squared_error, r2_score 
import matplotlib.pyplot as plt

bitcoin = "UC5/bitcoin/bitcoin_historico.csv"

df = pd.read_csv(bitcoin)


# Conversão da coluna 'Data' para o tipo datetime
df["Data"] = pd.to_datetime(df["Data"], format="%d.%m.%Y")

# Ordenação dos dados da data mais antiga para a mais recente
df = df.sort_values("Data").reset_index(drop=True)


# print(df.head())


# Converte colunas numéricas para float
colun = ["Último", "Abertura", "Máxima", "Mínima"]
for col in colun:
    df[col] = df[col].str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Converte a coluna Volume
def converter_volume(vol):
    vol = vol.replace(".", "").replace(",", ".")
    if "K" in vol:
        return float(vol.replace("K", "")) * 1e3
    elif "M" in vol:
        return float(vol.replace("M", "")) * 1e6
    elif "B" in vol:
        return float(vol.replace("B", "")) * 1e9
    return float(vol)

df["Vol."] = df["Vol."].astype(str).apply(converter_volume)

# Converte Var%
df["Var%"] = df["Var%"].str.replace("%", "").str.replace(",", ".").astype(float)

# Remove valores ausentes
df.dropna(inplace=True)

# print(df.head())



# Define os limites de data
data_inicio_treino = pd.to_datetime("2020-01-01")
data_fim_treino = pd.to_datetime("2025-08-16")

data_inicio_teste = pd.to_datetime("2025-08-17")
data_fim_teste = pd.to_datetime("2025-09-01")

# Divide em treino e teste
df_treino = df[(df["Data"] >= data_inicio_treino) & (df["Data"] <= data_fim_treino)].copy()
df_teste = df[(df["Data"] >= data_inicio_teste) & (df["Data"] <= data_fim_teste)].copy()

# Define as variáveis independentes (X) e dependente (y)
X_treino = df_treino[["Abertura", "Máxima", "Mínima", "Vol.", "Var%"]]
y_treino = df_treino["Último"]

X_teste = df_teste[["Abertura", "Máxima", "Mínima", "Vol.", "Var%"]]
y_teste = df_teste["Último"]


# print("Treino:")
# print(df_treino["Data"].min(), "→", df_treino["Data"].max())
# print("Registros:", len(df_treino))

# print("\nTeste:")
# print(df_teste["Data"].min(), "→", df_teste["Data"].max())
# print("Registros:", len(df_teste))


# Modelo
modelo = LinearRegression()
modelo.fit(X_treino, y_treino)


# Previsões
previsoes = modelo.predict(X_teste)

# Avaliação
erro = mean_squared_error(y_teste, previsoes)
r2 = r2_score(y_teste, previsoes)

print("\n--- MÉTRICAS DE AVALIAÇÃO ---")
print(f"Erro Médio Quadrático (MSE): {erro:.2f}")
print(f"Coeficiente de Determinação (R²): {r2:.4f}")

# # Mostra previsões vs reais
# resultados = pd.DataFrame({
#     'Data': df_teste['Data'].dt.strftime('%Y-%m-%d'),
#     'Preço Real': y_teste.values,
#     'Preço Previsto': previsoes
# })
# print("\n--- PREVISÕES VS VALORES REAIS ---")
# print(resultados)



plt.figure(figsize=(12, 6))

# Linha dos valores reais
plt.plot(df_teste["Data"], y_teste, label="Preço Real", color="blue", marker='o')

# Linha das previsões
plt.plot(df_teste["Data"], previsoes, label="Preço Previsto", color="green", linestyle='--', marker='x')

# Configurações do gráfico
plt.title("Cotação do Bitcoin – Valores Reais vs. Previsões")
plt.xlabel("Data")
plt.ylabel("Cotação")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Exibe o gráfico
plt.show()



# =====tentando prever o futuro===================

# from datetime import timedelta

# # Último dia com dados disponíveis
# ultimo_dia = df["Data"].max()

# # Cria datas futuras de 2 a 15 de setembro de 2025
# datas_futuras = pd.date_range(start="2025-09-02", end="2025-09-15")

# # Obtém o último valor conhecido para usar como base
# ultimo_registro = df[df["Data"] == ultimo_dia].iloc[0]

# # Cria um novo DataFrame com os dados simulados
# futuro = pd.DataFrame({
#     "Data": datas_futuras
# })

# # Simulação dos dados
# np.random.seed(42)  # para reprodutibilidade

# futuro["Abertura"] = ultimo_registro["Último"]
# futuro["Máxima"] = futuro["Abertura"] * (1 + np.random.uniform(0.005, 0.015, len(futuro)))
# futuro["Mínima"] = futuro["Abertura"] * (1 - np.random.uniform(0.005, 0.015, len(futuro)))
# futuro["Vol."] = df["Vol."].tail(10).mean()  # média dos últimos 10 dias
# futuro["Var%"] = np.random.uniform(-1.0, 1.0, len(futuro))  # variação percentual aleatória

# # Previsão usando o modelo treinado
# X_futuro = futuro[["Abertura", "Máxima", "Mínima", "Vol.", "Var%"]]
# previsoes_futuras = modelo.predict(X_futuro)

# # Adiciona as previsões ao DataFrame
# futuro["Preço Previsto"] = previsoes_futuras

# # Mostra os resultados
# print(futuro[["Data", "Preço Previsto"]])

# # Plot
# plt.figure(figsize=(12, 6))
# plt.plot(futuro["Data"], futuro["Preço Previsto"], label="Previsão Futura", color="orange", marker='o')
# plt.title("Previsão do Bitcoin – 02 a 15 de Setembro")
# plt.xlabel("Data")
# plt.ylabel("Preço Previsto")
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.legend()
# plt.tight_layout()
# plt.show()



