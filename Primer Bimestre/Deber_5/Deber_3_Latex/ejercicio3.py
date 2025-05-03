import math

# Función f(x) = x - tan(x), se busca el punto donde x = tan(x)
def f(x):
    return x - math.tan(x)

# Método de bisección
def biseccion(f, a, b, TOL, N0):
    i = 1
    FA = f(a)

    while i <= N0:
        p = a + (b - a) / 2
        FP = f(p)

        if FP == 0 or (b - a) / 2 < TOL:
            print("Procedimiento completado exitosamente.")
            return p

        i += 1

        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p

    print("El método fracasó después de", N0, "iteraciones.")
    return None

# Intervalo adecuado (evitamos la asíntota vertical de tan(x))
raiz = biseccion(f, 0.0, 1.4, 1e-5, 100)

if raiz is not None:
    print("Raíz aproximada encontrada:", round(raiz, 6))

## precaución no usar mas de b= 1.57o mas de la tan(x)

