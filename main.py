class Student:
    number_of_students = 0
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
        Student.number_of_students += 1
    def show(self):
        print(f"I am {self.name}, I am {self.age} years old, and I'm on a {self.gpa} gpa")

    def get_department(self):
        print("None Specified")


class ScienceStudent(Student):
    def __init__(self,name,age,grade,course):
        super().__init__(name,age,grade)
        self.course = course
    def get_department(self):
        print ("Science Department")

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old, and I'm on a {self.gpa} gpa, and I want to study {self.course}")
class ArtStudent(Student):
    def get_department(self):
        print ("art Department")

class CommercialStudent(Student):
    def get_department(self):
        print("commmercial Department")



sc = ScienceStudent("Bola", 16, 5.0, "Medicine")
a = ArtStudent("Adeboye", 21, 4.98)
a2 = ArtStudent("JOshua", 23, 3.55)
c = CommercialStudent("Marvingrace", 27, 4.77)
print (Student.number_of_students)

