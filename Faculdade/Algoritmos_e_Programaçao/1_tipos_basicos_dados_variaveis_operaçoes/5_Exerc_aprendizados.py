# Se NÃO estiver chovendo OU se ela tiver guarda-chuva, ela pode sair.

chovendo = input("Esta chovendo ?").strip().lower() == "Sim"
tem_guarda_chuva = input ("Você tem guarda-chuva").strip().lower() == "Sim"
# .strip().lower() - Remove espaços extras e coloca a resposta em minuscula.0

if not chovendo or tem_guarda_chuva:
    print("Vou sair")
else:
    print("Ficarei em casa")