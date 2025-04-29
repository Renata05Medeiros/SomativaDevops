# tests/test_calculos.py
import unittest

# Funções que você quer testar
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def multiplicar(a, b):
    return a * b

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Testes
class TestSomar(unittest.TestCase):
    def test_somar_positivos(self):
        self.assertEqual(somar(2, 3), 5)
    
    def test_somar_negativos(self):
        self.assertEqual(somar(-2, -3), -5)
    
    def test_somar_positivo_negativo(self):
        self.assertEqual(somar(2, -3), -1)


class TestSubtrair(unittest.TestCase):
    def test_subtrair_positivos(self):
        self.assertEqual(subtrair(5, 3), 2)
    
    def test_subtrair_negativos(self):
        self.assertEqual(subtrair(-5, -3), -2)
    
    def test_subtrair_positivo_negativo(self):
        self.assertEqual(subtrair(5, -3), 8)


class TestDividir(unittest.TestCase):
    def test_dividir_positivos(self):
        self.assertEqual(dividir(6, 3), 2)
    
    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(5, 0)
    
    def test_dividir_positivo_negativo(self):
        self.assertEqual(dividir(6, -3), -2)


class TestMultiplicar(unittest.TestCase):
    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(3, 2), 6)
    
    def test_multiplicar_negativos(self):
        self.assertEqual(multiplicar(-3, -2), 6)
    
    def test_multiplicar_positivo_negativo(self):
        self.assertEqual(multiplicar(3, -2), -6)


class TestEhPrimo(unittest.TestCase):
    def test_primo(self):
        self.assertTrue(eh_primo(5))
    
    def test_nao_primo(self):
        self.assertFalse(eh_primo(4))
    
    def test_numero_negativo(self):
        self.assertFalse(eh_primo(-7))


if __name__ == '__main__':
    unittest.main()
