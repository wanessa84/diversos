# Matriz 3x3 usando listas aninhadas
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Acessando um elemento (linha 2, coluna3)
print("Elemento nza posição (2,3):", matriz[1][2]) #saída: 6


#Manipulação da Matriz
#Percorrendo a matriz e imprimindo os valores
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
        print()
        

