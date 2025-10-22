import pandas as pd
import numpy as np

# Produtos da hamburgueria e seus preços unitários (em reais)
precos = {
    "Hambúrguer Clássico": 12.0,
    "Cheeseburguer": 14.0,
    "Batata Frita": 8.0,
    "Refrigerante": 5.0,
    "Milkshake": 10.0,
    "Sobremesa Especial": 15.0
}

produtos = list(precos.keys())

# Período de 6 meses
datas = pd.date_range(start="2025-05-01", end="2025-10-31")

dados = []
np.random.seed(42)  # Para resultados reproduzíveis

id_venda = 1

for data in datas:
    dia_semana = data.weekday()  # Segunda=0, Domingo=6
    
    # Ajuste da média de vendas por dia da semana
    if dia_semana in [4, 5, 6]:  # Sexta, Sábado, Domingo
        media_vendas = 40
    elif dia_semana in [0, 1]:  # Segunda, Terça
        media_vendas = 15
    else:  # Quarta, Quinta
        media_vendas = 25
    
    for produto in produtos:
        # Quantidade vendida por produto: média ajustada por dia + variação aleatória
        quantidade = max(0, int(np.random.normal(loc=media_vendas, scale=10)))
        valor_unitario = precos[produto]
        valor_total = round(quantidade * valor_unitario, 2)
        
        dados.append({
            "id_venda": id_venda,
            "Data": data.strftime("%Y-%m-%d"),
            "Produto": produto,
            "Quantidade": quantidade,
            "Valor_Total": valor_total
        })
        
        id_venda += 1

# Criar DataFrame
df_vendas = pd.DataFrame(dados)

# Salvar CSV
df_vendas.to_csv("vendas_simuladas.csv", index=False)

print("Arquivo 'vendas_simuladas.csv' criado com sucesso!")

