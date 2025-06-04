# try:
#     with open("UC2/arquivos/exemplo.txt") as novo_aquivo:
#         # conteudo = novo_aquivo.read()
#         # print(conteudo)
        
#         for linha in novo_aquivo:
#             print(linha) 
# except FileNotFoundError:
#     print("Arquivo não encontrado")


#ex

# try:
#     def maior():
                        
#         with open("UC2/arquivos/numeros.txt") as maior_numero:
#            maior = 0
#            for linha in maior_numero:
#                numero = int(linha)
#                if numero > maior:
#                    maior = numero
                   
#         print("Maior número", maior)
                                                           
# except FileNotFoundError:
        
#     print("Arquivo não encontrado")
  
# maior()

#====
       

# with open("UC2/arquivos/pessoas.csv") as novo_numero:
#     for linha in novo_numero:
#         linha = linha.replace("\n", "")#substitui
#         partes = linha.split(";")# converte ponto e virgula e cria uma lista
#         nome = partes[0]
#         notas = partes[1:]
#         print(f"Nome: {nome}\nNotas: {notas}")
        

#Atv: 1

# frutas = {}

# with open("UC2/arquivos/frutas.csv") as lista_frutas:
       
#     for linha in lista_frutas:
        
#         nome, preco = linha.split(";") 
#         frutas[nome] = float(preco) 
         
#         #dados = linha.split(";")
#         #frutas[dados[0]] = float(dados[1])    
        
#     print(frutas)
       
#prof

# def frutas():
#     dicionario_frutas = {}
    
#     try:
#         with open("UC2/arquivos/frutas.csv") as arquivo:
#             for linha in arquivo:
#                 linha = linha.replace("\n", "")
#                 if linha:
#                     dados = linha.split(";")
#                     dicionario_frutas[dados[0]] = float(dados[1])
                    
#     except FileNotFoundError:
#         print("Arquivo 'frutas.csv' não encontrado.")
        
#     except ValueError:
#         print("Erro ao converter o preço para float.")
        
#     return dicionario_frutas

# print(frutas())
        

#=====

#ler a linha especifica
# with open("UC2/dados.txt") as arquivo:
#     f = arquivo.readlines()
#     print(f[1]) 

#adicionar uma nova linha
#with open("UC2/dados.txt","a") as arquivo: #a adiciona um anova linha onde ja existe 
#    f = arquivo
#    f = arquivo.write("\nNova linha, aqui!")
#
##excluir    
#with open("UC2/dados.txt","w") as arquivo: #w excluir toda a linha e adciona um nova so e ecxlcui o rsto 
#    f = arquivo
#    f = arquivo.write("\nNova linha, aqui!")

# criar novo arquivo direto   
# with open("UC2/dados2.txt","x") as arquivo: #x cria novo arquivo  
#     f = arquivo
#     f = arquivo.write("\nNova linha, aqui!")
    

#======

#Atv: 2

# with open("UC2/arquivos/saida.txt","a", encoding="utf-8") as arquivo:  #encoding="utf-8" para tirar o erro da palvra com acento
    
#     f = arquivo
#     tex = input("Escreva o texto aqui: ")
#     f = arquivo.write(f"\n {tex}")  # \n coloquei o \n para escrever na proxima linha


#Atv: 3

# with open("UC2/arquivos/numeros.txt") as numero:
#     conteudo = numero.read()
#     print(conteudo)


#Atv: 4

# try:
#     with open("UC2/arquivos/numeros.txt") as numero:
#         total_linhas = 0
#         for linha in numero:
#             total_linhas += 1
            
#     print(total_linhas)
        
# except FileNotFoundError:
#     print("O arquivo 'numeros.txt' não foi encontrado.")
    

#Atv: 5


    