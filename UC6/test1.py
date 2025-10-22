import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Gerar dados simulados para 1 mês
np.random.seed(42)

# Produtos da hamburgueria
produtos = ['Hamburguer', 'Pão', 'Queijo', 'Batata Frita', 'Refrigerante', 'Milkshake', 'Sobremesa']

# Criar DataFrame com estoque inicial
estoque_inicial = {
    'produto': produtos,
    'estoque': [200, 300, 150, 180, 250, 100, 90]
}
df_estoque = pd.DataFrame(estoque_inicial)

# Criar dados de vendas simuladas para 30 dias
datas = pd.date_range(start='2025-10-01', periods=30)

vendas = []
for data in datas:
    dia_semana = data.weekday()  # 0=segunda, ..., 6=domingo
    for produto in produtos:
        # Venda maior no fim de semana (sábado=5, domingo=6)
        if dia_semana >= 5:
            qtd_vendida = np.random.poisson(8)
        else:
            qtd_vendida = np.random.poisson(3)
        vendas.append({'data': data, 'produto': produto, 'quantidade_vendida': qtd_vendida})

df_vendas = pd.DataFrame(vendas)

# Mostrar os 5 primeiros registros para conferir
print(df_vendas.head())
print(df_estoque)


# Adicionar coluna dia da semana no df_vendas
df_vendas['dia_semana'] = df_vendas['data'].dt.day_name()

# Média de vendas por produto e dia da semana
media_vendas = df_vendas.groupby(['produto', 'dia_semana'])['quantidade_vendida'].mean().reset_index()

print(media_vendas)


# Função para checar estoque baixo para o dia atual
def alerta_estoque(df_estoque, media_vendas, dia_semana):
    alertas = []
    for _, row in df_estoque.iterrows():
        produto = row['produto']
        estoque = row['estoque']
        # Pega média do produto no dia da semana
        media = media_vendas[(media_vendas['produto'] == produto) & (media_vendas['dia_semana'] == dia_semana)]['quantidade_vendida']
        media = media.values[0] if not media.empty else 0
        # Limite de estoque = média * 2 (para 2 dias)
        limite = media * 2
        if estoque < limite:
            alertas.append(f"Estoque BAIXO para {produto}: {estoque} unidades (precisa pelo menos {limite:.1f})")
    return alertas

# Exemplo: alertar para segunda-feira
alertas_segunda = alerta_estoque(df_estoque, media_vendas, 'Monday')
for a in alertas_segunda:
    print(a)


vendas_totais = df_vendas.groupby('produto')['quantidade_vendida'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
vendas_totais.plot(kind='bar', color='orange')
plt.title('Produtos Mais Vendidos no Mês')
plt.ylabel('Quantidade Vendida')
plt.xlabel('Produto')
plt.xticks(rotation=45)
plt.show()


produto_exemplo = 'Hamburguer'
media_produto = media_vendas[media_vendas['produto'] == produto_exemplo]
media_produto = media_produto.set_index('dia_semana').reindex(
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
)

plt.figure(figsize=(8,4))
plt.plot(media_produto.index, media_produto['quantidade_vendida'], marker='o')
plt.title(f'Média de Venda por Dia da Semana: {produto_exemplo}')
plt.ylabel('Média Quantidade Vendida')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
