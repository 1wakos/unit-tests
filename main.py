from students import Students
from presence import Presence

def print_student_list():
    for x in Students.students:
        print(x)

# student1 = Students("Zuzia", "Wilk", Presence.present())
# student2 = Students("Kinga", "Olczynska", Presence.absent())
# student3 = Students("Oliwier", "Nowak", Presence.present())

# adding

# Students.add_student(student1)
# Students.add_student(student2)
# Students.add_student(student3)

# exporting

# Students.export_to_txt()
# student4 = Students("Ola", "Pieczarka", Presence.absent())
# Students.add_student(student4)
# Students.export_to_txt()

# importing

# path = 'plik.txt'
# Students.import_from_txt(path)
# print_student_list()

# editing

# Students.edit_presence(student1, Presence.absent())
# print('-'*50)
# print_student_list()