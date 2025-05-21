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
list = []
opcao = input("Selecione o número:-1- Adição: \n-2- remoção:" )