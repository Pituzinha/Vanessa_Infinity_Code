# Calcule o resultado da expressão A > 1000 and B < C and D or E utilizando a tabela Valor A-1500, 500, 2000 B-50, 20, 30 C-100, 21, 10 D-True, True, False E-False, True, False.

#Expressão: A > 1000 and B< C and D or E

# Definição dos conjuntos de valores
valores = [{"A": 1500, "B": 50, "C": 100, "D": True, "E": False}, {"A": 500, "B": 20, "C":21, "D":True, "E": True} , {"A": 2000, "B": 30, "C":10, "D":False, "E": False}, ]

# Expressão Lógica aplicada a cada conjunto de valores
for i, v in enumerate (valores, 1):
    resultado = (v["A"] > 1000 and v ["B"] < v ["C"] and v ["D"]) or v ["E"]
    print (f" Conjunto {i}:{resultado}")