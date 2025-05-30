#Dicionário
#usado para dados no formato: Chave:valor
#São ordenas, mutáveis, não permite elementos duplicados

# meu_dicionario = {}
# meu_dicionario["apina"] = "macaco"
# meu_dicionario["nome"] = "jorge"

# print(meu_dicionario)
# print(meu_dicionario["nome"])

# palavra = input("digite uma palavra: ")

# if palavra in meu_dicionario:
#     print("tradução:", meu_dicionario[palavra])

# else:
#     print("palavra não encontrada")
    
    
# resultado = {}
# resultado["maria"] = 5
# resultado["julia"] = 10

# soma =  resultado["maria"] + resultado["julia"]
# print(soma)


#imprimir chave:valor

# dicionario = {}
# dicionario["apina"] = "macaco"
# dicionario["banana"] = "amarela"
# dicionario["cembalo"] = "cravo"

# for chave in dicionario:
#     print("chave", chave)
#     print("valor", dicionario[chave])


# lista_palavras = [
#   "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
#   "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
#   "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
# ]
# def contagens(minha_lista):
#     palavras = {} # "chave":"valor"
#     for palavra in minha_lista:
#         if palavra not in palavras:
#             palavras[palavra] = 0
            
#         palavras[palavra] += 1
#     return palavras

# print(contagens(lista_palavras))

# #Ex:

# def histogram(a):
#     cont = {}                      
#     for letra in a:                           
#         if letra in cont:                  
#             cont[letra] += 1
#         else:
#             cont[letra] = 1
           
#     for letra in cont:
#         print(f"{letra + ": "}{"*" * cont[letra]}")
          
# histogram("abba")


#Atv: 1

# usuario = {}

# def menu():
#     print("1. Buscar")
#     print("2. Adicionar")
#     print("3. Sair")
        
# while True:
#     menu()
#     opcao = int(input("digite a opção: "))
        
#     if opcao == 3:
#         print("Saindo...")
#         break
    
#     elif opcao == 2:
#         nome = input("digite o nome: ")
#         numero = int(input("digite o número: "))
#         usuario[nome] = numero
#         print(f"Nome: {nome}\nNúmero: {numero}")
        
#     elif opcao == 1:
#         nome = input("nome: ")
#         if nome in usuario:
#             print("Número:" , usuario[nome])
#         else:
#             print("Nenhum número")
        
#     else:
#         print("Opção inválida! ")
        
# #Prof:

# def lista_telefonica():
#     agenda = {}  
 
#     while True:
#         comando = input("Comando (1 busca, 2 adiciona, 3 sai): ")
 
#         if comando == "1":
#             nome = input("nome: ")
#             if nome in agenda:
#                 print("número:", agenda[nome])
#             else:
#                 print("nenhum número")
 
#         elif comando == "2":
#             nome = input("nome: ")
#             numero = input("número: ")
#             agenda[nome] = numero
#             print("ok!")
#         elif comando == "3":
#             print("saindo...")
#             print(agenda)
#             break
#         else:
#             print("Comando inválido. Tente novamente.")          
# lista_telefonica()
        

#Atv: 2

# usuario = {}

# def menu():
#     print("1. Buscar")
#     print("2. Adicionar")
#     print("3. Sair")
        
# while True:
#     menu()
#     opcao = int(input("digite a opção: "))
        
#     if opcao == 3:
#         print("Saindo...")
#         break
    
#     elif opcao == 2:
#         nome = input("digite o nome: ")
#         numero = int(input("digite o número: "))

#         if nome in usuario:
#             usuario[nome].append(numero)

#         else:              
#             usuario[nome] = [numero]
#         print(f"Nome: {nome}\nNúmero: {numero}")
        
#     elif opcao == 1:
#         nome = input("nome: ")
#         if nome in usuario:
#             print("Número:" , usuario[nome])
#         else:
#             print("Nenhum número")
        
#     else:
#         print("Opção inválida! ")

# testar
# elif opcao == 1:
#     nome = input("Digite o nome: ")
#     if nome in usuario:
#         print("Números:")
#         for num in usuario[nome]:
#             print(num)
#     else:
#         print("Nenhum número cadastrado para esse nome.")

        

#ex:
#Deletando chave
#del **

# staff = {"alan": "Professor","emily": "aluna", "joao": "professor"}

# print(staff)

# del staff ["alan"]
# print(staff)

# #pop
# #pop armazena o valor deletado, podemos gravar em uma variavel

# deletado = staff.pop("emily")
# print(deletado)

# #Estruturar dados com dicionário

# pessoa1 = {"nome": "Peppa Pig","Altura":125,"Peso": 546,"idade":54}
# pessoa2 = {"nome": "Lilo Stitch","Altura":847,"Peso": 474,"idade":5}
# pessoa3 = {"nome": "Ariel","Altura":25,"Peso": 6,"idade":74}

# pessoas = [pessoa1, pessoa2, pessoa3]

# for pessoa in pessoas:
#     print(f"Nome: {pessoa["nome"]}")
#     print(f"Altura: {pessoa["Altura"]}")
#     print(f"Peso: {pessoa["Peso"]}")
#     print(f"Idade: {pessoa["idade"]}")
#     print(" ")
    
# altura_combinada = 0

# for pessoa in pessoas:
#     altura_combinada += pessoa["Altura"]
    
# print(altura_combinada)

#Atv: 3

def ivert(dicionario: dict):
    invertido = {}
    




