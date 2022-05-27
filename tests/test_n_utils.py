import unittest

import n_utils


class UtilsCase(unittest.TestCase):
    def test_recurring_patterns(self):
        self.assertEqual('4', n_utils.find_recurring_pattern('444444'))
        self.assertEqual('geeksforgeeks', n_utils.find_recurring_pattern('geeksforgeeksgeeksforgeeksgeeksforgeeks'))
        self.assertEqual('124', n_utils.find_recurring_pattern('1232124124124124'))
        self.assertEqual('muremwav', n_utils.find_recurring_pattern('mynameismuremwavmuremwavmuremwavmuremwa'))
        self.assertEqual('3', n_utils.find_recurring_pattern('343333333'))

    def test_assurances_standard_base(self):
        self.assertTrue(n_utils.ensure_base_is_standard(2))
        self.assertTrue(n_utils.ensure_base_is_standard(23))
        self.assertTrue(n_utils.ensure_base_is_standard(64))
        self.assertTrue(n_utils.ensure_base_is_standard(8))
        self.assertTrue(n_utils.ensure_base_is_standard(10))
        self.assertTrue(n_utils.ensure_base_is_standard(16))
        self.assertTrue(n_utils.ensure_base_is_standard(216))
        self.assertTrue(n_utils.ensure_base_is_standard(360))

        self.assertFalse(n_utils.ensure_base_is_standard(259))
        self.assertFalse(n_utils.ensure_base_is_standard(63))
        self.assertFalse(n_utils.ensure_base_is_standard(71))
        self.assertFalse(n_utils.ensure_base_is_standard(101))
        self.assertFalse(n_utils.ensure_base_is_standard(301))
        self.assertFalse(n_utils.ensure_base_is_standard(214))
        self.assertFalse(n_utils.ensure_base_is_standard(359))

    def test_assurances_base_10(self):
        self.assertTrue(n_utils.ensure_no_base_10('100'))
        self.assertTrue(n_utils.ensure_no_base_10('140'))
        self.assertTrue(n_utils.ensure_no_base_10('121.32'))
        self.assertTrue(n_utils.ensure_no_base_10('0.13'))
        self.assertTrue(n_utils.ensure_no_base_10('0'))
        self.assertTrue(n_utils.ensure_no_base_10('0.0'))

        self.assertFalse(n_utils.ensure_no_base_10('S232.2e'))
        self.assertFalse(n_utils.ensure_no_base_10('as'))
        self.assertFalse(n_utils.ensure_no_base_10('A3'))
        self.assertFalse(n_utils.ensure_no_base_10('0.34sdD'))
        self.assertFalse(n_utils.ensure_no_base_10('dsd'))
        self.assertFalse(n_utils.ensure_no_base_10('A.0'))

    def test_number_representable(self):
        self.assertTrue(n_utils.ensure_number_is_representable('121dfË'))
        self.assertTrue(n_utils.ensure_number_is_representable('12Ʒd.fË'))
        self.assertTrue(n_utils.ensure_number_is_representable('12ƷdfË'))
        self.assertTrue(n_utils.ensure_number_is_representable('1.Ǧ'))
        self.assertTrue(n_utils.ensure_number_is_representable('1Ǧ'))
        self.assertTrue(n_utils.ensure_number_is_representable('Ë'))
        self.assertTrue(n_utils.ensure_number_is_representable('0'))
        self.assertTrue(n_utils.ensure_number_is_representable('0.0'))

        self.assertFalse(n_utils.ensure_number_is_representable('Ўew'))
        self.assertFalse(n_utils.ensure_number_is_representable('12.2߷'))
        self.assertFalse(n_utils.ensure_number_is_representable('12߷'))
        self.assertFalse(n_utils.ensure_number_is_representable('ߘsdk2'))
        self.assertFalse(n_utils.ensure_number_is_representable('ߝiwd.23'))
        self.assertFalse(n_utils.ensure_number_is_representable('1ߔ'))
        self.assertFalse(n_utils.ensure_number_is_representable('asߒ3'))

    def test_base_limits(self):
        self.assertTrue(n_utils.base_limits('AE', 16))
        self.assertTrue(n_utils.base_limits('AG', 30))
        self.assertTrue(n_utils.base_limits('AB', 12))
        self.assertTrue(n_utils.base_limits('10', 10))

        self.assertFalse(n_utils.base_limits('G4', 16))
        self.assertFalse(n_utils.base_limits('G4', 10))
        self.assertFalse(n_utils.base_limits('02', 2))
        self.assertFalse(n_utils.base_limits('9', 8))


if __name__ == '__main__':
    unittest.main()
