
# try e except:

# try:
#     numero = int(input("Digite um número: "))
#     print(f"Você digitou: {numero}")
    
    
# except ValueError:
#     print("Erro: você não digitou um número inteiro! ")

#=========

# try:
#     num_str = input("Digite um número: ")
#     num_int = int(num_str)
#     resultado = 10 / num_int
#     print(f"10 dividido por {num_int} é {resultado}")
    
# except ValueError:
#     print("Erro: Entrada inválida. Por favor, digite um número. ")
    
# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero. ")
    
# except Exception as e:
#     print(f"Ocorreu um erro inesperado {e}")
    
# # else va ser executado se nao tiver nem um erro    
# else:
#     print("Deu tudo certo! ")
    
# # finally executa mesmo que tenha erro ou não no try    
# finally:
#     num_str = input("Digite um número: ") 
    
#=======

# arquivo = None

# try:
#     arquivo = open("UC2/dados.txt", "r") # ("dados.txt", "r") chamar - cd UC2 no terminal, pq ele ta chamando a pasta python
#     conteudo = arquivo.read()    
#     print("Arquivo lido com sucesso")
    
# except FileNotFoundError:
#     print("Erro: arquivo não encontrado")
    
# except Exception as e:
#     print(f"Erro ao ler arquivo: {e}")

# else:
#     print("Processamento do arquivo concluído co sucesso!")
        
# finally:
#     if arquivo:
#         arquivo.close()
#         print("Arquivo fechado! ")


#Atv: 1

# try:
#     num = int(input("Digite um número: "))
#     print(f"Você digitou o número {num}")
    
# except ValueError:
#     print("Erro: você não digitou um número interio! ")


#Atv: 2

# try:
#     num = int(input("Digite um número: "))
#     resultado = 10 / num 
#     print(f"10 dividido por {num} é {resultado}")
    
# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero. ")
   
    
#Atv: 3

# frutas = ["Manga", "Goiaba", "Laranja", "Uva", "Melancia"]

# try:
#     indice = int(input("Digite o índice da fruta que deseja ver: "))
    
#     print(frutas[indice])
    
# except IndexError:
#     print("Índice fora de alcance")

# except ValueError:
#     print("Erro, digite um número inteiro! ")


#Atv: 4


# arquivo = None

# try:
#     arquivo = open("UC2/dados.txt", "r")
#     conteudo = arquivo.read()
#     print("Arquivo lido com sucesso!")
#     # 
# except FileNotFoundError:
#     print("Erro: arquivo não encontrado")
    
# finally:
#     if arquivo:
#         arquivo.close()
#         print("Arquivo fechado! ")
  

#Atv: 5

# num = [10, 20, 30]

# try:
#     divisor = int(input("digite um número divisor: "))
#     indice = int(input("digite um número divisor: "))
    
#     resultado = num[indice] / divisor
#     print(f"Resultado da divisão: {resultado}")
    
# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero")
    
# except IndexError:
#     print("Erro: Índice fora de alcance da lista.")

# except Exception as e:
#     print("Erro insperado:", e)


#Atv: 6

# lista = [1, 2, 5, 8, 4, 9]

# try:
#     "lista".append(10)
#     print(lista)

# except AttributeError:
#     print("Erro: string não tem append")       


