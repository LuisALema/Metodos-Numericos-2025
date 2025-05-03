import math

def f(x):
    return x - 2 * math.sin(x)

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

# Llamada correcta
raiz = biseccion(f, 1, 2, 1e-5, 100)
print("Raíz encontrada:", raiz)






