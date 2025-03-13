matriz = [[0,0,0], [0,0,0],[0,0,0]]
somas = [0,0,0]
#Leitura da matriz
for l in range (3):
    for c in range (3):
        valor = int (input ("Digite um número:"))
        matriz [l] [c] = valor
# Varredura pelas colunas
for c in range (3):
    s = 0 # guarda a soma de uma coluna
    # Varre todas as linhas da coluna c e soma o valor
    for l in range (3):
        s += matriz [l] [c]
    somas[c] = s
# MOstrar as somas
print (somas)