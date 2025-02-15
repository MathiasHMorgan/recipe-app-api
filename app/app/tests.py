"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test calc Mod"""

    def test_add_numbers(self):
        """Test numbers add"""

        res = calc.add(3, 9)
        self.assertEqual(res, 12)

    def test_subtract_numbers(self):
        """Test numbers subtract"""

        res = calc.subtract(9, 3)
        self.assertEqual(res, 6)

