import os

def menu():
    print("\t=======MENU PRINCIPAL=======")
    print("1. Exercícios resolvidos de Estatística (PDF) ")
    print("2. Quiz: Estatística em IA ")
    print("3. Quiz: Machine learning ")
    print("4. Pesquisa sobre uso de IA (PDF) ")
    print("0. Sair")
    
while True:
    menu()
    escolha = input("Escolha uma opção: ")
    
    if escolha == "0":
        print("\nVocê saiu!\n")
        break
    
    elif escolha == "1":
        print("\nOpção 1: Exercícios\n ")
        try:
            os.startfile("C:/Users/jorge.6234/Desktop/PYTHON/UC4/projeto/estatistica.pdf")    #(r"C:\Users\jorge.6234\Desktop\PYTHON\UC4\projeto/teste.pdf") usar o r como read, as barras invertidas ele ler mesmo assim
        except Exception as e:
            print(e,"\n")    
        input("Pressione ENTER para voltar ao Menu Principal: ")
        
    elif escolha == "2":
        print("\nOpção 2: Quiz: Estatística em IA\n")
        try:
            os.startfile("C:/Users/jorge.6234/Desktop/PYTHON/UC4/projeto/teste1.pdf")  # pode colocar só (teste1.pdf") mas o arquivo tem que está na pasta principal
        except Exception as e:
            print(e,"\n") 
        input("\nPressione ENTER para voltar ao Menu Principal: ")
        
    elif escolha == "3":
        print("\nOpção 3: Quiz: Machine learning\n")
        try:
            os.startfile("C:/Users/jorge.6234/Desktop/PYTHON/UC4/projeto/teste2.pdf")
        except Exception as e:
            print(e,"\n") 
        input("\nPressione ENTER para voltar ao Menu Principal: ")
        
    elif escolha == "4":
        print("\nOpção 4: Pesquisa\n")
        try:
            os.startfile("C:/Users/jorge.6234/Desktop/PYTHON/UC4/projeto/teste3.pdf")
        except Exception as e:
            print(e,"\n") 
        input("\nPressione ENTER para voltar ao Menu Principal: ")
        
    else:
        input("\n\t!!OPÇÃO INVÁLIDA! PRESSIONE ENTER PARA VOLTAR AO MENU PRINCIPAL!!")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
