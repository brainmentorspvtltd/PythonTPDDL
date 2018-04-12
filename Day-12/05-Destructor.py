class Person():
    # Parameterized Constructor
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def showPerson(self):
        print("Person Details",self.id,self.name,self.age)

    def __del__(self):
        print("Object Destroyed...")

Person.company = 'Tata'

obj = Person(101,'Ram',28)
obj.showPerson()
obj.dept = 'IT'
print("Company -",obj.company)
print("Department",obj.dept)

# del obj
obj = None

obj_2 = Person(102,'Shyam',30)
obj_2.showPerson()
print("Company",obj_2.company)

# print("Object of {} is deleted".format(obj.name))