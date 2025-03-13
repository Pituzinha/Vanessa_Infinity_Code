#Alocação e varredura de elementos de uma matriz - cria uma matriz (lista de listas) tamanho 2x2 (2 linhas e 2 colunas) e faz a varredura dos elementos, imprimindo as suas posições.

linhas = 2
colunas = 2 
matriz = []
for l in range(linhas):
    linhas_aloc = [0] * colunas
    matriz.append (linhas_aloc)
for l in range (linhas):
    for c in range (colunas):
        print (f"Linhas {l}, Colunas: {c}")