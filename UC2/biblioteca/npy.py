import numpy as np

#np abreviar biblioteca no código

#saída o arrray e as cimensões pelo metodo ndim

arr1d = np.array([1,2,3])
print(f"Array 1d: {arr1d}, Dimensões: {arr1d.ndim}")

arr2d = np.array([[1,2,3],[2,5,8]])
print(f"Array 2d: {arr2d}, Dimensões: {arr2d.ndim}")

arr3d = np.array([[[1,5,6],[2,7,4]],[[6,9,8],[5,6,4]]])
print(f"Array 3d: {arr3d}, Dimensões: {arr3d.ndim}")

#shape - indica o tamanho do array
print(f"Shape do arr1d: {arr1d.shape}")
print(f"Shape do arr1d: {arr2d.shape}")
print(f"Shape do arr1d: {arr3d.shape}")