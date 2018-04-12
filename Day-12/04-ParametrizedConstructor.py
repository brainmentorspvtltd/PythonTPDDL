class Person():
    # Parameterized Constructor
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def showPerson(self):
        print("Person Details",self.id,self.name,self.age)

Person.company = 'Tata'

obj = Person(101,'Ram',28)
obj.showPerson()
obj.dept = 'IT'
print("Company -",obj.company)
print("Department",obj.dept)

print(isinstance(obj,Person))
print(type(obj))
print(type(Person))

obj_2 = Person(102,'Shyam',30)
obj_2.showPerson()
print("Company",obj_2.company)