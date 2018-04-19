# ToString
# To convert object to readable format

class Emp():

    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.id) + " " + self.name + " " + str(self.age)

obj = Emp(101,'Ram',29)
print(obj)