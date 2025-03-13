#Escreva um programa que o usuario entre com dois numeros: linhas e colunas. O programa deve imprimir um retangulo de cerquilha # contendo a quantidade de linhas e colunas fornecidas. Use os comando FOR e RANGE.

linhas = int (input ("Digite o número de linhas:"))
colunas = int (input ("Digite o número de colunas:"))
for l in range (linhas):
    for c in range (colunas):
        print("#" , end="")
    print()

#    