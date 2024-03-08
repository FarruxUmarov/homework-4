class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

class Course(Student):
    def __init__(self, name, age, course_name, course_teacher) -> None:
        super().__init__(name, age)
        self.name = course_name
        self.teacher = course_teacher
        self.students = []

    def add(self, new_student):
        self.students.append(new_student)
    
    def delete(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print("Xatolik!!!")

    def info_course(self):
        print(f"""
            Course name: {self.name}
            Course teacher: {self.teacher}
            """)
        for student in self.students:
            print(f"""
            Name: {student.name},
            Age: {student.age}""")

st1 = Student("Alijon", 18)
st2 = Student("Bobur", 22)
st3 = Student("Akrom", 19)
st4 = Student("SHoxrux", 28)
st5 = Student("Sanjar", 25)

course = Course("Aziz", "Jorayev", "dasturlash", "Anvar")
course.add(st1)
course.add(st2)
course.add(st3)
course.add(st4)
course.add(st5)

course.info_course()

course.delete(st1)

course.info_course()

