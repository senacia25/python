import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configurações
start_date = datetime(2025, 5, 1)
end_date = datetime(2025, 10, 21)
date_range = pd.date_range(start_date, end_date)

# Lista de produtos variados
produtos = [
    "Cheeseburger", "Bacon Burger", "Veggie Burger",
    "Batata Frita", "Onion Rings", "Refrigerante", 
    "Milkshake", "Água", "Brownie", "Sorvete"
]

# Gerar vendas fictícias
vendas = []
id_venda = 1

for data in date_range:
    num_vendas_dia = random.randint(8, 20)  # número de vendas por dia
    produtos_dia = random.choices(produtos, k=num_vendas_dia)

    for produto in produtos_dia:
        quantidade = random.randint(1, 4)
        vendas.append([id_venda, data.strftime('%Y-%m-%d'), produto, quantidade])
        id_venda += 1

# Criar DataFrame
df_vendas = pd.DataFrame(vendas, columns=["ID_Venda", "Data", "Produto", "Quantidade"])

# Salvar em CSV
df_vendas.to_csv("vendas.csv", index=False)

print("Arquivo 'vendas.csv' criado com sucesso!")
