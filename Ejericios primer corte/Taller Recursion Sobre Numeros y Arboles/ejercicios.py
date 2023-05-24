#Escriba el paso a paso de 2x[3]

def funcion1(n):
    if n == 0:
        return 0
    else:
        return 2 + funcion1(n-1)

funcion1(3)
#El resultado debe ser 6

def funcion2(n):
    if n == 0:
        return 0
    else:
        return funcion2(n-1)
    
def funcion3(n):
    if n == 0:
        return n
    else:
        funcion2(funcion3(funcion2(n)))

print(funcion3(3))