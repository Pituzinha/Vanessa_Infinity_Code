#Faixa etária - Classifica a idade do usuario em tres categorias - criança menor 12 anos - adolescente entre 12 e 18 anos - adulto maiores de 18 anos.


a = int (input (" Digite a sua idade:"))
if a > 18:
    print ("Adulto")
else:
    if a >= 12:
        print ("Adolescente")
    else:
        print ("Criança")