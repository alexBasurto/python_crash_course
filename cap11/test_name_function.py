import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Pruebas para 'name_function.py'"""

    def test_first_last_name(self):
        """Funcionan nombres simples como 'Janis Joplin'?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """¿Funcionan nombres como 'Wolfgang Amadeus Mozart'?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()