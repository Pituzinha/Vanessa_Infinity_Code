# Escreva um programa que leia 10 temperaturas do teclado e as armazene em uma lista. Depois mostre a média de todas as temperaturas, a temperatura mais alta, e a mais baixa e a quantidade de temperaturas acima ou igual a 15 graus.

temp = []
for n in range (10):
    t = int (input ("Digite uma temperatura:"))
    temp.append(t)
maior = -1
menor = 99999
media = 0
qtde = 0
for n in range (10):
    media += temp[n]
    if temp[n] > maior:
        maior = temp[n]
    if temp[n] < menor :
        menor = temp[n]
    if temp[n] > 15:
        qtde += 1
media = media / 10
print (f"Média Total: {media}")
print (f"Maior Temperatura: {maior}")
print (f"Menor Temperatura: {menor}")
print (f"Quantidade >= 15 : {qtde}")

