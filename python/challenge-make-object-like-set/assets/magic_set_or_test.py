import sys

sys.path.append("/home/labex/project/")

import unittest
from magic_set import magic_set

class TestMagicSet(unittest.TestCase):
    def test_or(self):
        s1 = magic_set()
        s1.add(1)
        s1.add(2)
        s1.add(3)

        s2 = magic_set()
        s2.add(3)
        s2.add(4)
        s2.add(5)

        s3 = s1 | s2
        self.assertEqual(len(s3), 5)
        self.assertTrue(1 in s3)
        self.assertTrue(2 in s3)
        self.assertTrue(3 in s3)
        self.assertTrue(4 in s3)
        self.assertTrue(5 in s3)

if __name__ == '__main__':
    unittest.main()