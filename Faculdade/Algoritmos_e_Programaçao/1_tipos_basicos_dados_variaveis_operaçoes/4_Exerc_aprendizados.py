# Crie um programa que pergunta a idadde e diz se pode votar.
idade = int (input("Qual é a sua idade:"))
if idade < 16:  # se for menor de idade
    print("Você Não pode votar")
elif 16 <= idade < 18 or idade >= 70:  # Se estiver entre 17 e 18 ou 70+, OR é para combinar as duas condições
        print("Voto opcional")
else:    # Se não for nenhuma das anterires idade entre 18 a 69
        print("Voto Obrigatorio")