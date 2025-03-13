#Código contém vários exemplos de loops, incluindo criação de listas, break dentro do for loops.

list(range(6))
list (range (12, -1, -2))

for tabuada in range (1,11):
    for numero in range (1,11):
        valor = tabuada * numero
        print (f"{tabuada} * {numero} = {valor}")

for x in range (1,11):
    if x == 3:
        break 
    print (x)

for x in range (1,11):
    if x ==3 :
        continue
    print (x)


