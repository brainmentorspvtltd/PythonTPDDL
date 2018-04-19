class Emp():

    def __init__(self,id,name,age,company):
        self.id = id
        self.name = name
        self.age = age
        self.company = company

    def showEmp(self):
        print("Emp ID :",self.id)
        print("Emp Name :",self.name)
        print("Emp Age :",self.age)
        print("Emp Company :",self.company)

class Emp_1(Emp):

    def __init__(self,id,name,age,company,sal,dept):
        self.sal = sal
        self.dept = dept
        super().__init__(id,name,age,company)

    # Method Overriding
    def showEmp(self):
        print("Emp Sal :",self.sal)
        print("Emp Dept :",self.dept)

obj = Emp_1(101,'Ram',27,'TCS',24000,'IT')
obj.showEmp()