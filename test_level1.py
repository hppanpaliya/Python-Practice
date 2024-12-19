import unittest
from Beginner.Q1 import check_number
from Beginner.Q2 import count_digits_letters
from Beginner.Q3 import calculate_grade
from Beginner.Q4 import sum_odd_numbers
from Beginner.Q5 import factorial
from Beginner.Q6 import is_perfect_number
from Beginner.Q7 import is_anagram
from Beginner.Q8 import calculate_lcm
from Beginner.Q9 import count_frequency
from Beginner.Q10 import reverse_words
from Beginner.Q11 import single_digit_sum
from Beginner.Q12 import reverse_number

class TestLevel1(unittest.TestCase):
    
    def test_Q1(self):
        self.assertEqual(check_number(3), "Consultadd")
        self.assertEqual(check_number(5), "Python Training")
        self.assertEqual(check_number(15), "Consultadd - Python Training")
    
    def test_Q2(self):
        self.assertEqual(count_digits_letters("Hello123"), "Alphabets: 5 & Number: 3")
        self.assertEqual(count_digits_letters("Hello"), "Alphabets: 5 & Number: 0")
        self.assertEqual(count_digits_letters("123"), "Alphabets: 0 & Number: 3")
    
    def test_Q3(self):
        percentage, grade = calculate_grade(90, 90, 90, 90, 90)  
        self.assertEqual(grade, 'A')
        
        percentage, grade = calculate_grade(80, 80, 80, 80, 80) 
        self.assertEqual(grade, 'B')
        
        percentage, grade = calculate_grade(70, 70, 70, 70, 70) 
        self.assertEqual(grade, 'C')
        
        percentage, grade = calculate_grade(60, 60, 60, 60, 60) 
        self.assertEqual(grade, 'D')
        
        percentage, grade = calculate_grade(40, 40, 40, 40, 40)  
        self.assertEqual(grade, 'E')
        
        percentage, grade = calculate_grade(30, 30, 30, 30, 30)  
        self.assertEqual(grade, 'F')
    
    def test_Q4(self):
        self.assertEqual(sum_odd_numbers(1, 10), 25)  
        self.assertEqual(sum_odd_numbers(1, 5), 9)
        

    def test_Q5(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
    
    def test_Q6(self):
        self.assertEqual(is_perfect_number(5), False)
        self.assertEqual(is_perfect_number(6), True)
    
    def test_Q7(self):
        self.assertEqual(is_anagram("listen", "silent"), True)
    
    def test_Q8(self):
        self.assertEqual(calculate_lcm(12, 18), 36)
    
    def test_Q9(self):
        input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
        expected = {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
        self.assertEqual(count_frequency(input_list), expected)
    
    def test_Q10(self):
        input_sentence = "Hello, World! Welcome to Python programming."
        expected = "programming. Python to Welcome World! Hello,"
        self.assertEqual(reverse_words(input_sentence), expected)
    
    def test_Q11(self):
        self.assertEqual(single_digit_sum(987), 6)  
    
    def test_Q12(self):
        self.assertEqual(reverse_number(12345), 54321)

if __name__ == '__main__':
    unittest.main()