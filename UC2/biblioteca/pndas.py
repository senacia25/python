# import pandas as pd

#criando uma série

# idade = pd.Series([1,2,4,5,6,9])
# print(idade)

# idade_nomes = pd.Series([1,2,4,5], index=["ana", "joão", "maria", "carlos"])
# print(idade_nomes)

#dataframe

# dadosAlunos = {
#     "nome":["ana", "joão", "maria", "carlos"],
#     "idade":[1,2,5,4],
#     "curso":["engenharia", "medicina", "direito", "engenharia"]
# }

# df_alunos= pd.DataFrame(dadosAlunos)
# print(df_alunos)

# import pandas as pd

# url_fillmes = "UC2/biblioteca/IMDB-Movie-Data.csv"

# df_filme = pd.read_csv(url_fillmes)
# # print(df_filme)
# print("dados carregados com sucesso")

# #head() 5 primeira linhas

# print("Primeiras 5 linhas da dataframe")
# print(df_filme.head())

# #tail() 5 ultimas linhas
# print("Ultimas 5 linhas so dataframe de filme")
# print(df_filme.tail())

# #info()
# print("Informações sobre o dataframe")
# print(df_filme.info())

# # shape dimensoes
# print(f"o dataframe de filme tem {df_filme.shape[0]} linhas e {df_filme.shape[1]} colunas")

# #describe() - gera estatistica do dataframe
# print("estatistica descritiva do dataframe")
# print(df_filme.describe())

# #index - trás informações sobre os indice das linhas
# print("Informações do indice")
# print(df_filme.index)


#Atv: 1
# import pandas as pd

# netflix = "UC2/biblioteca/netflix_titles.csv"

# df_netflix = pd.read_csv(netflix)

# print("primeiras 7 linhas:\n",df_netflix.head(7))
# print(df_netflix.info())
# print(df_netflix.shape[0],"linhas",df_netflix.shape[1],"colunas")
# print(df_netflix.describe())                                                       


#Selecionar a coluna 'title'
# import pandas as pd
# url_fillmes = "UC2/biblioteca/IMDB-Movie-Data.csv"
# df_filme = pd.read_csv(url_fillmes)

# titulo_filmes = df_filme["Series_Title"]
# print("primeiros 5 títulos")
# print(titulo_filmes.head())

# #Selecionar multiplas coluna 

# titulo_selecionados = df_filme[["Series_Title", "Genre", "IMDB_Rating"]]
# print("Dataframe com título, Gênero e Nota")
# print(titulo_selecionados.head())

# #Selecionando a primeira linha
# #Iloc é usado para selecionar linhas por indice numérico
# primeiro_filme = df_filme.iloc[0] # uma linha ou [0:3] as três primeiras
# print("Primeiro filme(linha completa):")
# print(primeiro_filme)

# #Slecionando linhas e colunas específicas
# selecao_especifica = df_filme.iloc[[0,3],[5,6]]
# print("Printando uma seleção específica, linha 0 e 3 e coluna 5 e 6")
# print(selecao_especifica)

# #Selecionando dados com .loc
# #Localizar os dados pelo rótulos.

# df_filme_idx = df_filme.set_index("Series_Title")# Redefinir o indice como nome do filme pra chamar pelo .loc pelo nome
# print("Definimos o índice agora como Series title")
# print(df_filme_idx.head())

# poderoso = df_filme_idx.loc["The Godfather"]
# print("Dados do filme: The Godfather: ") 
# print(poderoso) 
 
#  #Filtrar os dados baseados em condiçôes (Boolenan indexin0)
# df_filme_bem_avaliados = df_filme[df_filme["IMDB_Rating"] >= 8.5]
# print("Filmes com nora >= 8.5 (Primeirs linhas)")
# print(df_filme_bem_avaliados["Series_Title"].head())#[["Series_Title","Genre"]] TRazer mais informações dois colchetes

# #filmes que tem gênero "Action"
# filme_acao = df_filme[df_filme["Genre"].str.contains("Action",na=False)]
# print("\n Filmes que contêm o Gênero 'action'")
# print(filme_acao[["Series_Title", "Genre"]].head())


#Atv: 2
# import pandas as pd

# url_fillmes = "UC2/biblioteca/IMDB-Movie-Data.csv"
# df_filme = pd.read_csv(url_fillmes)

# colunas = df_filme[["Series_Title", "Director", "Released_Year"]]
# print("\n1. Apenas as coluna do title, director e year das primeiras 5 linhas")
# print(colunas.head())

# linha_coluna = df_filme.iloc[10:16, 0:4]
# print("\n2. Linha 10 e 15 e coluna 0 e 3")
# print(linha_coluna)

# #df_temp = df_filme.set_index("IMDB_Rating")
# top_5_rank = df_filme.loc[0:5, ["Series_Title", "Gross"]]
# print("\n3. Filme de rank 1 a 5 com receita:")
# print(top_5_rank.head())
        
# #4 outra forma convertter para número        
# df_filme["Released_Year"] = pd.to_numeric(df_filme["Released_Year"],errors="coerce")
        
# lancamento = df_filme[df_filme["Released_Year"] >= 2016]
# print("\n4. Filmes a partir de 2016")
# print(lancamento["Released_Year"].head())

# #4 === 2016 fiz como string e funcionou mas não é muuito aconcelhavel, fazer da forma anterior
# lancamento = df_filme[df_filme["Released_Year"] >= "2016"]
# print("\n4. Filmes a partir de 2016")
# print(lancamento["Released_Year"].head())
                                      

#===========                                                  
#Criar uma nova coluna
# import pandas as pd
      
# url_fillmes = "UC2/biblioteca/IMDB-Movie-Data.csv"
# df_filme = pd.read_csv(url_fillmes)

# df_filme["Rating_x_10"] = df_filme["IMDB_Rating"] * 10
# print("\n O Dataframe agora tem uma nova coluna")
# print(df_filme.head())

# #Conversão de coluna Gross para float e ignorando erros casos falhar
# df_filme["Gross"] = pd.to_numeric(df_filme["Gross"], errors="coerce")
                              
# #Agora, convertido o número gross em número, é mais seguro fazer comparações
# df_filme["Alta_receita"] = df_filme["Gross"] > 1000
# print("\n Dataframe com nova coluna 'Alta Receita(Primeira linha)")              
# print(df_filme.head())              
                                               
# #Drop - metodo drop remove uma linha (registro) da coluna
# df_filme = df_filme.drop("Poster_Link", axis=1) # "axis 0 linha axis 1 coluna"       
# print(df_filme.head())

# #axis = 0 -exclui o registro
# df_filme = df_filme.drop(4,axis=0)
# print(df_filme.head())                                        
                              

#Atv: 3
# import pandas as pd

# url_fillmes = "UC2/biblioteca/IMDB-Movie-Data.csv"
# df_filme = pd.read_csv(url_fillmes)


# df_filme["Rating_Metascore_Diff"] = df_filme["IMDB_Rating"] - (df_filme["Meta_score"] / 10)
# print("\n O Dataframe agora tem uma nova coluna")
# print(df_filme.head())


# colunas = df_filme[["Series_Title", "IMDB_Rating", "Meta_score", "Rating_Metascore_Diff"]]
# print("\n1. Coluna do title, Rating, matescore e rating metascore diff primeiras 5 linhas")
# print(colunas.head())

# #Criar um novo dataframe sem a coluna "overview"
# df_filme_sem_overview = df_filme.drop(columns=["Overview"])

# #renomear com inplace=True
# df_filme.rename(columns={"No_of_votes":"Numero_votos"}, inplace=True)

# #verificar se foi renomeada
# print("\n Verificação das colunas após renomear 'no_of-vote':")
# print(df_filme.columns.tolist())


#===
#Lidando com dados Ausentes
#verificar dados ausentes com .isna() . sum()

# import pandas as pd

# url_fillmes = "UC2/biblioteca/IMDB-Movie-Data.csv"
# df_filme = pd.read_csv(url_fillmes)


# print("\n Contagem de valores ausentes por coluna")
# print(df_filme.isna().sum()) #isna pra saber se tem numero ausente

# #Removendo linhas/colunas
# #Criando uma cópia para nan(not a number numero ausente)
# def_sem_nan_linhas = df_filme.copy()

# #Removendo todas as linhas que contanhm qualquer valor Nan
# def_sem_nan_linhas.dropna(inplace=True)
# print(f"\nNúmero de linhas original: {len(df_filme)}")
# print(f"\nNúmero de linhas após drop: {len(def_sem_nan_linhas)}")

# #Removendo colunas que tenham qualquer valor Nan
# def_sem_nan_linhas = df_filme.dropna(axis=1)
# print(f"\ncoluna originais : {df_filme.columns.tolist()}")
# print(f"\nColunas após dropna: {def_sem_nan_linhas.columns.tolist()}")


#Atv: 4
# import pandas as pd

# url_fillmes = "UC2/biblioteca/IMDB-Movie-Data.csv"
# df_filme = pd.read_csv(url_fillmes)


# print("Valores ausentes por colunas:")
# print(df_filme[["Gross","Meta_score"]].isna().sum())

# df_filme_completos = df_filme.dropna()

# print(f"\nNúmero de linha no Dataframe original: {len(df_filme)}")
# print(f"Número de linhas após remover todas com Nan: {len(df_filme_completos)}")

# #Garantindo que as colunas estão númericas

# df_filme["Gross"] = pd.to_numeric(df_filme["Gross"], errors="coerce")# coerce força a mudança pra numerco
# df_filme["Mera_score"] = pd.to_numeric(df_filme["Meta_score"], errors="coerce")

# # Criando a cópia do Dataframe
# df_filme_preenchido_media = df_filme.copy()

# #Preenchendo os nans 
# df_filme_preenchido_media["Gross"] = df_filme_preenchido_media["Gross"].fillna(df_filme_preenchido_media["Gross"].mean()) #fill na fill prencher e na valores que nao existe preenche com mean                                      
# df_filme_preenchido_media["Meta_score"] = df_filme_preenchido_media["Meta_score"].fillna(df_filme_preenchido_media["Meta_score"].median())

# #verificando se ainda existem NaNs nessa colunas
# print("\nValores ausentes após preenchimento: ")
# print(df_filme_preenchido_media[["Gross", "Meta_score"]].isna().sum())

#outra

# url_fillmes = "UC2/biblioteca/IMDB-Movie-Data.csv"
# df_filme = pd.read_csv(url_fillmes)

# print("Valores ausentes por coluna:")
# print(df_filme[['Gross', 'Meta_score']].isna().sum())
 
# df_filmes_completo = df_filme.dropna()
 
# print(f"\nNúmero de linhas no DataFrame original: {len(df_filme)}")
# print(f"Número de linhas após remover todas com NaN: {len(df_filmes_completo)}")
 
# # Garantindo que as colunas estão numéricas
# df_filmes_completo['Gross'] = df_filmes_completo['Gross'].str.replace(',','.')
# df_filmes_completo['Gross'] = pd.to_numeric(df_filmes_completo['Gross'], errors='coerce')
# df_filmes_completo['Meta_score'] = pd.to_numeric(df_filmes_completo['Meta_score'], errors='coerce')
# print(df_filmes_completo['Gross'])
# # Criando uma cópia do DataFrame original
# df_filmes_preenchido_media = df_filmes_completo.copy()
 
# # Preenchendo os NaNs
# df_filmes_preenchido_media['Gross'] = df_filmes_preenchido_media['Gross'].fillna(df_filmes_preenchido_media['Gross'].mean())
# df_filmes_preenchido_media['Meta_score'] = df_filmes_preenchido_media['Meta_score'].fillna(df_filmes_preenchido_media['Meta_score'].mean())
 
# # Verificando se ainda existem NaNs nessas colunas
# print("\nValores ausentes após preenchimento:")
# print(df_filmes_preenchido_media[['Gross', 'Meta_score']].isna().sum())
 
 
#====== 
 
# import pandas as pd

# url_fillmes = "UC2/biblioteca/IMDB-Movie-Data.csv"
# df_filme = pd.read_csv(url_fillmes)
 
# #Contando as frequêcia de colunas
# contagem_diretores = df_filme["Director"].value_counts()
# print("\nOS 10 diretores mais frequentes")
# print(contagem_diretores.head(10))

# #Ordenando filmes pela nota (IMDB_Rating)
# df_ordenado_por_nota = df_filme.sort_values(by="IMDB_Rating",ascending=False)
# print("\nTop 5 filmes por nota (IMDB_Rating)")
# print(df_ordenado_por_nota.head())

# #Ordenando filmes por mais de um coluna
# df_ordenado_por_duas_colunas = df_filme.sort_values(by=["Released_Year","Gross"],ascending=[False,True])
# print("\nTop 5 filmes por ano e gross")
# print(df_ordenado_por_duas_colunas.head())

# #Converter caso necessário

# df_filme["Gross"] = pd.to_numeric(df_filme["Gross"].str.replace(",",""))
# df_filme["Gross"] = pd.to_numeric(df_filme["Gross"], errors="coerce")
# df_filme["IMDB_Rating"] = pd.to_numeric(df_filme["IMDB_Rating"], errors="coerce")

# #Calculando a media de IMDB e Gross para cada Released_Year=======mean- media / agg-agregar
# metrica_por_ano = df_filme.groupby("Released_Year").agg(
#     Media_Rating=("IMDB_Rating","mean"),
#     Media_Receita=("Gross","mean"),
#     Media_filmes=("Series_Title","count"))

# print(metrica_por_ano)

# #Salvando em um arquivo csv sem o indice
# df_filme.to_csv("UC2/biblioteca/meus_filmes_bem_avaliados.csv",index=False)
# print("znDataframe salvo  em 'UC2/biblioteca/meus_filmes_bem_avaliados.csv'")


#Atv: 5

import pandas as pd

url_fillmes = "UC2/biblioteca/IMDB-Movie-Data.csv"
df_filme = pd.read_csv(url_fillmes)

#1 
contagem_diretores = df_filme["Director"].value_counts()
print("\nOS 5 diretores mais frequentes")
print(contagem_diretores.head())

#2
df_filme["Runtime"] = df_filme["Runtime"].str.replace("min","")
df_filme["Runtime"] = pd.to_numeric(df_filme["Runtime"], errors="coerce")

tempo_filme = df_filme.sort_values(by="Runtime",ascending=False)
print("\n10 filmes mais longos: ")
print(tempo_filme.head(10))

#3
ordenar = df_filme.sort_values(by=["Certificate","Meta_score"],ascending=[False,True])
print("\nCertificate ordem alfabetica meta-score ordem decrecente")
print(ordenar.head())

#4
#df_filme["Meta_score"] = pd.to_numeric(df_filme["Meta_score"].str.replace(",",""))
df_filme["Meta_score"] = pd.to_numeric(df_filme["Meta_score"], errors="coerce")
df_filme["Runtime"] = pd.to_numeric(df_filme["Runtime"], errors="coerce")

#5
agrupando = df_filme.groupby("Certificate").agg(
    Media_Runtime=("Runtime","mean"),
    Media_Meta_score=("Meta_score","mean"),
    Total_filmes=("Certificate","count"))
print(agrupando)

#outra

#Contar quantos filmes cada diretor dirigiu
diretores_freq = df_filme['Director'].value_counts().head(5)
print("Diretores com mais filmes:")
print(diretores_freq)
 
# Ordenar os filmes pelo runtime e descrescente
df_filme['Runtime'] = df_filme['Runtime'].str.replace(' min','')
df_filme['Runtime'] = pd.to_numeric(df_filme['Runtime'], errors='coerce')
filmes_mais_longos = df_filme.sort_values(by='Runtime', ascending=False).head(10)
print("\nTop 10 filmes mais longos:")
print(filmes_mais_longos[['Series_Title', 'Runtime']])
 
#Ordenar por 'Certificate' (ordem alfabética) e depois por 'Meta_score's
df_filme['Meta_score'] = pd.to_numeric(df_filme['Meta_score'], errors='coerce')
filmes_ordenados = df_filme.sort_values(by=['Certificate', 'Meta_score'], ascending=[True, False])
print("\nFilmes ordenados por Certificate e Meta_score:")
print(filmes_ordenados[['Series_Title', 'Certificate', 'Meta_score']].head(5))
 
#Agrupamento por 'Certificate'
agrupado = df_filme.groupby('Certificate').agg({
    'Runtime': 'mean',
    'Meta_score': 'mean',
    'Series_Title': 'count'  # contar número de filmes
}).rename(columns={'Title': 'Total_filmes'})
 
print("\nEstatísticas por Certificate:")
print(agrupado)