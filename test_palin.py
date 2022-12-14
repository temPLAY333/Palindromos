import unittest
from palindromo import *

class Testpingo(unittest.TestCase):
    def test1(self):
        self.assertEqual(IsthisaPalindromo("ana"),"Yes Yes Yes Yes Yes")
    def test2(self):
        self.assertEqual(IsthisaPalindromo("Ana"),"Yes Yes Yes Yes Yes")
    def test3(self):
        self.assertEqual(IsthisaPalindromo("A"),"Yes Yes Yes Yes Yes")
    def test4(self):
        self.assertEqual(IsthisaPalindromo("5"),"Yes Yes Yes Yes Yes")
    def test5(self):
        self.assertEqual(IsthisaPalindromo(5),"No No No No No No")
    def test6(self):
        self.assertEqual(IsthisaPalindromo("5A5"),"Yes Yes Yes Yes Yes")
    def test7(self):
        self.assertEqual(IsthisaPalindromo("   "),"Yes Yes Yes Yes Yes")
    def test8(self):
        self.assertEqual(IsthisaPalindromo("AN A"),"Yes Yes Yes Yes Yes")
    def test9(self):
        self.assertEqual(IsthisaPalindromo("Somos o no somos"),"Yes Yes Yes Yes Yes")

if __name__ == "__main__": # pragma: no cover
    unittest.main()