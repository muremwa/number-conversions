import unittest

from n_utils import find_recurring_pattern


class UtilsCase(unittest.TestCase):
    def test_recurring_patterns(self):
        self.assertEqual('4', find_recurring_pattern('444444'))
        self.assertEqual('geeksforgeeks', find_recurring_pattern('geeksforgeeksgeeksforgeeksgeeksforgeeks'))
        self.assertEqual('124', find_recurring_pattern('1232124124124124'))
        self.assertEqual('muremwav', find_recurring_pattern('mynameismuremwavmuremwavmuremwavmuremwa'))
        self.assertEqual('3', find_recurring_pattern('343333333'))


if __name__ == '__main__':
    unittest.main()
