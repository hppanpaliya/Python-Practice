def create_student_dict(students, subjects):
    return dict(zip(students, subjects))


if __name__ == '__main__':
    students = ['Sam', 'Alice', 'Mona']
    subjects = ['Commerce', 'Science', 'Computer']
    expected = {
        'Sam': 'Commerce',
        'Alice': 'Science',
        'Mona': 'Computer'
    }
    assert create_student_dict(students, subjects) == expected
