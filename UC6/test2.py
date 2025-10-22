import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# ---------- CONFIGURAÇÕES ----------
random.seed(42)
start_date = datetime(2024, 1, 1)
num_days = 365
feriados = pd.to_datetime([
    '2024-01-01', '2024-04-21', '2024-05-01',
    '2024-09-07', '2024-10-12', '2024-11-02',
    '2024-11-15', '2024-12-25'
])

# ---------- TABELA: Produtos ----------
produtos = pd.DataFrame([
    {'id_produto': 1, 'nome': 'Pão de Hambúrguer', 'categoria': 'Pão', 'unidade_medida': 'unidade', 'quantidade_estoque': 200, 'preco_unitario': 1.50},
    {'id_produto': 2, 'nome': 'Carne de Hambúrguer', 'categoria': 'Carne', 'unidade_medida': 'kg', 'quantidade_estoque': 50, 'preco_unitario': 20.00},
    {'id_produto': 3, 'nome': 'Queijo', 'categoria': 'Queijo', 'unidade_medida': 'kg', 'quantidade_estoque': 30, 'preco_unitario': 15.00},
    {'id_produto': 4, 'nome': 'Bebida', 'categoria': 'Bebida', 'unidade_medida': 'litro', 'quantidade_estoque': 100, 'preco_unitario': 5.00},
    {'id_produto': 5, 'nome': 'Tomate', 'categoria': 'Vegetal', 'unidade_medida': 'unidade', 'quantidade_estoque': 150, 'preco_unitario': 2.00}
])

# ---------- Funções Auxiliares ----------
def is_feriado(data):
    return data in feriados

def dia_tipo(data):
    if is_feriado(data):
        return 'feriado'
    elif data.weekday() >= 5:
        return 'fim de semana'
    else:
        return 'semana'

# ---------- Inicializando Tabelas ----------
entradas = []
pedidos = []
itens_pedido = []
saidas = []
previsoes = []

id_entrada = id_pedido = id_item = id_saida = id_previsao = 1

# ---------- LOOP DE 365 DIAS ----------
for dia in range(num_days):
    data = start_date + timedelta(days=dia)
    dia_semana = data.strftime('%A')
    tipo_dia = dia_tipo(data)

    # Simular ENTRADAS (compras) toda segunda
    if data.weekday() == 0:
        for _, produto in produtos.iterrows():
            quantidade = random.randint(20, 100)
            preco_compra = round(produto['preco_unitario'] * random.uniform(0.7, 0.9), 2)
            entradas.append({
                'id_entrada': id_entrada,
                'id_produto': produto['id_produto'],
                'data_entrada': data,
                'quantidade': quantidade,
                'fornecedor': f'Fornecedor {chr(65 + produto["id_produto"])}',
                'preco_compra_unitario': preco_compra
            })
            id_entrada += 1

    # Simular PEDIDOS (vendas)
    num_pedidos = random.randint(5, 15)
    for _ in range(num_pedidos):
        valor_total = 0
        this_pedido = {
            'id_pedido': id_pedido,
            'data_pedido': data,
            'hora_pedido': f"{random.randint(10,22)}:{random.randint(0,59):02}",
            'dia_semana': dia_semana,
            'feriado': is_feriado(data),
            'valor_total': 0
        }

        num_itens = random.randint(1, 4)
        produtos_usados = produtos.sample(num_itens)
        for _, produto in produtos_usados.iterrows():
            qtd = random.randint(1, 5)
            preco_venda = round(produto['preco_unitario'] * random.uniform(1.2, 1.5), 2)
            subtotal = preco_venda * qtd
            valor_total += subtotal

            itens_pedido.append({
                'id_item': id_item,
                'id_pedido': id_pedido,
                'id_produto': produto['id_produto'],
                'quantidade': qtd,
                'preco_venda_unitario': preco_venda
            })

            saidas.append({
                'id_saida': id_saida,
                'id_produto': produto['id_produto'],
                'data_saida': data,
                'quantidade': qtd,
                'referencia_pedido': id_pedido
            })

            id_item += 1
            id_saida += 1

        this_pedido['valor_total'] = round(valor_total, 2)
        pedidos.append(this_pedido)
        id_pedido += 1

# ---------- Previsão de Demanda ----------
for dia in range(num_days, num_days + 30):
    data = start_date + timedelta(days=dia)
    tipo_dia = dia_tipo(data)
    for _, produto in produtos.iterrows():
        qtd_prevista = random.randint(10, 40) if tipo_dia == 'semana' else random.randint(20, 60)
        previsoes.append({
            'id_previsao': id_previsao,
            'id_produto': produto['id_produto'],
            'data_prevista': data,
            'quantidade_prevista': qtd_prevista,
            'tipo_dia': tipo_dia
        })
        id_previsao += 1

# ---------- Criar DataFrames ----------
df_entradas = pd.DataFrame(entradas)
df_pedidos = pd.DataFrame(pedidos)
df_itens = pd.DataFrame(itens_pedido)
df_saidas = pd.DataFrame(saidas)
df_previsoes = pd.DataFrame(previsoes)

# ---------- Exemplo de uso ----------
print("📦 Entradas de estoque:")
print(df_entradas.head())

print("\n🧾 Pedidos:")
print(df_pedidos.head())

print("\n📤 Saídas de estoque:")
print(df_saidas.head())

print("\n📈 Previsão de Demanda:")
print(df_previsoes.head())

# Salvar em CSV se quiser
# df_entradas.to_csv("entradas_estoque.csv", index=False)
# df_pedidos.to_csv("pedidos.csv", index=False)
# df_itens.to_csv("itens_pedido.csv", index=False)
# df_saidas.to_csv("saidas_estoque.csv", index=False)
# df_previsoes.to_csv("previsao_demanda.csv", index=False)
