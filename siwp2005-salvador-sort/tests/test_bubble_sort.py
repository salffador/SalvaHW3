import unittest
from sort.bubble_sort import BubbleSort  

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        arr = [4, 3, 2, 1]
        sorter = BubbleSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4])

    def test_bubble_sort_with_duplicates(self):
        arr = [3, 3, 2, 1]
        sorter = BubbleSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 3])

    def test_bubble_sort_already_sorted(self):
        arr = [1, 2, 3, 4]
        sorter = BubbleSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4])

    def test_bubble_sort_single_element(self):
        arr = [1]
        sorter = BubbleSort(arr)
        self.assertEqual(sorter.sort(), [1])

    def test_bubble_sort_empty(self):
        arr = []
        sorter = BubbleSort(arr)
        self.assertEqual(sorter.sort(), [])

if __name__ == '__main__':
    unittest.main()
