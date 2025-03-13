#Esse código serve para imprimir todos os números pares de 1 até o número digitado pelo usuário.

fim = int (input ("Digite o último número a imprimir:"))
x = 1
while x <= fim:
    if x % 2 ==0:
        print (x)
    x = x + 1