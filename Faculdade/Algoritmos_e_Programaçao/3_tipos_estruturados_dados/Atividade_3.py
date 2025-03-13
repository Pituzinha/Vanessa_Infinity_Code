# Imagine que você fará um almoço para um amigo. Como ambos tem restrições alimentares, você decidiu criar duas listas uma com o que você pode comer e outra com o que seu amigo pode comer. O almoço deve ser feito com igredientes que ambos podem comer. 

alimentos = []
alimentos_amigo = []
while True:
    x = input("Digite o seu alimento:")
    if x == "":
        break
    alimentos.append(x)
while True:
    x = input("Digite os alimentos do seu amigo:")
    if x == "":
        break
    alimentos_amigo.append(x)
conj1 = set (alimentos)
conj2 = set (alimentos_amigo)
conj_permitidos = conj1 & conj2
print ("Os alimentos permitidos são:")
for x in conj_permitidos:
    print (x)