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

# l1 = [1, 5, 4, 85]
# l2 = [5, 4, 6, 44]
# def lista_soma(la, lb):
#     resultado = []
#     for i in range(len(l1)):
#         soma = l1[i] + l2[i]  #i é o indice
#         resultado.append(soma)
#     return resultado #depois de somar tudo a cima ele tras o restado

# print(lista_soma(l1, l2))


#Ex: 

# minha_string = "Quantas madeiras um esquilo poderia empilhar se um esquilo pudesse empilhar madeira"
# print(minha_string.count("a"))

# minha_lista = [1,2,5,5,4,3,5,2,2,54,3]
# print(minha_lista.count(5))

#replace
# minha_palavra = "oi, oi, oi, amigos"
# print(minha_palavra.replace("oi","olá"))
# #ou
# nova_palavra = minha_palavra.replace("oi","olá")
# print(nova_palavra)


#EX:

# string = "olá amigos, como estão todos, hoje está chuvendo!"

# def mais_caracteres(texto):
#     maior_caractere = ""
#     maior_contagem = 0
    
#     for caractere in texto:
#         contagem = texto.count(caractere)
#         if contagem > maior_contagem:
#             maior_contagem = contagem
#             maior_caractere = caractere
            
#     return maior_caractere

# print(mais_caracteres(string.replace(" ", "")))# replace tirou os espaços, porque estava contando os espaços


#outra forma

# def mais_caracteres(s):
#     max_char = ''
#     max_count = 0
    
#     for c in s:
#         ocorrencias = s.count(c)
#         if ocorrencias > max_count:
#             max_count = ocorrencias
#             max_char = c
            
#     return max_char

# print(mais_caracteres("banana"))


#Atv: 6

# string = "Qualquer coisa escrita de qualquer forma"

# def sem_vogal(s):
#     vogais = "aeiouAEIOU"
#     for v in vogais:
#         if s.count(v) > 0:
#             s = s.replace(v, "")
#     return s

# print(sem_vogal(string))


#prof

# def sem_vogal(texto):
#     vogais = "aeiouAEIOU"
#     nova_string = ""
    
#     for letra in texto:
#         if letra not in vogais:
#             nova_string += letra
    
#     return nova_string

# print(sem_vogal("Qualquer coisa escrita de qualquer forma"))


#Ex

# lista_bidimensional = [[0,1,2,3],
#                        [1,2,5,6],
#                        [5,4,6,1],
#                        [5,6,4,1]]

# print(lista_bidimensional[2][1])


# array = [[0,1,2,3],[1,2,5,6],[5,4,6,1],[5,6,4,1]]

# def conta_elementos_match(minha_matriz, elemento):
#     contagem = 0
#     for linha in minha_matriz:
#         for item in linha:
#             if item == elemento:
#                 contagem += 1
    
#     return contagem
    
# print(conta_elementos_match(array, 5))


