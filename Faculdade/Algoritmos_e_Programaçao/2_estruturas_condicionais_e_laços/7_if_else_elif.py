#Calcule quanto um usuário gasta de energia baseada na faixa KWH e no preço por tipo de construção.
kwh = int (input ("Digite os KWH:"))
tipo = input ("Qual é o tipo (R,C ou I):")
preço = 0.0
if tipo == "R":
    if kwh <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif tipo =="C":
    if kwh <= 1000:
        preço = 0.55
    else:
        preço = 0.60
elif kwh <= 5000:
    if kwh <= 5000:
        preço = 0.55
    else: 
        preço = 0.60
valor = kwh * preço
print (f"O total a pagar é R$ {valor}.")