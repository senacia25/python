import os

def menu():
    print("\n\t=======MENU PRINCIPAL=======")
    print("1. Exercícios resolvidos de Estatística (PDF) ")
    print("2. Quiz: Estatística em IA ")
    print("3. Quiz: Machine learning ")
    print("4. Pesquisa sobre uso de IA (PDF) ")
    print("0. Sair")

    
def quiz(perguntas):
    score = 0
    for i, p in enumerate(perguntas, 1):
        print(f"\nPergunta {i}: {p['pergunta']}")
        for op in p ["opcoes"]:
            print(op)
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == p ["correta"]:
            print("Corrreto", "\u2714")
            score += 1
        else:
            print(f" Errou! Resposta correta: {p['correta']}")
    print(f"\nPontuação final: {score}/{len(perguntas)}")

perguntas_estatitica = [
    {"pergunta": "Qual medida representa a média dos quadrados dos desvios?", 
    "opcoes": ["A) Variância", "B) Desvio padrão", "C) Moda", "D) Mediana"], 
    "correta": "A"},
    
    
]


perguntas_machineLearning = [ 
    {"pergunta": "O que é overfitting?", 
    "opcoes": ["A) Modelo que generaliza bem", "B) Modelo que aprende ruído do treino", "C) Modelo que não aprende nada", "D) Nenhuma das anteriores"], 
    "correta": "B"},
    
     
] 

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    
    if escolha == "0":
        print("\n\tVocê saiu!\n")
        break
    
    elif escolha == "1":
        print("\n\tOpção 1: Exercícios\n ")
        try:
            os.startfile("C:/Users/jorge.6234/Desktop/PYTHON/UC4/projeto/estatistica.pdf")    #(r"C:\Users\jorge.6234\Desktop\PYTHON\UC4\projeto/teste.pdf") usar o r como read, as barras invertidas ele ler mesmo assim. 
        except Exception as e:
            print(e,"\n")    
        input("\nPressione ENTER para voltar ao Menu Principal: ")
        
    elif escolha == "2":
        print("\n\tOpção 2: Quiz: Estatística em IA\n")
        quiz(perguntas_estatitica)
        input("\nPressione ENTER para voltar ao Menu Principal: ")
        
    elif escolha == "3":
        print("\n\tOpção 3: Quiz: Machine learning\n")
        quiz(perguntas_machineLearning)
        input("\nPressione ENTER para voltar ao Menu Principal: ")
        
    elif escolha == "4":
        print("\n\tOpção 4: Pesquisa\n")
        try:
            os.startfile("C:/Users/jorge.6234/Desktop/PYTHON/UC4/projeto/teste3.pdf")  # pode colocar só (teste3.pdf") mas o arquivo tem que está na pasta principal
        except Exception as e:
            print(e,"\n") 
        input("\nPressione ENTER para voltar ao Menu Principal: ")
        
    else:
        input("\n\t!!OPÇÃO INVÁLIDA! PRESSIONE ENTER PARA VOLTAR AO MENU PRINCIPAL!!")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
