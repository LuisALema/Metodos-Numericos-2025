## Primer Ejercicio
def f(x):
    return x**3 - 7*x**2 + 14*x - 6

def biseccion(a, b, tol):
    if f(a) * f(b) >= 0:
        print("No se puede aplicar bisección en el intervalo [", a, ",", b, "]")
        return None
    while abs(b - a) > tol:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# Intervalos del ejerccio
intervalos = [(0, 1), (1, 3.2), (3.2, 4)]
for a, b in intervalos:
    raiz = biseccion(a, b, 1e-2)
    print(f"Raíz aproximada en [{a}, {b}]: {raiz:.4f}")
