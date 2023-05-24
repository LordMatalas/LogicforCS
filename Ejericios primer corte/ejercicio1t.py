#Sean n, m n´umeros naturales. Defina las funciones 2×[n], Pred[n] y m−[n] de la siguiente
# manera:

def funcion(n):
    if n == 0:
        return 0
    else:
        return 2 + funcion(n-1)

print(funcion(3))