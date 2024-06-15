import unittest
from sort.insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        # Test case 1
        arr1 = [3, 2, 1, 5, 4]
        sorted_arr1 = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(arr1), sorted_arr1)

        # Test case 2
        arr2 = [10, 8, 3, 7, 5, 4, 1, 9, 2, 6]
        sorted_arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(insertion_sort(arr2), sorted_arr2)

        # Test case 3
        arr3 = [5, 5, 5, 5, 5]
        sorted_arr3 = [5, 5, 5, 5, 5]
        self.assertEqual(insertion_sort(arr3), sorted_arr3)

        # Test case 4
        arr4 = [1]
        sorted_arr4 = [1]
        self.assertEqual(insertion_sort(arr4), sorted_arr4)

        # Test case 5
        arr5 = []
        sorted_arr5 = []
        self.assertEqual(insertion_sort(arr5), sorted_arr5)

if __name__ == '__main__':
    unittest.main()
