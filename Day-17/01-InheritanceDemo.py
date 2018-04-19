class Person():

    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def showPerson(self):
        print("Person Details")
        print("Name :",self.name)
        print("Age :",self.age)
        print("Occupation :",self.occupation)

# Single Level Inheritance
# Person is inherited
class Emp(Person):

    def __init__(self,name,age,occupation,company,sal):
        # self.name = name
        # self.age = age
        # self.occupation = occupation
        self.company = company
        self.sal = sal
        super().__init__(name,age,occupation)

    def showEmp(self):
        print("Emp Details :",self.company,self.sal)


class Student(Person):

    def __init__(self,name,age,occupation,school,grade):
        self.school = school
        self.grade = grade
        super().__init__(name,age,occupation)

    def showStudent(self):
        print("Student Details :",self.school, self.grade)

emp_1 = Emp('Ram',29,'Emp','TCS',30000)
emp_1.showPerson()
emp_1.showEmp()

student_1 = Student('Shyam',15,'Student','DPS','11th')
student_1.showPerson()
student_1.showStudent()