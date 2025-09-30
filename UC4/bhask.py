import math

def bhaskara(a,b,c):    #(a,b,c) = parâmetros
    delta = b**2-4*a*c            # ** quadrado
    if delta < 0:
        return "Não possui raízes reais"
    
    x1 = (-b + math.sqrt(delta)) /(2*a)
    x2 = (-b - math.sqrt(delta)) /(2*a)
    return x1, x2

raizes = bhaskara(1, -3, 2)
print("Raízes da equção:", raizes)
print(f"Raízes da equção:", bhaskara(1, 2, 5))
