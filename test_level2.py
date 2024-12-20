import unittest
from Level2.Q1 import find_common_elements
from Level2.Q2 import get_unique_elements
from Level2.Q3 import count_pairs_with_sum
from Level2.Q4 import rotate_array
from Level2.Q5 import analyze_temperature
from Level2.Q6 import is_power_of_two
from Level2.Q7 import find_median
from Level2.Q8 import count_vowels
from Level2.Q9 import access_list_safely
from Level2.Q10 import stone_piles
from Level2.Q11 import string_to_char_list
from Level2.Q12 import create_login_system
from Level2.Q13 import starts_with_char

class TestLevel2(unittest.TestCase):
    
    def test_Q1(self):
        l1 = [1, 2, 3, 4, 5]
        l2 = [4, 5, 6, 7, 8]
        self.assertEqual(find_common_elements(l1, l2), [4, 5])
    
    def test_Q2(self):
        list1 = [1, 2, 2, 3, 4, 4, 5, 5]
        self.assertEqual(get_unique_elements(list1), [1, 2, 3, 4, 5])
    
    def test_Q3(self):
        arr = [1, 2, 3, 4, 5]
        k = 6
        self.assertEqual(count_pairs_with_sum(arr, k), 2)
    
    def test_Q4(self):
        arr = [1, 2, 3, 4, 5]
        D = 2
        self.assertEqual(rotate_array(arr, D), [4, 5, 1, 2, 3])
    
    def test_Q5(self):
        temperature_readings = [25, 28, 21, 24, 27]
        expected = {
            'Average Temperature': 25.0,
            'Highest Temperature': 28,
            'Lowest Temperature': 21
        }
        self.assertEqual(analyze_temperature(temperature_readings), expected)

    def test_Q6(self):
        power_of_two = 16
        not_power_of_two = 15
        self.assertTrue(is_power_of_two(power_of_two))
        self.assertFalse(is_power_of_two(not_power_of_two))
    
    def test_Q7(self):
        number_list = [7, 2, 5, 1, 9, 3]
        self.assertEqual(find_median(number_list), 4.0)
    
    def test_Q8(self):
        string = "Hello, World!"
        self.assertEqual(count_vowels(string), 3)
    
    def test_Q9(self):
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(access_list_safely(test_list, 1), 2)
        self.assertTrue(isinstance(access_list_safely(test_list, 10), str)) # String returned as error message
    
    def test_Q10(self):
        n = 3
        self.assertEqual(stone_piles(n), [3, 5, 7])
    
    def test_Q11(self):
        input_list = ['Red', 'Blue', 'Black', 'White', 'Pink']
        expected = [
            ['R', 'e', 'd'],
            ['B', 'l', 'u', 'e'],
            ['B', 'l', 'a', 'c', 'k'],
            ['W', 'h', 'i', 't', 'e'],
            ['P', 'i', 'n', 'k']
        ]
        self.assertEqual(string_to_char_list(input_list), expected)

    def test_Q13(self):
        input_string = "Hello, World!"
        given_char = "H"
        self.assertTrue(starts_with_char(input_string, given_char))
        self.assertFalse(starts_with_char(input_string, "h"))

if __name__ == '__main__':
    unittest.main()