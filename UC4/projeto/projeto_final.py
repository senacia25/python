import os
import time
##poderia ate se criar um def(função) para abrir pdf  
##def abrir_pdf(caminho): 
##    try: 
##        os.startfile(caminho)  # Abre o PDF com o leitor padrão do Windows 
##    except Exception as e: 
##        print(f"Erro ao abrir o arquivo {caminho}: {e}") 
##então colocar na opcão 1 e 4 do menu, mas coloquei try direto lá
        
        
def menu():
    print("\n\t=======MENU PRINCIPAL=======\n")
    print("1. Exercícios resolvidos de Estatística (PDF) ")
    print("2. Quiz: Estatística em IA ")
    print("3. Quiz: Machine learning ")
    print("4. Pesquisa sobre uso de IA (PDF) ")
    print("0. Sair")

    
def quiz(perguntas):
    score = 0
    print("!Digite 'S' a qualquer momento para SAIR do quiz!")
    for i, p in enumerate(perguntas, 1):
        print(f"\nPergunta {i}: {p['pergunta']}")
        for op in p["opcoes"]:
            print(op)
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == p["correta"]:
            print("Corrreto", "\u2714") # "\u2714" código para certo, ok
            score += 1
        elif resposta == "S":
            print("Encerradando Quiz...")
            time.sleep(3)
            print("Quiz finalizado!")
            time.sleep(1)
            break
        else:
            print(f" Errou! Resposta correta: {p['correta']}")
    print(f"\nPontuação final: {score}/{len(perguntas)}")

perguntas_estatitica = [
    {"pergunta": "Qual medida representa a média dos quadrados dos desvios?", 
    "opcoes": ["A) Variância", "B) Desvio padrão", "C) Moda", "D) Mediana"], 
    "correta": "A"},
    
    {"pergunta": "Distribuição mais usada para modelar eventos raros:",
     "opcoes": ["A) Normal", "B) Poisson", "C) Binomial", "D) Uniforme"],
     "correta": "B"},
     
    {"pergunta": "O valor que divide a amostra ao meio é chamado de:",
     "opcoes": ["A) Média", "B) Mediana", "C) Moda", "D) Variância"],
     "correta": "B"},
    
    {"pergunta": "Se todos os valores têm a mesma probabilidade de ocorrer, temos a distribuição:",
     "opcoes": ["A) Normal", "B) Uniforme", "C) Binomial", "D) Poisson"],
     "correta": "B"},
    
    {"pergunta": "O desvio padrão mede:",
     "opcoes": ["A) Tendência central", "B) Grau de dispersão", "C) Probabilidade", "D) Frequência"],
     "correta": "B"},
    
    {"pergunta": "Qual destas NÃO é uma medida de tendência central?",
     "opcoes": ["A) Média", "B) Moda", "C) Variância", "D) Mediana"],
     "correta": "C"},
    
    {"pergunta": "Em um histograma, a área total representa:",
     "opcoes": ["A) Média", "B) Frequência total", "C) Probabilidade total", "D) Mediana"],
     "correta": "C"},
    
    {"pergunta": "Quando a média é maior que a mediana, a distribuição tende a ser:",
     "opcoes": ["A) Simétrica", "B) Assimétrica à esquerda", "C) Assimétrica à direita", "D) Normal"],
     "correta": "C"},
    
    {"pergunta": "O Teorema Central do Limite afirma que:",
     "opcoes": ["A) Toda variável é normal", "B) Médias amostrais tendem à normalidade", "C) A variância é sempre constante", "D) A moda é igual à mediana"],
     "correta": "B"},
    
    {"pergunta": "Probabilidade de evento impossível é:",
     "opcoes": ["A) 1", "B) 0", "C) 0,5", "D) Depende da amostra"],
     "correta": "B"},
    
]


perguntas_machineLearning = [ 
    {"pergunta": "O que é overfitting?", 
    "opcoes": ["A) Modelo que generaliza bem", "B) Modelo que aprende ruído do treino", "C) Modelo que não aprende nada", "D) Nenhuma das anteriores"], 
    "correta": "B"},
    
    {"pergunta": "Qual algoritmo é usado em classificação?",
     "opcoes": ["A) KNN", "B) Regressão Linear", "C) PCA", "D) K-means"],
     "correta": "A"},
    
    {"pergunta": "O que significa 'supervisionado' em Machine Learning?",
     "opcoes": ["A) Sem rótulos", "B) Com rótulos", "C) Autoaprendizado", "D) Nenhuma das anteriores"],
     "correta": "B"},

    {"pergunta": "Qual técnica reduz dimensionalidade?",
     "opcoes": ["A) SVM", "B) PCA", "C) Regressão logística", "D) Árvore de decisão"],
     "correta": "B"},

    {"pergunta": "Na regressão linear, o erro é medido pela:",
     "opcoes": ["A) Soma dos quadrados dos resíduos", "B) Moda", "C) Desvio padrão", "D) Acurácia"],
     "correta": "A"},

    {"pergunta": "O que é regularização?",
     "opcoes": ["A) Técnica para aumentar overfitting", "B) Reduz complexidade do modelo", "C) Melhorar gráficos", "D) Aumentar dimensionalidade"],
     "correta": "B"},

    {"pergunta": "Qual destes é um algoritmo NÃO supervisionado?",
     "opcoes": ["A) Regressão logística", "B) SVM", "C) K-means", "D) Random Forest"],
     "correta": "C"},

    {"pergunta": "O que significa 'feature' em Machine Learning?",
     "opcoes": ["A) O alvo a ser previsto", "B) Uma variável de entrada", "C) O erro do modelo", "D) O parâmetro de ajuste"],
     "correta": "B"},

    {"pergunta": "Qual métrica é usada em classificação binária?",
     "opcoes": ["A) Acurácia", "B) R²", "C) Erro quadrático médio", "D) Nenhuma das anteriores"],
     "correta": "A"},

    {"pergunta": "Em redes neurais, a função que introduz não-linearidade é chamada de:",
     "opcoes": ["A) Função de ativação", "B) Função de perda", "C) Função de custo", "D) Função de otimização"],
     "correta": "A"},
     
] 

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    
    if escolha == "0":
        print("\n\tSaindo...!\n")
        time.sleep(2)
        print("\tPROGRAMA FINALIZADO, ATÉ A PRÓXIMA!! \U0001F600 \U0001F44B \n")  # \U0001F600 \U0001F44B cogido para carinha rindo e tchau
        break
            
    elif escolha == "1":
        print("\n\tOpção 1: Exercícios\n ")
        try:
            os.startfile("C:/Users/jorge.6234/Desktop/PYTHON/UC4/projeto/estatistica.pdf")  #(r"C:\Users\jorge.6234\Desktop\PYTHON\UC4\projeto/teste.pdf") usar o r como read, as barras invertidas ele ler mesmo assim. 
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