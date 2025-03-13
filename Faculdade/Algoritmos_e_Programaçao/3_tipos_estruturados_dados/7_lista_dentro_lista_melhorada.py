#melhora a organização da sáida, tornando a exibição mais estruturada e legivel.

arroz = ["arroz", 5, 8.50]
feijão = ["feijão", 1,12.40]
print(arroz)
print(feijão)
compras = [arroz, feijão]
for item in compras:
    print (f"Produto:{item[0]}")
    print (f"Quantidade:{item[1]}")
    print (f"Valor:{item[2]}")