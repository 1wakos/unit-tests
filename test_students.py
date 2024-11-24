import pytest
from students import Students
from presence import Presence
import os

# 3. operacje na studentach

def test_add():

    #Given
    student1 = Students('Julia', 'Ciapala', Presence.absent)
    student2 = Students('Kasia', 'Liczydlo', Presence.present)
    student3 = Students('Ola', 'Nowak', Presence.present)

    #When
    Students.add_student(student1)
    Students.add_student(student2)
    Students.add_student(student3)

    #Then
    assert len(Students.students) == 3

def test_add_error():

    # Given
    student1 = Students('Julia', 'Ciapala', Presence.absent)

    #When
    Students.add_student(student1)

    #Then
    with pytest.raises(AssertionError):
        assert len(Students.students) == 8

# 4. operacje na obecnosci

def test_edit_attendance():

    #Given:
    student1 = Students('Julia', 'Ciapala', Presence.absent)
    
    #When:
    Students.edit_presence(student1, Presence.present)

    #Then:
    assert Students.students[0]['presence'] == Presence.present

def test_edit_attendance_same():
    # jesli chcemy edytowac na ta sama to dostaniemy wyjatek
    
    #Given:
    student1 = Students('Julia', 'Ciapala', Presence.present)
    
     # When & Then
    with pytest.raises(Exception):
        Students.edit_presence(Presence.present)

# 1. zapisywanie do pliku

def test_export_to_txt():
    Students.students.clear()

    student1 = Students('Julia', 'Ciapala', Presence.absent)
    student2 = Students('Kasia', 'Liczydlo', Presence.present)
    student1.add_student()
    student2.add_student()

    # When:
    path = 'students.txt'
    Students.export_to_txt(path)

    # Then:
    assert os.path.exists(path)

    with open(path, 'r') as file:
        lines = file.readlines()

    assert len(lines) == 2
    assert 'Julia' in lines[0] and 'Ciapala' in lines[0] and 'absent' in lines[0]
    assert 'Kasia' in lines[1] and 'Liczydlo' in lines[1] and 'present' in lines[1]

    # os.remove(path)

# 2. wczytywanie z pliku

def test_import_from_txt():
    path = 'students.txt'

    # Given:
    Students.students.clear()

    # When:
    Students.import_from_txt(path)

    # Then:
    assert len(Students.students) == 2
    assert Students.students[0]['name'] == 'Julia'
    assert Students.students[0]['surname'] == 'Ciapala'
    assert Students.students[0]['presence'] == Presence.absent

    assert Students.students[1]['name'] == 'Kasia'
    assert Students.students[1]['surname'] == 'Liczydlo'
    assert Students.students[1]['presence'] == Presence.present
    

    # os.remove(path)