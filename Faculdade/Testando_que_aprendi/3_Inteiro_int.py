# Receba um número inteiro e exiba a tabuada de 1 a 10.
numero = int (input ("Digite um número inteiro:"))
for i in range (1,11):          # O laço FOR repeti um bloco de codigo. Criando a variavel i que assume os valores de 1 a 10 um por x.
                                # RANGE(1,11) - Cria de 1 a 10.    
    resultado = numero * i  # Multiplica o número digitado pelo contador i de repetição.
    print(f"{numero} * {i} = {resultado}")

    
    
# a cada reprodução, i assuma um novo valor e o código dentro do FOR é executado novamente.