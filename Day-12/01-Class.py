class Person():
    """This is a person class"""
    p_id = 0
    name = ""
    age = 0

# print("Outside Main")

if __name__ == '__main__':
    print("Inside Main")
    # print(Person)
    Person.p_id = 101
    Person.name = "Ram"
    Person.age = 30
    print(Person.p_id, Person.name, Person.age)
    # Will print dictionary of Person Class
    print(Person.__dict__)
    # Will print doc string of Person Class
    print(Person.__doc__)