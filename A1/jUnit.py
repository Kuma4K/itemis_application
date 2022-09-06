import unittest
import utils1


class MyTestCase(unittest.TestCase):
    def test_round(self):
        self.assertEqual(utils1.myRound(0.04), 0.05, "Should be 0.05")
        self.assertEqual(utils1.myRound(16.98), 17.00)
        self.assertEqual(utils1.myRound(23.32), 23.35)

    def test_getStringAttr(self):
        self.assertEqual(utils1.getStringAttr("2 imported items at 13.45"),
                         ('2 imported items', '13.45', True, True))
        self.assertEqual(utils1.getStringAttr("50321 chocolate cookies with topping at 3687.55"),
                         ('50321 chocolate cookies with topping', '3687.55', False, False))

    def test_calc_total(self):
        self.assertEqual(utils1.calc_total(['items', '13.45', False, False]), (13.45, 0.0))
        self.assertEqual(utils1.calc_total(['1 plate', '10', True, False]), (10.5, 0.5))
        self.assertEqual(utils1.calc_total(['1 plate', '10', False, True]), (11, 1.0))
        self.assertEqual(utils1.calc_total(['1 plate', '10', True, True]), (11.5, 1.5))


if __name__ == '__main__':
    unittest.main()
