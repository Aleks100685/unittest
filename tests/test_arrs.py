import unittest
from utils import arrs


class Testarrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 5, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")




    def test_my_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -2), [4, 5])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -3, -1), [3, 4])
        self.assertEqual(arrs.my_slice([], 1, 2, ), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 10, ), [])




if __name__ == '__main__':
    unittest.main()