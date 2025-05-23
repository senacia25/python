# minha_lista = [10, 50, 15]
# print(minha_lista[2])

# resultado = minha_lista[0] + minha_lista[2]
# print(resultado)

# tamanhoDaLista = len(minha_lista)
# print(f"Lista tem {tamanhoDaLista} de tamanho")

#Ex
# list = [1, 2, 3, 4, 5]

# while True:
#     ind = int(input("índice: "))
#     if ind < 0:
#         print("Voce saiu")
#         break
#     vl = int(input("valor: "))
#     list[ind] = vl
    
#     print(list)

#Outra forma:
    
# list = [1, 2, 3, 4, 5]

# while True:
#     print(list)
#     ind = int(input("índice: "))
#     if ind == -1:
#         print("saindo")
#         break
#     if 0 <= ind < len(list):
#         vl = int(input("valor: "))
#         list[ind] = vl
    
#     else:
#         print("invalido")

# print(list)
    
#Fatiar lista:
# letra = ["a", "b", "c", "d", "e", "f"]
# print(letra[1:4])#ele corta de 1 até o elemento 4
# print(letra[:3])#conta do inicio até o 3
# print(letra[3:])#do indice 3 até o final
# print(letra[::2])#todos, com passo 2
# print(letra[::-1])# lista invertida

#Adicionar item e lista 

# numero = []
# numero.append(5)
# numero.append(25)
# numero.append(10)
# print(numero)


#Ex:
# list = []
# adc = int(input("Quantos itens: "))
# contador = 0
# while contador < adc:
#     vl = int(input(f"Digite o {contador + 1}° número: "))
#     list.append(vl)
#     contador += 1
    
# print(list)

#Adicionar item em lugar específico:
# numero = [1, 2, 6, 4]
# numero.insert(1, 44)
# print(numero)

# numero.pop

#Ex: 
# list = []
# while True:
#     opcao = input("Selecione o número:-1- Adição: \n-2- remoção:" )
    
#     if opcao == "1":
#         if len(list) == 0:
#             list.append(1)
#         else:
#             list.append(list[-1] + 1)
    
#     else:
#         if len(list) == 0:
#             print("A lista está vazia")
#         else:
#             list.pop(len(list) -1)
#     print(list)

#outra forma
# Função principal
# def main():
#     while True:
#         print("\nLista atual:", lista)
#         escolha = input("Digite 'a' para adicionar, 'r' para remover ou 's' para sair: ").strip().lower()

#         if escolha == 'a':
#             # Define o próximo número a adicionar
#             if lista:
#                 proximo = lista[-1] + 1
#             else:
#                 proximo = 1
#             lista.append(proximo)
#             print(f"{proximo} foi adicionado à lista.")

#         elif escolha == 'r':
#             # Remove o último item da lista
#             removido = lista.pop()
#             print(f"{removido} foi removido da lista.")

#         elif escolha == 's':
#             print("Encerrando o programa.")
#             break

#         else:
#             print("Opção inválida. Tente novamente.")

# # Executa o programa
# main()


# valores = []
# while True:
#     numero = int(input("Digite um número: "))
#     if numero == 0:
#         print("errado")
#         break
#     valores.append(numero)
#     print(valores)
#     print(valores)
    
    
#maximo, minimo, soma
# lista_numeros = [0,45,34,23,1,34]
# print(max(lista_numeros))
# print(min(lista_numeros))
# print(sum(lista_numeros))#soma

# lista_mediana = [15,24,2,525,58,74,5,74,54,658,5,22,54,7,9]
# def mediana(minha_lista: list):
#     ordenada = sorted(minha_lista)
#     centro_lista = len(ordenada) // 2
#     return ordenada[centro_lista]
# print(f"a mediana é: {mediana(lista_mediana)}")

# Ex:
# list = [1,54,25,548,558,51]
# def tamanho(lista):
#     return len(lista)
# print(tamanho(list))
    
    
#Atv:1
# list = [1,5,54,85,18,8]

# def media(list):
#     return sum(list) / len(list)
    
# print(media(list))
    

#Atv:2
# num = [8,3,15,1,9]

# def range(lista):
#     return max(lista) - min(lista)

# print(range(num))

#ex
# num = [8,3,15,1,9]
# x = 10
# if x in num:
#     print("existe")
# else:
#     print("não existe")


#Atv:3
# lista_nome = []
# def nome():
#     while len(lista_nome) < 5:
#         lista = input("Digite um nome: ")
            
#         if lista in lista_nome:
#             print("Nome já existe!")
#         else:
#             lista_nome.append(lista)
            
#         print(lista_nome)
# nome()


#Atv:4
# notas = []
# contador = 0
# while len(notas) < 5:
#     nota = float(input(f"Digite a nota {contador + 1}: "))
#     notas.append(nota)
#     contador += 1

# notas_aprovadas = [nota for nota in notas if nota >= 6]

# print("Notas aprovadas:", notas_aprovadas)

#forma prof******

# notas = []
# aprovadas = []

# while len(notas) < 5:
#     nota = float(input(f"Digite a nota: "))
#     notas.append(nota)
#     if nota >= 6:
#         aprovadas.append(nota)  
# print(f"aprovadas: {aprovadas}")  


#Atv:5

# list = []
# def menu():
#     print("=====LISTA DE TAREFAS=====")
#     print("1. Adicionar tarefa")
#     print("2. Remover tarefa")
#     print("3. Mostrar tarefas")
#     print("4. Sair")
    
    
# while True:
#     menu()
#     opcao = int(input("Escolha uma opção: "))
    
#     if opcao == 4:
#         print("Saindo...")
#         break
    
#     elif opcao == 1:
#         adc = input("digite a tarefa: ")
#         list.append(adc)      
#         print(adc,"Foi adicionado")
        
#     elif opcao == 2:
#         print(list)
#         remove = input("Qual tarefa deseja remover: ")
#         list.remove(remove)      
#         print(f"{remove}Foi removido")
        
#     elif opcao == 3:
#         print(list)
#         input("Aperte enter para voltar ao menu: ")
        
#     else:
#         input("Opção inválida!\nDigite enter para voltar ao menu inicial: ")


#Atv:6
#tentar mais
# num = []
# repetidos = []
# while len(num) < 10:
#     dig = int(input(f"Digite 10 número: "))
#     num.append(dig)
# i = 0   
# if num[i] not in repetidos:
#     repetidos.append(num[i])
#     print(num)


#prof:      
# def eli_duplicado():
#     num = []
#     while len(num) < 10:
#         dig = int(input(f"Digite 10 número: "))
#         num.append(dig)
#     unicos = []
#     repetidos = []    
#     i = 0   
#     while i < len(num):
#         if num[i] not in unicos:
#             unicos.append(num[i])
#         else:
#             repetidos.append(num[i])
#         i += 1
#     print("numeros", num)
#     print("unicos",unicos)
#     print("repetidos", repetidos)
    
# eli_duplicado()
        

#Atv: 7

frutas = ["maça", "melancia", "laranja", "limão"]
def comprar(frutas):
    while True:
        nome = input("Digite a fruta: ")
        if nome in frutas:
            print("fruta já esta na lista")
        
        elif nome == "sair":
            print("saindo")        
            break
        
        else:
            print("frutas não está na lista")

comprar(frutas)
