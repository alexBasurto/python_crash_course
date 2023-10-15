import unittest
from ciudad_funciones import formato_ciudad_pais

class NameTestCases(unittest.TestCase):
    """Pruebas para 'ciudad_funciones.py'"""

    def test_ciudad_pais(self):
        """Funcionan entradas simples como 'Bilbao, España'"""
        ciudad_formato = formato_ciudad_pais('bilbao', 'españa')
        self.assertEqual(ciudad_formato, "Bilbao, España.")
    
    def test_ciudad_pais_habitantes(self):
        """Funcionan entradas de ciudad, país y número habitantes."""
        ciudad_formato = formato_ciudad_pais('nueva york', 'estados unidos', 8_468_000)
        self.assertEqual(ciudad_formato, "Nueva York, Estados Unidos - habitantes 8468000.")

if __name__ == '__main__':
    unittest.main()