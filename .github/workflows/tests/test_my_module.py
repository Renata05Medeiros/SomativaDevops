import unittest
from src.my_module import soma, subtrai, palindromo, fibonacci, contador_vogais

class TestMyModule(unittest.TestCase):

    # Testando a função soma
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)
        self.assertEqual(soma(-5, -5), -10)

    # Testando a função subtrai
    def test_subtrai(self):
        self.assertEqual(subtrai(5, 3), 2)
        self.assertEqual(subtrai(0, 1), -1)
        self.assertEqual(subtrai(5, 5), 0)
        self.assertEqual(subtrai(-5, -3), -2)

    # Testando a função palindromo
    def test_palindromo(self):
        self.assertTrue(palindromo('ana'))
        self.assertTrue(palindromo('arara'))
        self.assertFalse(palindromo('hello'))
        self.assertFalse(palindromo('python'))

    # Testando a função fibonacci
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 0)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(5), 3)
        self.assertEqual(fibonacci(10), 34)
        with self.assertRaises(ValueError):
            fibonacci(0)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    # Testando a função contador_vogais
    def test_contador_vogais(self):
        self.assertEqual(contador_vogais("aeiou"), 5)
        self.assertEqual(contador_vogais("python"), 1)
        self.assertEqual(contador_vogais("aeiooo"), 6)
        self.assertEqual(contador_vogais("rhythm"), 0)

if __name__ == '__main__':
    unittest.main()
