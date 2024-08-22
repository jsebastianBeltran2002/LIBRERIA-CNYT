import math
import unittest
import ecuaciones as lc

class TestlibrarycMethods(unittest.TestCase):

    def test_suma(self):
        a = (1, 1)
        b = (2, 3)
        suma = lc.sumar(a, b)
        self.assertEqual(suma, (3, 4))

        a = (-5, 7)
        b = (2, -3)
        suma2 = lc.sumar(a, b)
        self.assertEqual(suma2, (-3, 4))

    def test_resta(self):
        a = (8, 6)
        b = (3, 2)
        resta = lc.restar(a, b)
        self.assertEqual(resta, (5, 4))

        a = (-4, -5)
        b = (2, 3)
        resta2 = lc.restar(a, b)
        self.assertEqual(resta2, (-6, -8))

    def test_multiplicacion(self):
        a = (2, 3)
        b = (4, -1)
        producto = lc.multiplicar(a, b)
        self.assertEqual(producto, (11, 10))

        a = (-3, 5)
        b = (1, 2)
        producto2 = lc.multiplicar(a, b)
        self.assertEqual(producto2, (-13, -1))

    def test_division(self):
        a = (8, 4)
        b = (2, 2)
        division = lc.dividir(a, b)
        self.assertAlmostEqual(division[0], 3.0, places=7)
        self.assertAlmostEqual(division[1], -1.0, places=7)

        a = (7, -5)
        b = (1, 1)
        division2 = lc.dividir(a, b)
        self.assertAlmostEqual(division2[0], 1.0, places=7)
        self.assertAlmostEqual(division2[1], -6.0, places=7)

    def test_modulo(self):
        a = (3, 4)
        modulo = lc.modulo(a)
        self.assertAlmostEqual(modulo, 5.0)

        a = (-8, 6)
        modulo2 = lc.modulo(a)
        self.assertAlmostEqual(modulo2, 10.0)

    def test_conjugado(self):
        a = (4, -3)
        conjugado = lc.conjugado(a)
        self.assertEqual(conjugado, (4, 3))

        a = (-6, 2)
        conjugado2 = lc.conjugado(a)
        self.assertEqual(conjugado2, (-6, -2))

    def test_polar_a_cartesiano(self):
        a = (7, 1.2)
        polar1 = lc.polar_a_cartesiano(a)
        self.assertAlmostEqual(polar1[0], 7 * math.cos(1.2))
        self.assertAlmostEqual(polar1[1], 7 * math.sin(1.2))

        a = (10, 0.5)
        polar2 = lc.polar_a_cartesiano(a)
        self.assertAlmostEqual(polar2[0], 10 * math.cos(0.5))
        self.assertAlmostEqual(polar2[1], 10 * math.sin(0.5))

    def test_cartesiano_a_polar(self):
        a = (5, 12)
        polar1 = lc.cartesiano_a_polar(a)
        self.assertAlmostEqual(polar1[0], math.sqrt(5**2 + 12**2))
        self.assertAlmostEqual(polar1[1], math.atan2(12, 5))

        a = (-7, -24)
        polar2 = lc.cartesiano_a_polar(a)
        self.assertAlmostEqual(polar2[0], math.sqrt((-7)**2 + (-24)**2))
        self.assertAlmostEqual(polar2[1], math.atan2(-24, -7))

    def test_fase(self):
        a = (1, 1)
        fase1 = lc.fase(a)
        self.assertAlmostEqual(fase1, math.atan2(1, 1))

        a = (-3, 4)
        fase2 = lc.fase(a)
        self.assertAlmostEqual(fase2, math.atan2(4, -3))

if __name__ == '__main__':
    unittest.main()

