import unittest
from main import sua_funcao

class TestMain(unittest.TestCase):

    def test_exemplo_1(self):
        self.assertEqual(sua_funcao(2), 4)

    def test_exemplo_2(self):
        self.assertTrue(sua_funcao(0) >= 0)

    def test_exemplo_3(self):
        self.assertIsInstance(sua_funcao(5), int)

    def test_exemplo_4(self):
        self.assertNotEqual(sua_funcao(3), 0)

    def test_exemplo_5(self):
        self.assertLess(sua_funcao(1), 10)

if __name__ == '__main__':
    unittest.main()
