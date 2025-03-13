#vamos varrer todos os itens de um dicionario usando o FOR
compras = {"arroz": 5, "feijão": 3, "cebola": 2} #lista de compras
for nome, quantidade in compras.items(): #laço atriu 2 variaveis a cada volta pois depois do in temos compras.items() que é um metodo que retorna todos os itens do dicionário basicamente como uma lista de tupas.Assim atribuios as duas variaveis no for.
    print (f"Compre {quantidade} de {nome}") #mostramos os valores relacionados 