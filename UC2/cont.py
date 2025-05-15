#Atv:39
# from math import sqrt
# #print(sqrt(9))

# while True:
#     num = int(input("Digite um número: "))
#     if num < 0:
#         print("Número inválido")
#     elif num > 0:
#         print(sqrt(num))
#     else:
#         print("Encerrado!")
#         break


#Atv:40
# numero = 5
# print("contando")
# while True:
#     print(numero)
#     numero = numero - 1
#     if numero == 0:
#         break
# print("Foi")

#Atv:41
# senha = int(input("Cadastre uma senha: "))

# while True:
#     tent = int(input("Digite a senha cadastrada: "))
#     if tent == senha:
#         print("Acesso concedido!")
#         break
#     else:
#         print("Senha errada, tente novamente!")


#Atv:42
# tent = 0

# while True:
#     pin = int(input("Digite o pin: "))
#     tent += 1
#     if pin == 123456:
#         print(f"PIN correto inserido, números de tentativas. {tent}")
#         break
#     else:
#         print(tent)    


#Atv:43
# ano = int(input("Digite um ano:"))

# while True:
#     ano += 1
#     if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#         print(f"{ano} é um ano bissexto!")
#         break
        

#Atv:44     
# par = 0

# while par < 30:
#     par += 2
#     print(par)
    
# print("finalizado")


#Atv:45
# print("Você está pronto?")
# numero = int(input("Por favor, digite um número: "))

# while numero == 0:
#     print(numero)
#     print("Agora")
#     numero = int(input("Por favor, digite um número: "))


# #Atv:46
# var = 1
# num = int(input("Digite um número: "))

# while var < num:
#     print(var)
#     var += 1


# #Atv:47
# num = int(input("Digite um número: "))
# dobro = 1

# while dobro <= num:
#     print(dobro)
#     dobro *= 2
# print(f"O limite é {num}")

#refazer
#Atv:48
# num = int(input("Digite um número: "))
# dobro = 1
# base = int(input("Qual a base: "))

# while dobro <= num:
#     print(dobro)
#     dobro *= base
# print(f"O limite é {num}")

# import re
# import random

# print(re.search("[A-Z]", "senhA"))

# numero_secreto = random.randint(1, 200)
# print(numero_secreto)


#Atv:49-50
# soma = 0
# while soma <= 100:
#     num = int(input("Digite um número: "))
#     soma += num
#     print(soma)
    
# print("limite")


# exem = "ele é o instrutor do curso"
# total = len(exem)
# print(total)

           
#Atv:51
# import re

#refazer
# while True:
#     senha = input("Digite a senha: ")
#     lmai = re.search("[A-Z]", senha)
#     lmin = re.search("[a-z]", senha) 
#     tnum = re.search("[0-9]", senha)
#     if len(senha) < 8:
#         print("Senha precisa ter 8 cacteres.")
    
#     elif lmai == None:
#         print("Precisa 1 letra maiúscula")
#     elif lmin == None:
#         print("1 letra minúscula")
#     elif tnum == None:
#         print("1 número")
#     else:
#         print("Senha compatível")
#         break
        

# Atv:52
# num = 152
# while True:
#     dig = int(input("Adivinhe o número: "))
#     if dig > num:
#         print("O número é menor")
#     elif dig < num:
#         print("o número é maior")
#     else:
#         print(f"{num} - Acertou")

#outra forma atv:52
# import random
# numero_secreto = random.randint(1, 100)   
# tent = 0
# while True:
#     num = int(input("Adivinhe o número: "))
#     tent += 1
    
#     if numero_secreto < num :
#         print("O número é menor")
#     elif numero_secreto > num:
#         print("o número é maior")
#     else:
#         print(f"{numero_secreto} - Acertou \n{tent} - Número de tentativas ")

#refazer
# #Atv:53
# saldo = 500
# print(f"Seu saldo é: {saldo}")
# while True:
#     saque = int(input("Digite um valor: "))
        
#     if saque % 10 != 0:
#         print("O valor deve ser multilplicado por 10")
#     elif saque > saldo:
#         print("Saldo insuficiente")
#     elif saque <= 0:
#         print("Valor inválido")
#     else:
#         saldo -= saque
#         print(saldo)
#         print(saldo)
        
        
 #Atv:54
# while True:
#     palavra1 = input("Digite uma palavra: ")   
#     palavra2 = input("Digite outra palavra: ") 
#     if len(palavra1) == len(palavra2):
#          print("As palavras tem o mesmo número de caracterer")
#          break
#     else:
#         print("Tamanhos diferente, tente novamente")

#Atv:55
# while True:
#     palavra1 = input("Digite uma palavra: ")   
#     palavra2 = input("Digite outra palavra: ") 
#     if len(palavra1) > len(palavra2):
#         print(f"{palavra1}Essa é maior")
#     elif len(palavra1) == len(palavra2):
#         print("As duas são do mesmo tamanho")
#     else:
#         print(f"{palavra2} É maior")
    

# entrada = input("Digite um palavra: ")
# ultimo = len(entrada) - 1
# print(f"O último caracter da palavra é -{entrada[ultimo]}-")


#Atv:56