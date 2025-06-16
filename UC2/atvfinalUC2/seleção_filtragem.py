import pandas as pd
produtos_mercado = "UC2/atvfinal/produtos_mercado.csv"
df_pdmrc = pd.read_csv(produtos_mercado)

#7
cl_produto = df_pdmrc["Produto"]
print("\n====PRODUTOS=====\n")
print("\n",cl_produto)

#8
colunas = df_pdmrc[["Produto","Categoria","Preco_Kg"]]
print("\n",colunas)

#9
linha = df_pdmrc.iloc[109]
print("\n=====Dados ID_produto linha -110=====\n")
print(linha)

#10
verdura = df_pdmrc[df_pdmrc["Categoria"].str.contains("Verdura",na=False)]
print("\n===== VERDURAS =====\n")
print(verdura)

#11
preco = df_pdmrc[df_pdmrc["Preco_Kg"] >= 10.00]
print("\n=====Produtos com preço superior de R$ 10=====\n")
print(preco)

#12
repor = df_pdmrc[df_pdmrc["Data_Ultima_Reposicao"] == "2024-06-01"]
print("\n===== Produto reposto na data 2024-06-01 =====\n\n", repor)

#13
fruta = df_pdmrc[df_pdmrc["Categoria"].str.contains("Fruta",na=False)]
print("\n===== -FRUTAS- FORNERCIDA PELA FAZENDA SOL NASCENTE =====\n")
print(fruta)

#14
kg = df_pdmrc[df_pdmrc["Estoque_Kg"] >= 150]
print("\n===== PRODUTOS MAIORES QUE 150Kg =====\n")
print(kg)