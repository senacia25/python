# textostring = "arroz"
# inteiroint = 123
# flutuantefloat = 1,2,3
# print(f" texto: {textostring},\n inteiro: {inteiroint},\n float: {flutuantefloat}")

# text1 = "Era uma vez dois porquinhos,"
# text2 = "elez pularam no fogo e viraram BACON!"
# print(text1,text2)

# salario = int(input("Qual seu sálario "))
# horas_mes = int(input("Quantas horas você trabalha por mês? "))
# valor_hora = salario / horas_mes
# dia = int(input("Quantos horas você trabalha por dia? ")) ***
# valor_dia = valor_hora * dia***

# print(f"Você ganha: R$ {valor_hora:.2f} por hora!")
# print(f"Você ganha: R$ {valor_dia:.2f} por dia! ")***

# saber o tipo classe type
# t = "oi"
# n = 10 
# n2 = 12.5
# print(type(t))
# print(type(n))
# print(type(n2))

# num = int(input("Digite um número: "))
# num1 = 5                  #outra forma, resu = num * 5
# resu = num * num1
# print(f"{num} vezes {num1} é {resu}")


#ATV:7
# nome = input("Qual seu nome? ")
# ano_de_nascimento = int(input("Qual o ano que você nasceu? "))
# idfut = 2025 - ano_de_nascimento
# print(f"Olá {nome},você fará {idfut} no final do ano de 2025")


# ATV:8
# preco = float(input("Qual o preço do produto? "))
# descont = int(input("Qual o valor de desconto? "))
# num = descont / 100
# num2 = num * preco
# resul = preco - num2 
# print(f"valor do produto é: {resul}")


#Atv:9
# conta = int(input("Qual o valor da conta? "))
# gorj = int(input("Qual o valor da gorjeta? "))
# cont = (conta * gorj) / 100 
# resul = conta + cont 
# print(f"Sua conta é: {resul}")


#Atv:10
# real = float(input("Qual o valor em reis? "))
# dolar = float(input("Qual a cotaçao dolar? "))
# resul = real / dolar
# print(f"Valor final é: {resul:.2f}")


#Atv:11
# capital_inicial = float(input("Qual a capital inicial? ")) 
# juros_anual = float(input("Qual o juros anual? "))
# temp_anos = float(input("Quantos anos? "))
# resul = capital_inicial * (juros_anual / 100) * temp_anos
# print(f"resulta {resul}")


#Atv:12
# n1 = int(input("Coloque um número! "))
# n2 = int(input("Coloque um número! "))
# n3 = int(input("Coloque um número! "))
# media = round((n1 + n2 + n3) / 3)
# print(f"Média:{media}")


#Atv:13
# largura = int(input("Qual a largura? "))
# altura = int(input("Qual a altura? "))
# area = largura * altura
# perimetro = 2 * (largura + altura)
# print(f"Área: {area} \nPerímetro: {perimetro}")


#Atv:14
# cel = int(input("Qual a temperatura? "))
# fah = cel * 9 / 5 + 32
# print(fah)

#Exp: += , *=... soma a variavel, colocar o mesmmo nome da variavel
# valor = 10
# valor += 5
# print(valor)
# valor *= 2
# print(valor)

# numero = int(input("Entre com um número:"))
# if numero < 0:
#     print("esse número é negativo") 
    
# if numero > 0:
#     print("Esse número é positivo")               
                                                                   
# if numero == 0:
#     print("O número é zero")
    
# num = int(input("Digite um número: "))
# if num == 1984:
#     print("Orwell!!")
# else:
#     print("Errouu!")


#Atv:16
#num = int(input("Digite um número: "))
# if num < 0:
#     num *= -1
#     print(num)
# else:
#     print(num)


#Atv:17
# nome =input("Digite um nome: ")
# if nome != "jerry":
#     porcoes = int(input("Digete o número de porção: "))
#     conta = porcoes * 5.90
#     print(f"valor total: ${conta}")
# else:
#     print("Tudo pago!")
   
    
#Atv:18
# num = int(input("Digite um número:"))
# if num < 1000 and num >= 100:
#     print("Este numero é menor que 1000 Obrigado!")
# elif num < 100 and num >= 10:
#     print("Este número é menor que 100 Obrigado!")
# elif num < 10:
#     print("Este número é menor que 10 Obrigado!")
# else:
#     print("Acertou, obrigado!")
    
    
#Atv:19
# nome = "alfredo"
# cidade = "alfradinha"
# estado = "alfralandia"
# cep = 123456
# tent = input("digite um nome: ")
# if tent == nome:
#     print(f"Nome: {tent}\nCidade: {cidade}\nEstado: {estado}\nCep: {cep}")  
# else:
#     print("Esse usuário não existe em nossas bases de dados!")
  
    
#Atv:20
# num = float(input("Digite um número: "))
# num2 = float(input("Digite o segundo número: "))
# opera = input("Qual operação? ")
# if opera == "+":
#     mult = num + num2 
#     print(mult)
# elif opera == "*":
#     soma = num * num2
#     print(soma)
# elif opera == "-":
#     subt = num - num2
#     print(subt)
# elif opera == "/":
#     div = num / num2
#     print(div)
# else:
#     print("Inválido!")


#Atv:21
# fah = int(input("Qual a temperatura em fahrenheit? "))
# cel = (fah - 32)  * 5 / 9 
# if cel < 0:
#     print("Brr! Está frio aqui!")
# print(f"{cel:.2f} Celsius")


#Atv:22
# horas = int(input("Digite quanto ganha por hora: "))
# horas_trab = int(input("Quantas horas trabalha por dia? "))
# semana = input("Qual dia da semana? ")
# sal_dia = horas * horas_trab
# if semana == "domingo":
#     print(sal_dia * 2) 
# else:
#     print(f"Salário diario: {sal_dia}")


#Atv:23
# pontos = int(input("Digite a quantidade de pontos: "))
# if pontos <= 100:
#     print("O bônus é de 10%")
# else:
#     print("O bônus é de 15%")


#Atv:24
# prev = int(input("Qual a previsão o tempo para amanhâ? "))
# chuv = input("Vai chover? (sim/não)")
# if prev > 20:
#     print("Use jeans e camiseta!")
#     if chuv == "sim":
#         print("Leve um guarda-chuva!")
# elif prev >= 10 and prev < 20:
#     print("Use um moletom!")
#     if chuv == "sim":
#         print("Leve um guarda-chuva!")
# elif prev >= 5 and prev < 10:
#     print("Use casaco!")
#     if chuv == "sim":
#         print("Leve um guarda-chuva!")
# else:
#     print("Use moleton e casaco")
    
    
#Atv:25
# idade = int(input("Qual sua idade? "))
# if idade >= 18:
#     print("Você é maior de idade!")
# else:
#     print("Você é menor de idade!")
    

#Atv:26
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# resul = (nota1 + nota2) / 2
# if resul >= 7:
#     print(f"{resul} Aprovado")
# else: 
#     print(f"{resul} Reprovado")


#Atv:27
# prod = int(input("Qual o valor do produto? "))
# if prod <= 50:
#     print("Categoria econômica!")
# elif prod > 50 and prod <=100:
#     print("categoria intermediária")
# else:
#     print("Categoria Premium!!")


#Atv:28
# idade = int(input("Qual a idade? "))
# if idade >= 16:
#     print("Pode votar")
# else:
#     print("Não pode votar.")


#Atv:29
# mes = int(input("Digite o mês: "))
# if mes == 1:
#     print("Janeiro")
# elif mes == 2:
#     print("Fevereiro")
# elif mes == 3:
#     print("Março") 
# elif mes == 4:
#     print("Abril")
# elif mes == 4:
#     print("Abril")
# elif mes == 5:
#     print("Maio")
# elif mes == 6:
#     print("Junho")
# else:
#     print("Mês invalido!")


#Atv:30
# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite um número: "))
# if num1 > num2:
#     print(f"{num1} é maior")
# elif num1 < num2:
#     print(f"{num2} é maior")
# else:
#     print("ERRO")


#Atv:31-32
# nome1 = input("Qual o seu nome? ")
# idade1 = int(input("Digite sua idade: "))
# nome2 = input("Qual o seu nome? ")
# idade2 = int(input("Digite sua idade: "))
# if idade1 >= 60:
#     print(nome1)
# elif idade2 < 60:
#     print(nome2)
# else:
#     print("erro")


#Atv:33
# idade = int(input("Digite sua idade: "))
# if idade < 5 and idade > 1:
#     print("Você errou sua idade!")
# elif idade >= 6 and idade <= 120:
#     print(f"OK, você tem {idade}")
# else:
#     print("Você é um animal!")


#Atv:34
# nome = input("Qual seu nome? ")
# if nome == "huguinho" or nome == "zezinho" or nome == "luisinho":
#     print("Você é sobrinho do Pato Donald!")
# elif nome == "chiquinho" or nome == "francisquinho":
#     print("Você é sobrinho do Mickey Mouse")
# else:
#     print("Você não tem tio!")


#Atv:35
# pontos = int(input("digite os pontos: "))
# if pontos <= 0:
#     print("mpossível")
# elif pontos >= 0 and pontos <= 49:
#     print("Falhar")
# elif pontos >= 50 and pontos <= 59:
#     print(1)
# elif pontos >= 60 and pontos <= 69:
#     print(2)
# elif pontos >= 70 and pontos <= 79:
#     print(3)
# elif pontos >= 80 and pontos <=89:
#     print(4)
# elif pontos >= 90 and pontos <= 99:
#     print(5)
# else:
#     print("Impossível")

#Atv:36
# num = int(input("Digite um número interio: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")     
# elif num % 3 == 0:
#     print("fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print("ok")

#Atv:37
# ano = int(input("digite o ano: "))
# if ano % 100 == 0 and ano % 400 == 0:
#     print("bissexto divido por 400")
# elif ano % 4 == 0:                     tentativa 1
#     print("ano bissexto 4")
# else:
#     print("Erro")
#tenttiva 2
# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print("ano bissexto")
# else:
#     print("erro")

#exerwhile
#Atv:38
# print("Óla")
# while True:
#     mens = input("Você quer continuar? ")
#     if mens == "nao":
#         print("Okay! até a próxima")
#         break 

