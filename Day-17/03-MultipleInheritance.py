class Bank():

    def __init__(self, age, sal, occupation):
        self.bankName = "ICICI"
        self.age = age
        self.sal = sal
        self.occupation = occupation

    def bankDetails(self):
        print("Bank Details :", self.bankName)

    def checkEligibility(self):

        if self.sal > 25000 and self.age > 24:
            print("Loan Available")
        elif self.occupation == 'Student':
            print("Education Loan will be provided")
        else:
            print("Loan Not Available")

class Person():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def showPerson(self):
        print("Person Details")
        print("Name :",self.name)
        print("Age :",self.age)

# Multiple Inheritance
class Customer(Person,Bank):

    def __init__(self,name,age,occupation,sal=0):
        Person.__init__(self,name,age)
        Bank.__init__(self,age,sal,occupation)

cust_1 = Customer('Ram',26,'Emp',28000)
cust_1.bankDetails()
cust_1.showPerson()
cust_1.checkEligibility()

cust_2 = Customer('Shyam',17,'Student')
cust_2.bankDetails()
cust_2.showPerson()
cust_2.checkEligibility()

cust_3 = Customer('Mohan',27,'Emp',20000)
cust_3.bankDetails()
cust_3.showPerson()
cust_3.checkEligibility()