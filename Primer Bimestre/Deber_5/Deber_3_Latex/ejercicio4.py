import math

# Definimos la función f(x) = x^2 - 1 - e^(1 - x^2)
def f4(x):
    return x**2 - 1 - math.exp(1 - x**2)

# Método de bisección
def biseccion(f, a, b, TOL, N0):
    i = 1
    FA = f(a)

    while i <= N0:
        p = a + (b - a) / 2
        FP = f(p)

        if FP == 0 or (b - a) / 2 < TOL:
            return p

        i += 1

        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p

    return None

# Se busca una raíz en el intervalo [-2, 0] con tolerancia 10^-3
raiz = biseccion(f4, -2, 0, 1e-3, 100)

if raiz is not None:
    print(f"Raíz aproximada en [-2, 0]: {raiz:.4f}")
else:
    print("No se encontró solución en el intervalo dado.")
