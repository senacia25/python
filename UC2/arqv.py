# try:
#     with open("UC2/arquivos/exemplo.txt") as novo_aquivo:
#         # conteudo = novo_aquivo.read()
#         # print(conteudo)
        
#         for linha in novo_aquivo:
#             print(linha) 
# except FileNotFoundError:
#     print("Arquivo não encontrado")


#Atv: 1

# try:
#     def maior():
                        
#         with open("UC2/arquivos/numeros.txt")as maior_numero:
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

with open("UC2/arquivos/pessoas.csv")as novo_numero:
    for linha in novo_numero:
        linha = linha.replace("\n", "")
        partes = linha.split(";")
        nome = partes[0]
        notas = partes[1:]
        print(f"Nome: {nome}\nNotas: {notas}")
        
        