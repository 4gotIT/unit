import unittest
from utils.arrs import get, my_slice


class TestArr(unittest.TestCase):
    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(my_slice([1, 2, 3]),  [1, 2, 3])
        self.assertEqual(my_slice([]), [])


if __name__ == '__main__':
    unittest.main()