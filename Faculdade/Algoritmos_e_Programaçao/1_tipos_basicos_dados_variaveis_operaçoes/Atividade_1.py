#Sabemos que dado um triângulo, retângulo,  a partir dos valores se seus catetos, a hipotenusa é calculado pelo teorema de Pitágoras da seguinte forma: 
#1 - Leia os valores do cateto em duas variáveis: A e B
#2 - Calcule o valor da hipotenusa e atribua-o á variável C.
#3 - Apresente os valores dos catetos e da hipotenusa.

import math
A = int (input ("Digite o Cateto A:"))
B = int (input ("Digite o Cateto B:"))
C = math.sqrt (A**2 + B**2)
print (f" Cateto A: {A}, Cateto B: {B}, Hipotenusa:{C}.")

#Para colocar em duas casas decimais 

import math
A = float(input("Digite o valor do primeiro cateto (A): "))
B = float(input("Digite o valor do segundo cateto (B): "))
C = math.sqrt(A**2 + B**2)
print(f"Cateto A: {A}, Cateto B: {B}, Hipotenusa: {C:.2f}.")