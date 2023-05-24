#1 Clase Lógica para CS

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

x = int(input('Digite un numero: '))

print("El factorial de",x, "es:", int(factorial(x)))