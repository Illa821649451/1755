class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects

    def attend_lesson(self, teacher):
        teacher.teach_lesson(self)


class Teacher:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects

    def teach_lesson(self, student):
        print(f"Викладач {self.name} проводить урок для студента {student.name}")

        student1 = Student("Іван", 20, ["Математика", "Фізика"])
        student2 = Student("Олена", 19, ["Хімія", "Біологія"])

        teacher = Teacher("Петро", 35, ["Математика", "Фізика", "Хімія", "Біологія"])

        student1.attend_lesson(teacher)
        student2.attend_lesson(teacher)
