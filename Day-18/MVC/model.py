class Emp():

    def __init__(self,id,name,company,salary):
        self.id = id
        self.name = name
        self.company = company
        self.salary = salary

    def __str__(self):
        return str(self.id) + " " + self.name + " " + self.company + " " + str(self.salary)

empList = []

def addEmp(id,name,company,salary):
    obj = Emp(id,name,company,salary)
    empList.append(obj)
    # print("Object",obj)
    # print("Emplist",empList)
    return empList