# def soma():
#     print(5 + 5)
# soma()

#prática:
# def sete_irmaos():
#     print("alvaro\nbruno\ncarlos\ndiego\nelias\nfabio\ngabriel")
# sete_irmaos()

# def soma(x,y):
#     return x + y
# print(soma(5,15))


#Atv: 1
# def media(x,y,z):
#     soma = x + y + z
#     return soma / 3
# print(f"A média é: {media(10,30,50)}")

# #Atv:2
# def printa_varias_vezes(texto, vezes):
#     return texto * vezes
# print(printa_varias_vezes("hoje\n", 8))


#Atv:3
# def quadrado_hashtag(x,y):
#     return x * y
# print(quadrado_hashtag("#",5))
# print(quadrado_hashtag("#####\n",5))

# Outra forma:
# numero = int(input("Número: "))
# def quadrado_hashtag(tamanho):
#     contador = 0
#     while contador < tamanho:
#         print("#" * tamanho)
#         contador += 1
# quadrado_hashtag(numero)


#Atv:4
# numero = int(input("Número: "))
# def mesaXadrez(tamanho):
#     linha = 0
#     while linha < tamanho:
#         coluna = 0
#         linha_texto = ""
#         while coluna < tamanho:
#             if (linha + coluna) % 2 == 0:
#                 linha_texto += "1"
#             else:
#                 linha_texto += "0"
#             coluna += 1
#         print(linha_texto)
#         linha += 1
# mesaXadrez(numero)


#Atv:5
# nome = input("Número: ")
# def quadradoString(palavra , numero):
#     stringTotal = (palavra * numero)
#     linha = 0
#     while linha < numero:
#         coluna = 0
#         letra = ""
#         while coluna < numero:
#             posicao = linha * numero + coluna
#             letra += stringTotal[posicao]
#             coluna += 1

#         print(letra)
#         linha += 1
# quadradoString("jumanji", 4)


# def quadradoString(s, n):
#     i = 0
#     while i < n:
        
#         print(s[i:] + s[:i])
#         i += 1

# quadradoString("jumanji", 4)


# def quadradoString():
#     # Solicita a string e o tamanho do quadrado ao usuário
#     s = input("Digite a string: ")
#     n = len(s)  # O tamanho do quadrado é o comprimento da string

#     i = 0
#     while i < n:
#         # Imprime a string deslocada para a direita
#         print(s[i:] + s[:i])
#         i += 1

# # Exemplo de uso
# quadradoString()

# def quadradoString():
#     # Solicita a string e o número de colunas ao usuário
#     s = input("Digite a string: ")
#     n = int(input("Digite o número de colunas: "))

#     # A quantidade de linhas do quadrado será igual ao número de colunas
#     # Ou seja, o quadrado será sempre de n x n
#     i = 0
#     while i < n:
#         # Ajusta a string para que ela tenha exatamente n caracteres
#         linha = (s * ((n // len(s)) + 1))[:n]  # Repete a string e corta para n caracteres
#         # Imprime a string deslocada para a direita
#         print(linha[i:] + linha[:i])
#         i += 1

# # Exemplo de uso
# quadradoString()


#Atv:8
# def linha():
 
#     comprimento = int(input("Digite o comprimento da linha: "))

#     texto = input("Digite uma string (ou deixe em branco para usar '*'): ")

#     if texto == "":
#         caractere = "*"
#     else:
#         caractere = texto[0]

#     print(caractere * comprimento)

# linha()


#Ex:
# def comprimentar(nome):
#     print(f"Olá, {nome}")

# def comprimentar_vezes(nome, vezes):
#     while vezes > 0:
#         comprimentar(nome)
#         vezes -= 1

# comprimentar_vezes("Maria!", 5)

#Outro Ex:

# def resultado():
#     resultado = 25 + 25
#     return resultado

# def calculo(x):
#     soma = x + resultado()
#     print(soma)

# calculo(50)


#Atv: 7
# def linha(n, texto):
 
#     if texto == "":
#         caractere = "*"
#     else:
#         caractere = texto[0]

#     print(caractere * n)


# def caixa_de_hashtag(tamanho):
#     contador = 0
#     while contador < tamanho:
#         linha(10, "#")
#         contador += 1

# caixa_de_hashtag(3)


#Atv: 8
# def triangulo(x):
#     contador = 0
#     while contador < x:
#         elementos = "#" * (contador + 1)  #invertido (x - contador)
#         print(elementos)
#         contador += 1
    
# triangulo(10)


#Atv: 9
# def o_maior_numero(x, y ,z):
#     return max(x ,y , z)
# print(o_maior_numero(10 ,37, 55))
    
#Outra forma:
# def o_maior_numero(x, y ,z):
#     maior = x
#     if y > maior:
#         maior = y
#     if z > maior:
#         maior = z
#     return maior
# print(o_maior_numero(10 ,37, 55))



#Atv:10
# escreva uma funcao chamada mesmo_caracter, que receba uma string e dois interios como argumento. Os interos se referem a indice(numero letra string) dentro a string.
# A função deve retorna True se os dois carateres no índice especificados forem os mesmos. Caso contrario, e especialmente se qualquer um dos indices 
# estiver fora do escobo da string, a função retorna False.

# def mesmo_caracter(a, b, c):
#     if  b == len(a) or c == len(a):
#         return False
#     return a[b] == a[c]
# print(mesmo_caracter("hojee", 3, 4))

# #outra forma prof
# def mesmo_caracter(a, b, c):
#     if b < 0 or c < 0 or b >= len(a) or c >= len(a):
#         return False
#     else:
#         if a[b] != a[c]:
#             return False
#         else:
#             return True
# print(mesmo_caracter("hojee", 1, 1))


