# Crie um dicionario para manter os dados de uma pessoa : nome, e-mamil e idade. Faça a leitura desses dados do teclado e, depois usando um laço, imprima todas as chaves e valores do dicionário.

pessoa = {}
nome = input ("Digite o nome:")
email = input ("Digite o seu e-mail:")
idade = int(input ("Digite a sua idade:"))
pessoa ["nome"] = nome
pessoa ["e-mail"] = email
pessoa ["idade"] = idade
for chave, valor in pessoa.items():
    print (f"Chave: {chave}, Valor: {valor}")
