def calculate_grade(physics, chemistry, biology, mathematics, computer):
    total_marks = physics + chemistry + biology + mathematics + computer
    percentage = (total_marks / 500) * 100
    
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 40:
        grade = 'E'
    else:
        grade = 'F'
    
    return percentage, grade

if __name__ == '__main__':
    assert calculate_grade(90, 90, 90, 90, 90) == (90.0, 'A')
    assert calculate_grade(80, 80, 80, 80, 80) == (80.0, 'B')
    assert calculate_grade(70, 70, 70, 70, 70) == (70.0, 'C')
    assert calculate_grade(60, 60, 60, 60, 60) == (60.0, 'D')
    assert calculate_grade(40, 40, 40, 40, 40) == (40.0, 'E')
    assert calculate_grade(30, 30, 30, 30, 30) == (30.0, 'F')