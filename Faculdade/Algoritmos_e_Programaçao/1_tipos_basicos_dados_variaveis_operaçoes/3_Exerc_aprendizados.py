# Escrevaum programa que recebe o número e exibe se é par ou impar
numero = int(input("Escreva um número:"))
if numero % 2 == 0 :
    print(f"O número {numero} é par.")
else: 
    print(f"O número {numero} é impar.")
    
# Porque usamos int() ? O input() sempre recebe texto(str). Se o usuario digitar 10, sem int(), o Py 
# entenderia como 10 (string) e não número.
# % - operador modulo retorna resto da divisão, 