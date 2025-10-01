# import math

# def bhaskara(a,b,c):    #(a,b,c) = parâmetros
#     delta = b**2-4*a*c            # ** quadrado
#     if delta < 0:
#         return "Não possui raízes reais"
    
#     x1 = (-b + math.sqrt(delta)) /(2*a)
#     x2 = (-b - math.sqrt(delta)) /(2*a)
#     return x1, x2

# raizes = bhaskara(1, -3, 2)
# print("Raízes da equção:", raizes)
# print(f"Raízes da equção:", bhaskara(1, 2, 5))




import numpy as np
import matplotlib.pyplot as plt

def grafico_quadratico(a, b, c):
    # Definir o intervalo de x (por exemplo, de -10 a 10)
    x = np.linspace(-10, 10, 400)
    
    # Calcular o valor de y usando a equação quadrática
    y = a * x**2 + b * x + c
    
    # Plotar o gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'$y = {a}x^2 + {b}x + {c}$')
    plt.title(f'Gráfico da função quadrática: $y = {a}x^2 + {b}x + {c}$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

# Exemplo de uso
grafico_quadratico(1, -3, 2)



