import sys

sys.path.append("/home/labex/project/")

import unittest
from magic_set import magic_set

class TestMagicSet(unittest.TestCase):
    def test_init(self):
        s = magic_set()
        self.assertIsNotNone(s._data)
        self.assertIsInstance(s, magic_set)
        
if __name__ == '__main__':
    unittest.main()