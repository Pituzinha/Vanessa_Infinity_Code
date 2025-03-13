# Crie um programa que peça números ao usúario e continue somando até que o número zero seja digitado. 
soma = 0
numero = int(input("Digite um número (0 para parar)"))
while numero != 0:
    soma += numero
    numero = int(input("Digite um número (0 para parar)"))
print (f"A soma total é: {soma}")
