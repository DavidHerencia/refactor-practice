from app import CalculaGanador
import unittest
class TestCalculaGanador(unittest.TestCase):

    def test_archivo_no_encontrado(self):
        calc = CalculaGanador()
        with self.assertRaises(FileNotFoundError):
            calc.cargar_datos_de_csv('archivo_inexistente.csv')

    def test_archivo_valido(self):
        calc = CalculaGanador()
        datos = calc.cargar_datos_de_csv('0204.csv')
        self.assertIsInstance(datos, list)
        self.assertGreater(len(datos), 0)

    def test_encabezado_incorrecto(self):
        calc = CalculaGanador()
        # Simulamos un archivo con encabezado incorrecto
        datos = [
            ['region', 'provincia', 'distrito', 'dni', 'nombre_incorrecto', 'esvalido']
        ]
        with self.assertRaises(ValueError):
            calc.parse_encabezado(datos[0])

    def test_empate_votos(self):
        calc = CalculaGanador()
        datatest = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        resultado = calc.calcularganador(datatest)
        self.assertEqual(resultado, ['Aundrea Grace', 'Eddie Hinesley'])

    def test_ganador_unico(self):
        calc = CalculaGanador()
        datatest = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '0']
        ]
        resultado = calc.calcularganador(datatest)
        self.assertEqual(resultado, ['Eddie Hinesley'])

if __name__ == '__main__':
    unittest.main()