A = 10
B = 20
def calculo():
    global A
    A = 100
    B = 200
print (f"Valores - A={A} , B={B}")
calculo()
print (f"Valores - A={A} , B={B}")

