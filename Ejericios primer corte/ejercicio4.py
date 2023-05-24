def funcion(n):
    if n == 0:
        return 1
    elif n > 0:
        return (n+1) ** 3 + funcion(n-1)
    
print(funcion(20))