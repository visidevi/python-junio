def factorial(n):
    """ Calcula el factorial de n.

    n int > 0, n es un entero que es mayor que 0
    regresa n! = n factorial
    """
    if n == 1:
        return n
    print(n)
    return n * factorial(n-1)

n = int(input('Escribe un entero: '))
print(factorial(n))