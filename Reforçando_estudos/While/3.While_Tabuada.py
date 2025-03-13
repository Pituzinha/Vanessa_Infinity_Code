# Crie um programa que imprime a tabuada de um número escolhido pelo usuario.
numero = int(input("Digite um número para ver a tabuada:"))
x = 1
while x <= 10:
    print (f"{numero} x {x} = {numero*x}")
    x += 1
     