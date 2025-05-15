senha_correta = "python123"

tent = 0
tentativas = 3

while tent < tentativas:
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("CONCEDIDO!")
        break
    else:
        tent += 1
        print(f"SENHA INCORRETA! Tentativas restantes: {tentativas - tent}")
        

if tent == tentativas:
    print("ACESSO BLOQUEADO!")
