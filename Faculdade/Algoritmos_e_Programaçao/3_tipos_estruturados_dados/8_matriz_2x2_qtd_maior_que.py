linhas = 2
colunas = 2
matriz = []
for l in range (linhas):
    linhas_aloc = [0] * colunas
    matriz.append (linhas_aloc)
for l in range (linhas):
    for c in range (colunas):
        valor = int (input ("Digite o valor:"))
        matriz [l] [c] = valor
qtde = 0 
for l in range (linhas):
    for c in range (colunas):
        if matriz [l] [c] > 10 :
            qtde += 1
print (f"Tem {qtde} números maiores que 10.")
