import Libreriacomplejos as lc
import unittest
import math

class TestOperaciones(unittest.TestCase):

    def test_sumac(self):
        suma = lc.suma((1.5, 2.3), (3, 4))
        self.assertAlmostEquals(suma[0], 4.5)
        self.assertAlmostEquals(suma[1], 6.3)
        suma = lc.suma((-1, 2), (5, 5.3))
        self.assertAlmostEquals(suma[0], 4)
        self.assertAlmostEquals(suma[1], 7.3)

    def test_producto(self):
        producto = lc.producto((1, 2), (-3, 4))
        self.assertAlmostEquals(producto[0], -11)
        self.assertAlmostEquals(producto[1], -2)
        producto = lc.producto((-1, -2), (5, 5))
        self.assertAlmostEquals(producto[0], 5)
        self.assertAlmostEquals(producto[1], -15)

    def test_resta(self):
        resta = lc.resta((1.5, 2.3), (3.4, 4.1))
        self.assertAlmostEquals(resta[0], -1.9)
        self.assertAlmostEquals(resta[1], -1.8)
        resta = lc.resta((-1.2, -2.7), (5.9, 5.2))
        self.assertAlmostEquals(resta[0], -7.1)
        self.assertAlmostEquals(resta[1], -7.9)

    def test_division(self):
        division = lc.division((12, 1), (1, 4))
        self.assertAlmostEquals(division[0], 0)
        self.assertAlmostEquals(division[1], 0)
        division = lc.division((-1, -2), (5, 5))
        self.assertAlmostEquals(division[0], -0.3)
        self.assertAlmostEquals(division[1], 0.1)

    def test_modulo(self):
        modulo = lc.modulo((3, 4))
        self.assertAlmostEquals(modulo[0], 5)
        modulo = lc.modulo(-1, -2)
        self.assertAlmostEquals(modulo[0], 2.236)

    def test_conjugado(self):
        conjugado = lc.conjugado(2, 3)
        self.assertAlmostEquals(conjugado[0], 2)
        self.assertAlmostEquals(conjugado[1], -3)
        conjugado = lc.conjugado(3, -5)
        self.assertAlmostEquals(conjugado[0], 3)
        self.assertAlmostEquals(conjugado[1], 5)

    def test_polar_cartesiano(self):
        polar = lc.polar_cartesiano(5.9,math.pi/3)
        self.assertAlmostEquals(polar[0], -2.95)
        self.assertAlmostEquals(polar[1], 5.12)
        polar = lc.polar_cartesiano(2.7, math.pi/4)
        self.assertAlmostEquals(polar[0], 1.91)
        self.assertAlmostEquals(polar[1], 1,91)

    def test_cartesiano_polar(self):
        cartesiano = lc.cartesiano_polar(2, 3)
        self.assertAlmostEquals(cartesiano[0], 2)
        self.assertAlmostEquals(cartesiano[1], -3)
        cartesiano = lc.cartesiano_polar(3, -5)
        self.assertAlmostEquals(cartesiano[0], 3)
        self.assertAlmostEquals(cartesiano[1], 5)

    def test_fase(self):
        fase = lc.fase((3.7, 4.2))
        self.assertAlmostEquals(fase[0], 0)
        fase = lc.fase((-1.5, -2.9))
        self.assertAlmostEquals(fase[0], 2)


if __name__ == '__main__':
    unittest.main()
