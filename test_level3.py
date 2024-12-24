import unittest
import os
from io import StringIO
import sys
from Level3.Q1 import get_even_length_strings
from Level3.Q2 import count_lines
from Level3.Q3 import JtoI
from Level3.Q4 import Shape, Square
from Level3.Q5 import Time
from Level3.Q6 import Animal, Dog, Cat, Bird, Parrot
from Level3.Q7 import create_student_dict
from Level3.Q8 import parse_encoded_string
from Level3.Q9 import run_length_encode
from Level3.Q10 import count_unserviced_customers

class TestLevel3(unittest.TestCase):
    
    def setUp(self):
        with open('doc.txt', 'w') as f:
            f.write('Hello I am a file\n')
        
        with open('demo.txt', 'w') as f:
            f.write('Line 1\nLine 2\nLine 3\n')
            
        with open('WORDS.TXT', 'w') as f:
            f.write('THJS JS A NOTEBOOK')
    
    def tearDown(self):
        files = ['doc.txt', 'demo.txt', 'WORDS.TXT']
        for file in files:
            if os.path.exists(file):
                os.remove(file)
    
    def test_Q1(self):
        result = get_even_length_strings('doc.txt')
        self.assertEqual(result, ['am', 'file'])
    
    def test_Q2(self):
        self.assertEqual(count_lines('demo.txt'), 3)
    
    def test_Q3(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        JtoI()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), 'THIS IS A NOTEBOOK')

    def test_Q4(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)
        
        shape = Shape()
        self.assertEqual(shape.area(), 0)
    
    def test_Q5(self):
        t1 = Time(2, 50)
        t2 = Time(1, 20)
        result = t1.addTime(t2)
        self.assertEqual(result.displayTime(), "4 hr and 10 min")
        
        t3 = Time(1, 2)
        self.assertEqual(t3.displayMinute(), 62)
    
    def test_Q6(self):
        dog = Dog("Perro")
        cat = Cat("Gato")
        parrot = Parrot("Rio")
        
        self.assertEqual(dog.speak(), f"{dog.name} says Woof!")
        self.assertEqual(cat.speak(), f"{cat.name} says Meow!")
        self.assertEqual(parrot.speak(), f"{parrot.name} says Hello!")
        self.assertEqual(parrot.fly(), f"{parrot.name} is Flying!")
    
    def test_Q7(self):
        students = ['Sam', 'Alice', 'Mona']
        subjects = ['Commerce', 'Science', 'Computer']
        expected = {
            'Sam': 'Commerce',
            'Alice': 'Science',
            'Mona': 'Computer'
        }
        self.assertEqual(create_student_dict(students, subjects), expected)
    
    def test_Q8(self):
        encoded = "Robert000Smith000123"
        expected = {
            "first_name": "Robert",
            "last_name": "Smith",
            "id": "123"
        }
        self.assertEqual(parse_encoded_string(encoded), expected)
    
    def test_Q9(self):
        input_str = "wwwwaaadebbbbbw"
        self.assertEqual(run_length_encode(input_str), "w4a3d1e1b5w1")
    
    def test_Q10(self):
        N = 3
        S = "GACCBDDBAGEE"
        self.assertEqual(count_unserviced_customers(N, S), 1)
        
        N = 1
        S = "ABCBAC"
        self.assertEqual(count_unserviced_customers(N, S), 2)

if __name__ == '__main__':
    unittest.main()