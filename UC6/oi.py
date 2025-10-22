import random
from datetime import datetime, timedelta

# Configurações
start_date = datetime(2024, 1, 1)
num_days = 365
produtos = [
    (1, 'Pão de Hambúrguer', 'Pão', 'unidade', 200, 1.50),
    (2, 'Carne de Hambúrguer', 'Carne', 'kg', 50, 20.00),
    (3, 'Queijo', 'Queijo', 'kg', 30, 15.00),
    (4, 'Bebida', 'Bebida', 'litro', 100, 5.00),
    (5, 'Tomate', 'Vegetal', 'unidade', 150, 2.00)
]

feriados = [
    '2024-01-01', '2024-04-21', '2024-05-01', '2024-09-07',
    '2024-10-12', '2024-11-02', '2024-11-15', '2024-12-25'
]

def is_feriado(date):
    return date.strftime('%Y-%m-%d') in feriados

# SQL insert inicial para Produtos
sql_statements = []
sql_statements.append("-- Produtos")
sql_statements.append("INSERT INTO Produtos (id_produto, nome, categoria, unidade_medida, quantidade_estoque, preco_unitario) VALUES")
sql_statements.append(",\n".join(
    f"({p[0]}, '{p[1]}', '{p[2]}', '{p[3]}', {p[4]}, {p[5]:.2f})" for p in produtos
) + ";")

# Entradas_Estoque: compras semanais para cada produto (toda segunda-feira)
sql_statements.append("\n-- Entradas_Estoque")
id_entrada = 1
for day_offset in range(0, num_days, 7):
    date = start_date + timedelta(days=day_offset)
    for p in produtos:
        qty = random.randint(20, 100)
        preco_compra = round(p[5] * random.uniform(0.7, 0.9), 2)  # compra mais barata que venda
        sql_statements.append(
            f"INSERT INTO Entradas_Estoque (id_entrada, id_produto, data_entrada, quantidade, fornecedor, preco_compra_unitario) "
            f"VALUES ({id_entrada}, {p[0]}, '{date.strftime('%Y-%m-%d')}', {qty}, 'Fornecedor {chr(65+p[0])}', {preco_compra});"
        )
        id_entrada += 1

# Pedidos diários, 5 a 15 pedidos por dia
sql_statements.append("\n-- Pedidos")
id_pedido = 1
pedidos_por_dia = []
for day_offset in range(num_days):
    date = start_date + timedelta(days=day_offset)
    weekday = date.strftime('%A')  # dia da semana em inglês (Monday, ...)
    fer = is_feriado(date)
    num_pedidos = random.randint(5, 15)
    for _ in range(num_pedidos):
        hora = random.randint(10, 22)
        minuto = random.randint(0, 59)
        segundo = random.randint(0, 59)
        sql_statements.append(
            f"INSERT INTO Pedidos (id_pedido, data_pedido, hora_pedido, dia_semana, feriado, valor_total) "
            f"VALUES ({id_pedido}, '{date.strftime('%Y-%m-%d')}', '{hora:02d}:{minuto:02d}:{segundo:02d}', '{weekday}', {int(fer)}, 0);"
        )
        pedidos_por_dia.append((id_pedido, date, fer, weekday))
        id_pedido += 1

# Itens_Pedido e Saidas_Estoque
sql_statements.append("\n-- Itens_Pedido e Saidas_Estoque")
id_item = 1
id_saida = 1
valor_totais_pedido = {}

for pedido_info in pedidos_por_dia:
    pedido_id, date, fer, weekday = pedido_info
    num_itens = random.randint(1, 4)
    total_pedido = 0.0
    for _ in range(num_itens):
        produto = random.choice(produtos)
        prod_id = produto[0]
        preco_venda = round(produto[5] * random.uniform(1.1, 1.5), 2)  # markup na venda
        quantidade = random.randint(1, 5)
        total_item = preco_venda * quantidade
        total_pedido += total_item
        sql_statements.append(
            f"INSERT INTO Itens_Pedido (id_item, id_pedido, id_produto, quantidade, preco_venda_unitario) "
            f"VALUES ({id_item}, {pedido_id}, {prod_id}, {quantidade}, {preco_venda});"
        )
        sql_statements.append(
            f"INSERT INTO Saidas_Estoque (id_saida, id_produto, data_saida, quantidade, referencia_pedido) "
            f"VALUES ({id_saida}, {prod_id}, '{date.strftime('%Y-%m-%d')}', {quantidade}, {pedido_id});"
        )
        id_item += 1
        id_saida += 1
    valor_totais_pedido[pedido_id] = total_pedido

# Atualizar valor_total dos pedidos
sql_statements.append("\n-- Atualização dos valores totais dos pedidos")
for pedido_id, valor_total in valor_totais_pedido.items():
    sql_statements.append(
        f"UPDATE Pedidos SET valor_total = {valor_total:.2f} WHERE id_pedido = {pedido_id};"
    )

# Previsao_Demanda para 30 dias após o período
sql_statements.append("\n-- Previsao_Demanda")
id_previsao = 1
for day_offset in range(num_days, num_days + 30):
    date = start_date + timedelta(days=day_offset)
    weekday = date.strftime('%A')
    fer = is_feriado(date)
    tipo_dia = 'feriado' if fer else ('fim de semana' if weekday in ['Saturday', 'Sunday'] else 'semana')
    for p in produtos:
        qtd_prevista = random.randint(20, 60) if tipo_dia != 'semana' else random.randint(10, 40)
        sql_statements.append(
            f"INSERT INTO Previsao_Demanda (id_previsao, id_produto, data_prevista, quantidade_prevista, tipo_dia) "
            f"VALUES ({id_previsao}, {p[0]}, '{date.strftime('%Y-%m-%d')}', {qtd_prevista}, '{tipo_dia}');"
        )
        id_previsao += 1

# Salvar em arquivo SQL
with open('dados_hamburgueria_1ano.sql', 'w', encoding='utf-8') as f:
    f.write("\n".join(sql_statements))

print("Arquivo SQL com dados para 1 ano criado: dados_hamburgueria_1ano.sql")
