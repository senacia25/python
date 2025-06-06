# import numpy as np

# #np abreviar biblioteca no código

# #saída o arrray e as cimensões pelo metodo ndim

# arr1d = np.array([1,2,3])
# print(f"Array 1d: {arr1d}, Dimensões: {arr1d.ndim}")

# arr2d = np.array([[1,2,3],[2,5,8]])
# print(f"Array 2d: {arr2d}, Dimensões: {arr2d.ndim}")

# arr3d = np.array([[[1,5,6],[2,7,4]],[[6,9,8],[5,6,4]]])
# print(f"Array 3d: {arr3d}, Dimensões: {arr3d.ndim}")

# #shape - indica o tamanho do array
# print(f"Shape do arr1d: {arr1d.shape}")
# print(f"Shape do arr1d: {arr2d.shape}")
# print(f"Shape do arr1d: {arr3d.shape}")

# #Dtype - tipo de dados 64
# array_fload = np.array([1.2,3.5,1.9])
# print(f"O dtype dessa array é: {array_fload.dtype}")
# print(f"O dtype dessa arr1d é: {arr1d.dtype}")

# #Itemsize - retorna o comprimento de cada elemento da matriz em bytes, o tamanho em bytes
# print(f"O itemsize do arr1d é: {arr1d.itemsize}")
# print(f"O itemsize do arr2d é: {arr2d.itemsize}")
# print(f"O itemsize do array_fload é: {array_fload.itemsize}")

#Ex:

# import numpy as np

# array1 = np.array([1, 5, 4, 6, 8])
# array2 = np.array([[1.5, 4.6, 8.2],[3.7, 5.8, 9.7]])

# print(f"A dimensão da Array 1: {array1.ndim}")
# print(f"A dimensão da Array 2: {array2.ndim}")
# print(f"Shape da Array 1: {array1.shape}")
# print(f"Shape da Array 2: {array2.shape}")
# print(f"O size da Array 1: {array1.size}")
# print(f"O size da Array 2: {array2.size}")
# print(f"O dtype da Array 1: {array1.dtype}")
# print(f"O dtype da Array 2: {array2.dtype}")
# print(f"O itemsize da Array 1: {array1.itemsize}")
# print(f"O itemsize da Array 2: {array2.itemsize}")


# import numpy as np

# rng = np.random.default_rng()

# #Criar array apartir de listas e tuplas

# lista_py = [1,2,4,5,6,8]
# print(lista_py)
# array_1d = np.array(lista_py)
# print(array_1d)

# lista2_py = [[5,5,1,4],[4,5,7,1]]
# array_2d = np.array(lista2_py)
# print(array_2d)

# #np.array converte tuplas e listas em array(arranjo)
# tupla = (1,2,5,4,5,6,2,4,8,2)
# array_tupla = np.array(tupla)
# print(array_tupla)

# # np.zeros - cria um array preenchido por zeros
# zero_array = np.zeros((3,3),int)#((3,3))
# print(f"Array de zero é:\n {zero_array}")

# #np.ones - preenche com 1
# ones_array = np.ones((2,3))
# print(ones_array)

# #np.full - cria uma array preenchida com números específicos
# full_array = np.full((2,4),7.5)
# print(full_array)

# # arange
# array_arange = np.arange(0,10,2)
# print(array_arange)

# array_float_arange = np.arange(0.0,1.0,0.25)
# print(array_float_arange)

# #array de números aleatórios -- importar rng = np.random.defalt_rng()
# arrray_aleatorios = rng.random((2,5))
# arrray_aleatorios = rng.integers(0, 60, size=6) #rng.integers(0, 60, size=6) para números aleatorios
# print(arrray_aleatorios)

# #indices em numpy
# #indices vetor
# array_indice = np.array([1,5,4,2,8])
# print(f"elemento 0: {array_indice[0]}") 
# print(f"elemento 3: {array_indice[3]}") 

# #indice matriz
# array_indicie2 = np.array([[1,5,6,4,6],[5,4,2,6,8]])
# print(f"Elemento da linha 0 e coluna 2: {array_indicie2[0,2]}")


# #slicing
# arr2d = np.array([[1, 2, 3, 4],
#                   [5, 6, 12, 13],
#                   [14, 7, 15, 16]])

# fatia2d_a = arr2d[:2, 1:3] # linha e coluna
# print(fatia2d_a)


# #operações matemáticas
# array_a = np.array([1,5,2,9])
# array_b = np.array([2,7,3,8])

# #soma
# soma = array_a + array_b
# print(soma)

# #multiplação
# soma = array_a * array_b
# print(soma)

# #subtração
# soma = array_a - array_b
# print(soma)

# #divisão
# soma = array_a / array_b
# print(soma)

# #copy e view
# precos = np.array([15.00, 10.99, 20.50])
# print(f"preços: {precos}")

# precoAjustado = precos # mesma coisa -  precoAjustado = precos.view()
# print(precos[0] * 2)

# precoAjustado2 = precos.copy() #copiou ([15.00, 10.99, 20.50]) agora se alterar a primeira não impacta nas egunda
# print(precoAjustado2)

# #Iteração

# array = np.array([1, 6, 5, 6, 2, 8, 9, 4, 7, 6, 3])
# for n in array:
#     print(f"Valor: {n}")
    

#Atv: 1    
# import numpy as np

# #Cria  alista que recebe a lista com parametro
# def criar_array(lista):

#     #np.array converte a lista em array
#     return np.array(lista)

# #the list
# numeros = [5,4,8,9,4,7]

# #printa e invoca a função passando a lista como argumento
# print(criar_array(numeros))
    

#Atv: 2

import numpy as np

def matriz_identidade(n):
    return np.identity(n) # para numero inteiro return np.identity(n, dtype=int)

print(matriz_identidade(10))
