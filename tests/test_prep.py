import unittest

from prep import number_systems, number_codes


class NumberSystemsWiki(unittest.TestCase):
    def setUp(self):
        self.nms = number_systems
        self.nmc = number_codes

    def test_number_systems_82(self):
        # get back 82 number systems
        self.assertEqual(len(self.nms), 82)

    def test_number_systems_dict_convection(self):
        for nm in self.nms:
            # keys are the defined ones
            self.assertListEqual(['base', 'system', 'system_name'], list(nm.keys()))
            # all values are strings
            self.assertEqual(
                True,
                all(type(value) == str for value in nm.values())
            )

    def test_number_codes_length(self):
        # get 360 codes
        self.assertEqual(len(self.nmc), 360)

    def test_number_codes_work(self):
        chr_s = list(filter(lambda c_: bool(c_), [chr(c) for c in self.nmc]))
        self.assertEqual(len(chr_s), 360)


if __name__ == '__main__':
    unittest.main()
