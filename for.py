# esc = input("digite uma string: ")
# for caractere in esc:
#     print(caractere + "*")#linha de baixo
#     print(caractere, end ="*")# na mesma linha
 
#range no for
# for i in range(5):
#     print(i) 

# for i in range(2,8): # vai contar do 2 ao 7
#     print(i)
# for i in range(1,19,2): # vai conta do 1 ao 19 pulado de 2 em 2 números( repete bloco de código pulando 2 em 2)
#     print(i)
#i é iteração

# num = int(input("digite um número positivo: "))
# for i in range(-num, num + 1):
#     if i != 0:
#         #print(i)
#         print(i, end=" ")#end no final acontecer...fez as coisas fica na mesma linha

#crinfo uma lista apartir do Range
# numero = list(range(3,22))
# print(numero)       

#Atv: 1  
# lista1 = [3, 7, 11 ,2]

# def lista_estrela(lista: list):
#     for i in lista:
#         estrela = "*" * i
#         print(estrela)

# lista_estrela(lista1)


#Atv: 2
#sorted organiza as letras, numeros tbm

# def anagramas(a, b):
#     return sorted(a) == sorted(b)

# print(anagramas("tame", "meta"))
# print(anagramas("tame", "mate"))
# print(anagramas("tame", "team"))
# print(anagramas("tabby", "batty"))
# print(anagramas("python", "java"))


#Atv: 3
# list = [1, 5, 6, 10]

# def soma_positivos():
#     print(sum(list))

# soma_positivos()
    
#prof

# list = [1, 5, 6, 10]

# def soma_positivos(lista):
#     soma = 0
#     for numero in lista:
#         if numero > 0:
#             soma += numero
#     return soma

# print(soma_positivos(list))


#Atv: 4

# list = [2, 5, 6, 4, 10]

# def numeros_pares(lista):
#     par = []
#     for numero in lista:
#         if numero % 2 == 0:
#             par.append(numero)
#     return par 
            
        
# print(numeros_pares(list))


#Atv: 5
# list1 = [1, 5, 4, 8]
# list2 = [5, 4, 6, 4]
# def lista_soma(a, b):
