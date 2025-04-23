# src/my_module.py

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def palindromo(string):
    return string == string[::-1]

def fibonacci(n):
    if n <= 0:
        raise ValueError("O número deve ser maior que zero.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

def contador_vogais(string):
    return sum(1 for char in string.lower() if char in 'aeiou')
