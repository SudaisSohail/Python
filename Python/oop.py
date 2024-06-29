class Student:

    School = "St.Paul's English High School"
    
    def __init__(self, name, age, grade):

        self.name, self.age, self.grade = name, age, grade

    def get_grade(self):
        return self.grade

    def get_name(self):  # This method also exists in child class. If child class do not have this method, this method will be called.

        return self.name

    def __add__(self, other): # Over loading "+" operator   --> OPERATOR OVERLOADING

        return self.grade + other.grade

    def __str__(self):                      # Over loading "str" method  --> METHOD OVERLOADING

        return f"{self.name} {self.age} {self.grade}"


class Course(Student):                      # Course class is inheriting from student class

    def __init__(self, name, max_students):

        self.name, self.max_students, self.students = name, max_students, []

    def add_students(self, student):

        if len(self.students) < self.max_students:

            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):

        value = 0

        for student in self.students:
            value += student.get_grade()

        return value / len(self.students) 

    def get_name(self):     # This method also exists in super class  --> METHOD OVERRIDING 

        return self.name
    
    def __str__(self):      # Over loading "str" method  --> METHOD OVERLOADING

        return f"{self.name} {self.max_students}" 



s1 = Student("Sudais", 15, 90)
s2 = Student("Umair", 15, 65)
s3 = Student("Usman", 15, 85)
course = Course("Machine Learning", 50)

print(course.get_name())
print(getattr(s1, "name"))
print(s1.name)

