def f(x):
    if x == 2:
        return float('inf')  # evitar división por cero
    return ((x + 2) * (x + 1)**2 * x * (x - 1)**3) / (x - 2)

def biseccion(f, a, b, tol, max_iter):
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        return None  # no hay cambio de signo

    for i in range(max_iter):
        p = (a + b) / 2
        fp = f(p)

        if abs(fp) < tol or (b - a) / 2 < tol:
            return p

        if fa * fp < 0:
            b = p
            fb = fp
        else:
            a = p
            fa = fp

    return (a + b) / 2

# Intervalos a analizar
intervalos = [
    [-1.5, 2.5],
    [-0.5, 2.4],
    [-0.5, 3],
    [-3, -0.5]
]

for i, intervalo in enumerate(intervalos):
    a, b = intervalo
    raiz = biseccion(f, a, b, 1e-5, 100)
    if raiz is not None:
        print(f"Intervalo {chr(97+i)}) [{a}, {b}] -> Raíz aproximada: {raiz:.5f}")
    else:
        print(f"Intervalo {chr(97+i)}) [{a}, {b}] -> No hay cambio de signo")
