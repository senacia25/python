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
# strip igual a replace
# split trasnfoma em lista

# try:
#     with open("UC2/arquivos/dados.csv", "r") as arquivo:
#         with open("UC2/arquivos/dados_maiores.csv", "w") as arquivo_saida:
#             for linha in arquivo:
#                 linha = linha.replace("\n","")
#                 if linha:
#                     print(linha)
#                     partes = linha.split(",")
#                     nome = partes[0]
#                     idade = partes[1]
#                     if len(idade) <= 3:
#                         if int(idade) >= 18:
#                             arquivo_saida.write(linha +"\n")
#         print("Arquivo 'dados_maiores' criado com sucesso!")
        
# except FileNotFoundError:
#     print("Arquivo 'dados.csv' não encontrado.")
    
# except ValueError:
#     print("Erro: varifique se o arquivo está no formato 'nome,idade'.")                    
    

#===========
#** os operation system sistema operacional

# import os

# #os.remove("UC2/dados.txt")" remove arquivo"

# if os.path.exists("UC2/apagar"): # ver se existe pasta
#     print("sim, a pasta existe")
#     os.rmdir("UC2/apagar") # apaga diretorio
    
# else:
#     print("Pasta não existe")
#     os.mkdir("UC2/Numpy") #cria diretorio
#=======

#Atv: 6

#dá pra criar um loop pra ficar retindo até sair

# def adc_diario():
    
#     data = input("Digite a data: ")
#     descricao = input("Digite a discrição: ")
    
#     entrada = {"data": data,
#                "descricao": descricao}
    
#     with open("UC2/arquivos/diario.txt", "a", encoding="utf-8") as arquivo:
#         arquivo.write(str(f"\nData: {entrada["data"]} - Descrição: {entrada["descricao"]}")) # coloquei o 'str' para pular só uma linha
    
#     print("Entrada adicionada em 'diario.txt' com sucesso! ")
        
# adc_diario()




