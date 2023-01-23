class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname =surname

    def show(self):
        print(f'{self.name} - {self.surname}')

class student(Person):
    def __init__(self, name, surname, gpa, faculty):
        super().__init__(name, surname)
        self.gpa = gpa
        self.faculty = faculty

    def show(self):
        super().show()
        print(f'{self.gpa} - {self.faculty}')

a = student('Aaa', 'Bbb', 3.9, 'FIT')
a.show()