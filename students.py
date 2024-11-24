from presence import Presence

class Students:
    students = []

    def __init__(self, name: str, surname: str, presence: Presence):
        self.name = name
        self.surname = surname
        self.presence = presence

    def add_student(self):
        student_data = {
            'name': self.name,
            'surname': self.surname,
            'presence': self.presence
        }
        Students.students.append(student_data)

    def edit_presence(self, new_presence: Presence):
        for student_data in Students.students:
            if student_data['name'] == self.name and student_data['surname'] == self.surname:
                if student_data['presence'] != new_presence:
                    student_data['presence'] = new_presence
                    break
                else:
                    raise(Exception)

    def export_to_txt(path:str):
        with open(path, 'w') as f:
            for student in Students.students:
                f.write(f'{student['name']},{student['surname']},{student['presence']}\n')

    def import_from_txt(path:str):

        with open(path, 'r') as file:

            for line in file.readlines():
                data = line.split(',')
                
                name = data[0]
                surname = data[1]
                presence = getattr(Presence, data[2].split('.')[1].strip())

                Students.students.append({
                    'name': name,
                    'surname': surname,
                    'presence': presence
                })