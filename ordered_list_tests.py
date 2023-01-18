# Ordered List Tests [Data Structures]
# Joshua Estrada

import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):
    def test_standard(self):
        t_list = OrderedList()
        t_list.add(10)  # 10
        self.assertEqual(t_list.python_list(), [10])  # 10 is [10]
        self.assertEqual(t_list.size(), 1)  # one item in list
        self.assertEqual(t_list.index(10), 0)  # 10 is at idx 0
        self.assertTrue(t_list.search(10))  # there is a 10
        self.assertFalse(t_list.is_empty()) # list is not empty
        self.assertEqual(t_list.python_list_reversed(), [10])  # 10 reversed is [10]
        self.assertTrue(t_list.remove(10))  # remove 10
        t_list.add(10)  # add 10
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.pop(0), 10)

    def test_is_empty(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertFalse(t_list.is_empty())
        t_list.add(20)
        self.assertFalse(t_list.is_empty())
        t_list.remove(10)
        t_list.pop(0)
        self.assertTrue(t_list.is_empty())

    def test_add_1(self):
        t_list = OrderedList()
        t_list.add(1)  # add 1
        t_list.add(3)  # add 3
        t_list.add(2)  # add 2
        self.assertEqual(t_list.index(2), 1)  # 1 2 3  # idx0 idx1 idx2
        t_list.remove(2)  # 1 2 3  ->  # 1 3
        self.assertEqual(t_list.index(1), 0)  # 1 3  -> 1 is at index 0
        self.assertEqual(t_list.index(3), 1)  # 1 3  -> 3 is at index 1
        # add and index now functional
        t_list.remove(1)  # remove 1
        self.assertEqual(t_list.index(1), None)  # there is no 1 return None
        self.assertTrue(t_list.remove(3))   # remove 3
        self.assertFalse(t_list.remove(3))  # there is no 3 to remove
        self.assertTrue(t_list.is_empty())  # no nodes, "list" is empty

    def test_add_2(self):
        t_list = OrderedList()
        t_list.add(10)  # 10
        t_list.add(20)  # 10 20
        t_list.add(30)  # 10 20 30
        t_list.add(15)  # 10 15 20 30
        self.assertEqual(t_list.index(15), 1)
        t_list.remove(30)  # remove from end
        t_list.remove(10)  # remove from beginning
        t_list.add(17)
        t_list.remove(17)  # remove from middle

    def test_add_3(self):
        t_list = OrderedList()
        self.assertTrue(t_list.add(31))  # add 31
        self.assertFalse(t_list.add(31))  # shouldn't add duplicate

    def test_remove(self):
        t_list = OrderedList()
        self.assertFalse(t_list.remove(10))
        t_list.add(10)
        self.assertTrue(t_list.remove(10))
        self.assertFalse(t_list.remove(10))
        t_list.add(10)
        t_list.add(15)
        self.assertTrue(t_list.remove(10))
        self.assertTrue(t_list.remove(15))
        t_list.add(4.54)
        t_list.add(3.14)
        t_list.add(4.35)
        self.assertTrue(t_list.remove(4.35))

    def test_index(self):
        t_list = OrderedList()
        self.assertEqual(t_list.index(21), None)
        t_list.add(21)
        self.assertEqual(t_list.index(21), 0)  # 21 at idx 0
        t_list.add(21)
        t_list.add(41)
        self.assertEqual(t_list.index(41), 1)

    def test_pop(self):
        t_list = OrderedList()
        self.assertRaises(IndexError, t_list.pop, -1)
        t_list.add(0)
        self.assertEqual(t_list.pop(0), 0)
        self.assertRaises(IndexError, t_list.pop, 1)
        t_list.add(5)
        t_list.add(11)
        self.assertEqual(t_list.pop(1), 11)
        self.assertEqual(t_list.pop(0), 5)

    def test_search(self):
        t_list = OrderedList()
        self.assertFalse(t_list.search(31))
        t_list.add(31)
        self.assertTrue(t_list.search(31))
        t_list.add(41)
        self.assertTrue(t_list.search(41))

    def test_python_list(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list(), [])
        t_list.add(31)
        t_list.add(5)
        t_list.add(11)
        self.assertEqual(t_list.python_list(), [5, 11, 31])
        t_list.remove(11)
        self.assertEqual(t_list.python_list(), [5, 31])

    def test_python_reversed_list(self):
        t_list = OrderedList()
        t_list.add(31)
        t_list.add(5)
        t_list.add(11)
        self.assertEqual(t_list.python_list_reversed(), [31, 11, 5])
        t_list.remove(11)
        self.assertEqual(t_list.python_list_reversed(), [31, 5])

    def test_size(self):
        t_list = OrderedList()
        self.assertEqual(t_list.size(), 0)
        t_list.add(1)
        self.assertEqual(t_list.size(), 1)
        t_list.add(2)
        t_list.add(3)
        t_list.add(4)
        t_list.add(5)
        self.assertEqual(t_list.size(), 5)
        t_list.remove(5)
        self.assertEqual(t_list.size(), 4)
        t_list.add(4)
        self.assertEqual(t_list.size(), 4)

    def test_string(self):
        t_list = OrderedList()
        t_list.add("a")
        t_list.add("A")
        self.assertEqual(t_list.index("a"), 1)
        self.assertEqual(t_list.index("A"), 0)

    def test_string_word(self):
        t_list = OrderedList()
        t_list.add("Joshua")
        t_list.add("Melissa")
        t_list.add("Aaron")
        t_list.add("Kato")
        t_list.add("Tina")
        self.assertEqual(t_list.index("Aaron"), 0)
        self.assertEqual(t_list.index("Joshua"), 1)
        self.assertEqual(t_list.index("Melissa"), 3)
        self.assertEqual(t_list.index("Kato"), 2)
        self.assertEqual(t_list.index("Tina"), 4)
        self.assertFalse(t_list.search("Pedro"))
        t_list.add("Pedro")
        self.assertEqual(t_list.index("Pedro"), 4)
        t_list.add("Jesus")
        self.assertTrue(t_list.search("Jesus"))


if __name__ == '__main__': 
    unittest.main()
