
import numpy as np
# O NumPy é ideal para operações matemáticas com matrizes.
# Criando uma matriz NumPy 3x3
matriz_np = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("Matriz NumPy:\n", matriz_np)

#Operações com Matrizes
print("Soma dos elementos da matriz:", np.sum(matriz_np))
print("Media dos valores da matriz:", np.mean(matriz_np))
print("Transposta da matriz:\n", matriz_np.T) # Transposta

