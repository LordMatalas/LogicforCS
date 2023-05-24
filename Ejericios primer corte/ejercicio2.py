def funcion(n):
    if n == 0:
        return 0
    elif n > 0:
        return n ** 2 + funcion(n - 1)

print(funcion(2))