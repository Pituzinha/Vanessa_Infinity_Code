#calculando a média a partir de entradas do usuário

Temperaturas = []
while True:
    T = int ( input ("Digite uma temperatura: (0 para sair)"))
    if T == 0:
        break
    Temperaturas. append(T)
tamanho = len(Temperaturas)
soma = 0 
for T in Temperaturas:
    soma += T
media = soma / tamanho
print (f"A média é: {media}.")