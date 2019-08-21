import unittest

from decorator_pattern.beverages import Espresso, HouseBlend, Size
from decorator_pattern.condiments import Mocha, Milk
from decorator_pattern.exceptions import SizeNotDefineError


class TestStarbuzz(unittest.TestCase):
    def setUp(self) -> None:
        self.espresso = Espresso()
        self.house_blend = HouseBlend()

    def test_espresso_size_not_set_error(self):
        with self.assertRaises(SizeNotDefineError):
            self.espresso.cost()

    def test_venti_espresso_cost(self):
        self.espresso.set_size(Size.VENTI)
        self.assertEqual(self.espresso.cost(), self.espresso.coffee_cost + Size.VENTI.value)

    def test_venti_espresso_with_milk_cost(self):
        self.espresso.set_size(Size.VENTI)
        with_milk = Milk(self.espresso)
        self.assertEqual(with_milk.cost(), self.espresso.coffee_cost + Size.VENTI.value + with_milk.condiment_cost)

    def test_espress_with_milk_description(self):
        with_milk = Milk(self.espresso)
        self.assertEqual(with_milk.get_description(), 'Espresso, Milk')

    def test_house_blend_size_not_set_error(self):
        with self.assertRaises(SizeNotDefineError):
            self.house_blend.cost()

    def test_house_blend_grande_espresso_cost(self):
        self.house_blend.set_size(Size.GRANDE)
        self.assertEqual(self.house_blend.cost(), self.house_blend.coffee_cost + Size.GRANDE.value)

    def test_house_blend_grande_espresso_with_mocha_cost(self):
        self.house_blend.set_size(Size.GRANDE)
        with_mocha = Mocha(self.house_blend)
        self.assertEqual(with_mocha.cost(), self.house_blend.coffee_cost + Size.GRANDE.value + with_mocha.condiment_cost)


if __name__ == '__main__':
    unittest.main()
