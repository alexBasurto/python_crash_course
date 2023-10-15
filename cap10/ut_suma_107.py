import unittest
from unittest.mock import patch
import io
import sys

import suma_107

class TestSuma(unittest.TestCase):
    def test_suma_numeros(self):
        # Simulamos la entrada del usuario para los números 5 y 7
        with patch('builtins.input', side_effect=['5', '7', 'q']):
            # Redirigimos la salida estándar a un objeto io.StringIO para capturarla
            captured_output = io.StringIO()
            sys.stdout = captured_output

            # Ejecutamos la función principal
            suma_107.main()

            # Restauramos la salida estándar
            sys.stdout = sys.__stdout__

            # Comprobamos la salida esperada
            self.assertEqual(captured_output.getvalue(), "\nPor favor, indique dos números para que sean sumados:\nIntroduzca 'q' para salir del programa.\n\nIndique el primer número: Indique el segundo número: 12\n")

    def test_suma_caracteres_no_numericos(self):
        # Simulamos la entrada del usuario para un carácter no numérico y luego 'q'
        with patch('builtins.input', side_effect=['a', 'q']):
            captured_output = io.StringIO()
            sys.stdout = captured_output

            suma_107.main()

            sys.stdout = sys.__stdout__

            self.assertEqual(captured_output.getvalue(), "\nPor favor, indique dos números para que sean sumados:\nIntroduzca 'q' para salir del programa.\n\nIndique el primer número: Solo se admiten caracteres numéricos.\n")

if __name__ == '__main__':
    unittest.main()
