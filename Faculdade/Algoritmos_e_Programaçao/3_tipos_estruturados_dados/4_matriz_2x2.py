#Ler dados da matriz - Cria uma matriz 2x2, permite que o usuário insira valores e depois imprime a matriz de duas formas:
#como uma lista de listas - print(matriz) e formatada, como uma matriz visual (print(matriz[l] [c], end= " "))

linhas = 2
colunas = 2 
matriz = []
for l in range (linhas):
    linhas_aloc = [0] * colunas
    matriz.append (linhas_aloc)
for l in range (linhas):
    for c in range (colunas):
        valor = int (input ("Digite um valor:"))
        matriz [l] [c] = valor 
print (matriz)
for l in range (linhas):
    for c in range (colunas):
        print (matriz [l] [c], end=" ")
    print ()