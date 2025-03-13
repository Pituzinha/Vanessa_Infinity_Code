# criação e manipulação de dicionarios 

#Dicionario vazio 
x = dict()
x
{} #resultado
y = {}
y
{} #resultado


#Dicionario preenchido
gastos = {"Aluguel": 3500.0, "luz": 250.0 }
print(gastos)
{'Aluguel': 3500.0, 'luz': 250.0} #resultado

#indexar o dicionario que criamos acima para podermos olhar os elementos (uma chave).
print(gastos ["aluguel"])
3500.00 #resultado

#acessar chave que não existe teremos o seguinte erro.
print (gastos ["internet"])
#traceback (most recent call last):
#File"<stdin>", line 1, in <module>
#KeyError: 'internet'
#acima erro obtido por não ter essa chave no dicionario.

#Adicionar novas chaves e novos elementos nesse dicionario pode indexiar chaves que não existe.Vamos adicionar o gasto com agua.
gastos ["agua"] = 120.0

#Não pode recuperar uma chave que não existe mas pode setar uma chave que não existe ai ele cria.
print(gastos)
{'aluguel': 3500.00, 'luz': 250.0, 'agua': 120.00}

#Se reatribuir um valor a uma chave exemplo a luz para valor 120.0
gastos["luz"] = 380.0
gastos
{'aluguel': 3500.0, 'luz': 380.0, 'agua': 120.0} #mostra que o valor da luz foi alterado.

 #Para remover um item usa o Del
del gastos ["luz"]
gastos
{'aluguel': 3500.0, 'agua': 120.0} #mostra que a luz foi removida.

#Para verificar se essa luz ainda existe.
"luz" in gastos
#false é o resultado, pois foi verificado se a chave luz esta dentro dos gastos do seu dicionario, como a chave não existe esse foi o resultado.

#Retornar todas as chaves e valores desse dicionario.
gastos.keys()
#dict_keys(['aluguel, 'agua']) é o que retorna mostrando todas as chaves dentro de gastos.

gastos.values()
#dict_values([3500.0, 120.0]) retornando todos os valores o que pode te ajudar a fazer laços ou algo do tipo.

#Para saber quantos elementos tem dentro de um dicionário
len(gastos)
2 #resposta