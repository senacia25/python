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


#Ex: 

# sudoku = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [0, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [0, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# for linha in sudoku:
#     for numero in linha:
#         if numero == 0:
#             print(" _ ", end="")
#         else:
#             print(numero, end="")
#     print("")


#Atv: 7

#prof:

# mesa = [
#     ["","",""],
#     ["","",""],
#     ["","",""]
#     ]
# contador = 0
# print(F"Tempo: {contador} - Olá jogador 1, comece o jogo com X. BOA SORTE!")
 
# def jogue_o_jogo(mesa,linha,coluna,caracter):
#     mesa[linha][coluna] = caracter
#     exibe_resultado()
#     if contador % 2 != 0:
#         jogador = "1 (x)"
#     else:
#         jogador = "2 (O)"
       
#     print(f"Tempo {contador} - Ótimo jogada, agora é a vez do jogador {jogador}")
#     print("")
 
# def exibe_resultado():
#     for linhas in mesa:
#         for items in linhas:
#             if items == "":
#                 print("_ ",end="")
#             print(items,end=" ")
 
#         print(" ")
   
# while True:
#     linha = int(input("Qual a linha: "))
#     coluna = int(input("Qual a coluna: "))
#     caracter = input("Qual o caracter: ")
#     jogue_o_jogo(mesa,linha, coluna, caracter)
#     contador += 1
#     if contador == 9:
#         exibe_resultado()
#         break

#############################################################

# # Inicializa a mesa vazia
# mesa = [["" for _ in range(3)] for _ in range(3)]

# contador = 0
# jogador_atual = "X"

# print(f"Tempo: {contador} - Olá jogador 1, comece o jogo com X. BOA SORTE!\n")

# def exibe_resultado():
#     print("\nEstado atual da mesa:")
#     for i, linha in enumerate(mesa):
#         linha_formatada = " | ".join([item if item != "" else " " for item in linha])
#         print(" " + linha_formatada)
#         if i < 2:
#             print("---+---+---")
#     print()

# def jogue_o_jogo(linha, coluna):
#     global contador, jogador_atual

#     if mesa[linha][coluna] != "":
#         print("Posição já ocupada! Tente novamente.")
#         return

#     mesa[linha][coluna] = jogador_atual
#     exibe_resultado()

#     contador += 1

#     if verificar_vencedor(jogador_atual):
#         print(f"Parabéns! Jogador {'1' if jogador_atual == 'X' else '2'} ({jogador_atual}) venceu o jogo!")
#         exit()

#     if contador == 9:
#         print("Empate! O jogo terminou sem vencedor.")
#         exit()

#     # Alterna o jogador
#     jogador_atual = "O" if jogador_atual == "X" else "X"
#     proximo_jogador = "1 (X)" if jogador_atual == "X" else "2 (O)"
#     print(f"Tempo: {contador} - Ótima jogada! Agora é a vez do jogador {proximo_jogador}\n")

# def verificar_vencedor(simbolo):
#     # Verifica linhas, colunas e diagonais
#     for i in range(3):
#         if all(mesa[i][j] == simbolo for j in range(3)) or all(mesa[j][i] == simbolo for j in range(3)):
#             return True
#     if all(mesa[i][i] == simbolo for i in range(3)) or all(mesa[i][2 - i] == simbolo for i in range(3)):
#         return True
#     return False

# # Loop principal do jogo
# while True:
#     try:
#         linha = int(input("Escolha a linha (0-2): "))
#         coluna = int(input("Escolha a coluna (0-2): "))

#         if 0 <= linha <= 2 and 0 <= coluna <= 2:
#             jogue_o_jogo(linha, coluna)
#         else:
#             print("Linha e coluna devem estar entre 0 e 2.")
#     except ValueError:
#         print("Entrada inválida. Por favor, insira números inteiros.")


#################################################################

# def criar_tabuleiro():
#     return [[" " for _ in range(3)] for _ in range(3)]

# def exibir_tabuleiro(tabuleiro):
#     print("\nTabuleiro:")
#     for i, linha in enumerate(tabuleiro):
#         print(" " + " | ".join(linha))
#         if i < 2:
#             print("---+---+---")
#     print()

# def verificar_vitoria(tabuleiro, jogador):
#     # Linhas e colunas
#     for i in range(3):
#         if all(tabuleiro[i][j] == jogador for j in range(3)) or \
#            all(tabuleiro[j][i] == jogador for j in range(3)):
#             return True
#     # Diagonais
#     if all(tabuleiro[i][i] == jogador for i in range(3)) or \
#        all(tabuleiro[i][2 - i] == jogador for i in range(3)):
#         return True
#     return False

# def verificar_empate(tabuleiro):
#     return all(tabuleiro[i][j] != " " for i in range(3) for j in range(3))

# def jogar():
#     tabuleiro = criar_tabuleiro()
#     jogador_atual = "X"
#     rodada = 1

#     print("Bem-vindo ao Jogo da Velha!\nJogador 1 = X  |  Jogador 2 = O")
#     exibir_tabuleiro(tabuleiro)

#     while True:
#         print(f"Rodada {rodada} - Jogador {jogador_atual}")
#         try:
#             linha = int(input("Escolha a linha (0-2): "))
#             coluna = int(input("Escolha a coluna (0-2): "))
#         except ValueError:
#             print("Entrada inválida. Use apenas números de 0 a 2.\n")
#             continue

#         if not (0 <= linha <= 2 and 0 <= coluna <= 2):
#             print("Coordenadas fora do intervalo! Tente novamente.\n")
#             continue

#         if tabuleiro[linha][coluna] != " ":
#             print("Essa posição já está ocupada. Escolha outra.\n")
#             continue

#         tabuleiro[linha][coluna] = jogador_atual
#         exibir_tabuleiro(tabuleiro)

#         if verificar_vitoria(tabuleiro, jogador_atual):
#             print(f"Parabéns! Jogador {jogador_atual} venceu o jogo!")
#             break

#         if verificar_empate(tabuleiro):
#             print("Empate! O tabuleiro está cheio e ninguém venceu.")
#             break

#         jogador_atual = "O" if jogador_atual == "X" else "X"
#         rodada += 1

# # Inicia o jogo
# jogar()


