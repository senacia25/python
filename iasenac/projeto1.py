#Lista Mágica do Usuário
lista = ["macarrão", "trigo", "bolacha"]
def mostrar_menu():
    print("======MENU DE OPERAÇÕES======")
    print("1. Adicionar item")
    print("2. Iserir item em posição")
    print("3. Adicionar vários itens")
    print("4. remover item")
    print("5. Remover posição")
    print("6. limpar lista")
    print("7. Ver posição de um item")
    print("8. Contar item")
    print("9. ordenar lista")
    print("10. Inverter lista")
    print("0. SAIR")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")
  
    #lista = []
    #escolha = input("Escolha uma opção: ")
    if escolha == "1":
        item = input("Qual item gostaria de adiconar? ")
        lista.append(item)
        print(f"{item} Foi adcionado!")
        
    elif escolha == "2":
        item1 = input("Qual item gostaria de inserir? ")
        posicao = int(input ("Qual posição gostaria de adicionar? "))
        lista.insert(posicao, item1)
        print(f"{item1} Foi inserido a lista na posição {posicao}!")
    
    elif escolha == "3":
        item2 = input("adicione mais de um item ")
        lista.extend((item2).split(","))
        print(f"{item2} Foi adicionado a lista!")
    
    elif escolha == "4":
        item3 = input("Digite o item que gostaria de remover ")
        if item3 in lista:
            lista.remove(item3)
            print(f"{item}Foi removido!")
            
    elif escolha == "5":
        item4 = input("digite a posição do item que gostaria de remover ") 
        if item4 in lista:
            removido = lista.pop(item4)
            print(f"{item4} Foi ")


    # elif escolha == "3": 
    # elif escolha == "3": 
    # elif escolha == "3": 


       
    print(lista)

























# while True:
#     mostrar_menu()
#     escolha = input("Escolha uma opção: ")
