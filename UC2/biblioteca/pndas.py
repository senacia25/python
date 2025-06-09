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


#Ex:
import pandas as pd

netflix = "UC2/biblioteca/netflix_titles.csv"

df_netflix = pd.read_csv(netflix)

print("primeiras 7 linhas:\n",df_netflix.head(7))
print(df_netflix.info())
print(df_netflix.shape[0],"linhas",df_netflix.shape[1],"colunas")
print(df_netflix.describe())


