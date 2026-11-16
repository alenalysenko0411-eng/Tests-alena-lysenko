"""Unit-тесты модуля square.py (квадрат).

Ожидаемые значения взяты из формул в docs/README.md:
площадь S = a^2, периметр P = 4a.

Пример запуска:
    python -m unittest tests.test_square -v
"""
import unittest

import square


class SquareAreaTestCase(unittest.TestCase):
    """Тесты функции square.area(a)."""

    def test_area_integer_side(self):
        """Сторона 5: площадь 25.

        Пример: square.area(5) -> 25
        """
        self.assertEqual(square.area(5), 25)

    def test_area_zero_side(self):
        """Сторона 0: площадь 0.

        Пример: square.area(0) -> 0
        """
        self.assertEqual(square.area(0), 0)

    def test_area_fractional_side(self):
        """Дробная сторона 2.5: площадь 6.25.

        Пример: square.area(2.5) -> 6.25
        """
        self.assertAlmostEqual(square.area(2.5), 6.25)

    def test_area_big_side(self):
        """Большая сторона 1000: площадь 1 000 000.

        Пример: square.area(1000) -> 1000000
        """
        self.assertEqual(square.area(1000), 1000000)


class SquarePerimeterTestCase(unittest.TestCase):
    """Тесты функции square.perimeter(a)."""

    def test_perimeter_integer_side(self):
        """Сторона 5: периметр 20.

        Пример: square.perimeter(5) -> 20
        """
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_zero_side(self):
        """Сторона 0: периметр 0.

        Пример: square.perimeter(0) -> 0
        """
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_fractional_side(self):
        """Дробная сторона 2.5: периметр 10.

        Пример: square.perimeter(2.5) -> 10.0
        """
        self.assertAlmostEqual(square.perimeter(2.5), 10)

    def test_perimeter_big_side(self):
        """Большая сторона 10**6: периметр 4 * 10**6.

        Пример: square.perimeter(1000000) -> 4000000
        """
        self.assertEqual(square.perimeter(10 ** 6), 4 * 10 ** 6)

    def test_perimeter_unit_side(self):
        """Сторона 1: периметр 4.

        Пример: square.perimeter(1) -> 4
        """
        self.assertEqual(square.perimeter(1), 4)


if __name__ == '__main__':
    unittest.main()
