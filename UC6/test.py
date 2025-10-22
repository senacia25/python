import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define o intervalo de datas de um ano
start_date = datetime(2024, 10, 1)
end_date = datetime(2025, 10, 1)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Define os produtos e a demanda base
products = {
    "Combo Hambúrguer + Batata": {"type": "combo", "base_demand": 50},
    "Hambúrguer Simples": {"type": "burger", "base_demand": 30},
    "Batata Frita": {"type": "side", "base_demand": 25},
    "Refrigerante": {"type": "drink", "base_demand": 20},
    "Milkshake": {"type": "drink", "base_demand": 15},
    "Sobremesa": {"type": "dessert", "base_demand": 10}
}

# Feriados nacionais aproximados (exemplos)
holidays = [
    "2024-10-12", "2024-11-02", "2024-11-15", "2024-12-25",
    "2025-01-01", "2025-02-25", "2025-04-18", "2025-05-01",
    "2025-09-07"
]
holidays = pd.to_datetime(holidays)

# Simulação de vendas diárias
data = []

for date in date_range:
    day_of_week = date.weekday()  # 0 = segunda, 6 = domingo
    is_weekend = day_of_week >= 5
    is_holiday = date in holidays

    for product_name, product_info in products.items():
        base = product_info["base_demand"]

        # Aumenta a demanda em finais de semana e feriados
        multiplier = 1.0
        if is_weekend:
            multiplier += 0.5
        if is_holiday:
            multiplier += 0.75

        # Adiciona variação aleatória
        quantity_sold = int(np.random.normal(loc=base * multiplier, scale=5))
        quantity_sold = max(quantity_sold, 0)

        data.append({
            "Data": date.date(),
            "Dia da Semana": date.strftime("%A"),
            "Produto": product_name,
            "Categoria": product_info["type"],
            "Quantidade Vendida": quantity_sold
        })

# Cria o DataFrame
df = pd.DataFrame(data)

# Salva em CSV
df.to_csv("vendas_hamburgueria.csv", index=False)

print("Arquivo CSV 'vendas_hamburgueria.csv' gerado com sucesso!")
