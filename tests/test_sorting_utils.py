# tests/test_sorting_utils.py

import unittest
from utils.sorting_utils import bubble_sort, selection_sort, insertion_sort

class TestSortingUtils(unittest.TestCase):
    
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1]), [1])

    def test_selection_sort(self):
        self.assertEqual(selection_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(selection_sort([]), [])
        self.assertEqual(selection_sort([1]), [1])

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1]), [1])

if __name__ == '__main__':
    unittest.main()
