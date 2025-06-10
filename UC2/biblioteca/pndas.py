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
        
# lancamento = df_filme[df_filme["Released_Year"] >= "2016"]
# print("\n4. Filmes a partir de 2016")
# print(lancamento["Released_Year"].head())
                                      
            
     
     
     
     
              
                                 
                                                 
                                                 
                                                 