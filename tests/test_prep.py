import unittest

from prep import number_systems


class NumberSystemsWiki(unittest.TestCase):
    def setUp(self):
        self.nms = number_systems

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


if __name__ == '__main__':
    unittest.main()
