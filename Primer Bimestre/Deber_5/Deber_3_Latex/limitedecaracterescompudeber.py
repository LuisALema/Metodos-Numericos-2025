def biseccion(f, a, b, TOL, N0):
    i = 1
    FA = f(a)

    while i <= N0:
        p = a + (b - a) / 2
        FP = f(p)

        if FP == 0 or (b - a) / 2 < TOL:
            print("Procedimiento completado exitosamente.")
            return p

        i = i + 1

        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p

    print("El método fracasó después de", N0, "iteraciones.")
    return None
def funcion_prueba(x):
    return x**3 - 7*x**2 + 14*x - 6

raiz = biseccion(funcion_prueba, 0, 1, 1e-2, 100)

if raiz is not None:
    print("Raíz aproximada encontrada:", round(raiz, 4))
