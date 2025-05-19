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
tex = input("Número: ")
def quadradoString(tamanho):
    linha = 0
    while linha < tamanho:
        coluna = 0
        linha_texto = ""
        while coluna < tamanho:
            if (linha + coluna) % 2 == 0:
                linha_texto += "a"
            elif (linha + coluna) % 2 == 0:
                linha_texto += "b"
            elif (linha + coluna) % 2 == 0:
                linha_texto += "t"
            else:
                linha_texto += "y"
            coluna += 1
        print(linha_texto)
        linha += 1
quadradoString(tex)
