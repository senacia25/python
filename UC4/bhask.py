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

#===========================
#===========================

# import numpy as np
# import matplotlib.pyplot as plt

# def grafico_quadratico(a, b, c):
#     # Definir o intervalo de x (por exemplo, de -10 a 10)
#     x = np.linspace(-10, 10, 400)
    
#     # Calcular o valor de y usando a equação quadrática
#     y = a * x**2 + b * x + c
    
#     # Plotar o gráfico
#     plt.figure(figsize=(8, 6))
#     plt.plot(x, y, label=f'$y = {a}x^2 + {b}x + {c}$')
#     plt.title(f'Gráfico da função quadrática: $y = {a}x^2 + {b}x + {c}$')
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.axhline(0, color='black',linewidth=0.5)
#     plt.axvline(0, color='black',linewidth=0.5)
#     plt.grid(True)
#     plt.legend()
#     plt.show()

# # Exemplo de uso
# grafico_quadratico(1, -3, 2)

#===========================
#===========================

# import numpy as np
# import matplotlib.pyplot as plt

# # Definição da função
# def f(x):    #f(x) = y
#     return 2*x - 4

# # Raiz
# raiz = 4/2

# # Intervalo de valores
# x = np.linspace(-2, 5, 100)
# y = f(x)
# print ("Valores de x:", x[:10]) # mostar so os 10 ao invés de 100
# print ("Valores de y:",y[:10])
# # Gráfico
# plt.axhline(0, color="black", linewidth=1)
# plt.axvline(0, color="black", linewidth=1)
# plt.plot(x, y, label="f(x) = 2x - 4")
# plt.scatter(raiz, 0, color="red", label=f"Raiz: x={raiz}")
# plt.legend()
# plt.grid(True)
# plt.show()

#===========================
#===========================

# import numpy as np
# import matplotlib.pyplot as plt

# # Definição da função
# def f(x):    #f(x) = y
#     return 5*x + 10

# # Raiz
# raiz = -10 / 5

# # Intervalo de valores
# x = np.linspace(-2, 5, 100)
# y = f(x)

# print ("Valores de x:", x[:5])
# print ("Valores de y:",y[:5])

# # Gráfico
# plt.axhline(0, color="black", linewidth=1)
# plt.axvline(0, color="black", linewidth=1)
# plt.plot(x, y, label="f(x) = 5x + 10")
# plt.scatter(raiz, 0, color="red", label=f"Raiz: x={raiz}")
# plt.legend() # caso queira mudar o local onde aparece  legenda usar loc=..loc='upper left') upper superior, pode ser center, entre outros
# plt.grid(True)
# plt.show()

#===========================
#===========================

import numpy as np
import matplotlib.pyplot as plt

def f(a):
    return 2*x**2 + 2*x - 1
    # v = np.array([2*x**2 + 2*x - 1])
    # r = f(x)(v)

# x = np.linspace(-3, 3, 7)     
# y = f(x)
# se quiser como array, y chama a função com o parametro variavel x
x = np.array([-3, -2, -1, 0, 1, 2, 3])
y = f(x)

plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.plot(x, y, label="f(x) = 2x² + 2x - 1", color="red")
plt.legend() # caso queira mudar o local onde aparece  legenda usar loc=..loc='upper left') upper superior, pode ser center, entre outros
plt.grid(True)
plt.show()