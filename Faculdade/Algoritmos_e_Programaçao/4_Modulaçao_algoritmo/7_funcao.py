import math
def bhaskara (A, B, C):
    delta = B ** 2 - 4 * A * C
    if delta < 0:
        x1 = None
        x2 = None
    elif delta == 0:
        x1 = -B / (2 * A)
        x2 = None
    else:
        x1 = (-B + math.sqrt(delta)) / (2*A)
        x2 = (-B - math.sqrt(delta)) / (2*A)
    return (x1, x2)
A = int(input("Entre com A:"))
B = int(input("Entre com B:"))
C = int(input("Entre com C:"))
(R1, R2) = bhaskara (A, B, C)
print(f"As raizes são: X1 = {R1}, X2 = {R2}")


