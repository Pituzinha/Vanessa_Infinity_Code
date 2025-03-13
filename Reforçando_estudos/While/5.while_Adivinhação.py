# Crie um programa onde o computador escolhe um número aleatorio de 1 a 10, e o usuario deve adivinhar quel é. O programa deve continuar até o usuario acertar.
import random
numero_secreto = random.randint(1,10)
tentativa = int(input("Tente adivinhar o número secreto de 1 a 10:"))
while tentativa != numero_secreto:
    tentativa = int(input("Errou! Tente Novamente:"))
print ("Parabéns, você acertou!")