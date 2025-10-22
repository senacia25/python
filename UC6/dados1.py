import pandas as pd
import random
from datetime import datetime, timedelta

# Lista de produtos (mesma usada no vendas.csv)
produtos = [
    "Cheeseburger", "Bacon Burger", "Veggie Burger",
    "Batata Frita", "Onion Rings", "Refrigerante", 
    "Milkshake", "Água", "Brownie", "Sorvete"
]

# Data base para validade (após o fim do período de vendas)
base_data_validade = datetime(2025, 10, 21)

# Gerar dados de estoque
estoque = []

for produto in produtos:
    quantidade = random.randint(10, 50)
    validade = base_data_validade + timedelta(days=random.randint(5, 20))
    estoque.append([produto, quantidade, validade.strftime('%Y-%m-%d')])

# Criar DataFrame
df_estoque = pd.DataFrame(estoque, columns=["Produto", "Estoque_Atual", "Validade"])

# Salvar em CSV
df_estoque.to_csv("estoque.csv", index=False)

print("Arquivo 'estoque.csv' criado com sucesso!")
