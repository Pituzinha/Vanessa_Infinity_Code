#Usando o comando while, escreva um programa que leia vários números digitados pelo usuário e pare quando for lido Zero. Para cada número mostre: o número, o seu quadrado e a raiz quadrada.

import math
while True:
    nr = int (input ("Entre com um número:"))
    if nr == 0:
        break
    quadrado = nr * nr
    raiz = math.sqrt(nr)
    print(f"Número: {nr}, Quadrado: {quadrado}, Raiz: {raiz}")
    