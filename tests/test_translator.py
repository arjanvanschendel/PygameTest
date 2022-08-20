import sys
sys.path.append("..")

import unittest
from src.translator import coordsToName, nameToCoords

class TestStringMethods(unittest.TestCase):

    def test_nameToCoords(self):
        self.assertEqual(nameToCoords('a1'), '0,7')
        self.assertEqual(nameToCoords('h8'), '7,0')
        self.assertEqual(nameToCoords('e4'), '4,4')
        self.assertEqual(nameToCoords('d4'), '3,4')
        self.assertEqual(nameToCoords('g7'), '6,1')
        
    def test_coordsToName(self):
        self.assertEqual(coordsToName('(0,7)'), 'a1')
        self.assertEqual(coordsToName('(7,0)'), 'h8')
        self.assertEqual(coordsToName('(4,4)'), 'e4')
        self.assertEqual(coordsToName('(3,4)'), 'd4')
        self.assertEqual(coordsToName('(6,1)'), 'g7')

if __name__ == '__main__':
    unittest.main()