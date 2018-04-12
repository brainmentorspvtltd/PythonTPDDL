class Person():
    p_id = 0
    name = ""
    age = 0

    # self = this
    # this -> refers to current object
    def show(self):
        print(self.p_id,self.name,self.age)

obj_1 = Person()
obj_1.p_id = 101
obj_1.name = 'Ram'
obj_1.age = 29
# print(obj_1)
# obj_1.show()
obj_1.show(obj_1)


obj_2 = Person()
obj_2.p_id = 102
obj_2.name = "Shyam"
obj_2.age = 30
obj_2.show()