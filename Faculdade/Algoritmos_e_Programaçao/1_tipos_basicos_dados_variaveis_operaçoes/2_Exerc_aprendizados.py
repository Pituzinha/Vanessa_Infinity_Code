# Faça um código que calcule o IMC 

peso = float(input("Quanto você pesa:"))   #input() - Captura entrada do usuario
altura = float(input("Qual é a sua altura:"))  #Float() - Converte o valor para número decimal
imc = peso / (altura ** 2)       # (/ )faz a divisão e (altura ** 2) eleva a altura ao quadrado (exponenciação)
print(f"Seu IMC é: {imc:.2f}")   #Print() - exibe o IMC na tela e (f"{imc:.2f}") formata o nº p mostrar apenas 2 casas decimais

#Opcional 
if imc < 18.5:  #Se o IMC for menor que 18.5, classifica como ABAIXO PESO.
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:   #Se o IMC estiver entre 18.5 e 24.9 , classifica como PESO NORMAl.
        print("Classificação: Peso Normal")
elif 25 <= imc < 29.9:  #Se o IMC estiver entre 25 e 29.9 , classifica como SOBREPESO.
        print("Classificação: Sobrepeso")
else:    #Se o IMC for 30 ou mais, classifica como OBESIDADE.
        print("Classificação: Obesidade")


