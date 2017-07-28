import stormtrooper.stormtrooper as stormtrooper
import unittest


class KnowValues(unittest.TestCase):
    known_coordinates = ((2.4, [2, 4]),
                         (42.91, [42, 91]),
                         (-22.456, [-22, 456]))

    def test_split_into_int(self):
        """split_into_integer should give known result with known input"""
        for coordinate, intergers in self.known_coordinates:
            result = stormtrooper.split_into_integers(coordinate)
            self.assertEqual(intergers, result)
