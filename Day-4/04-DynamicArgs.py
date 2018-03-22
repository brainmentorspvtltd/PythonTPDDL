## Dynamic Arguments
## *args
## **kwargs

def emp(id,name,age,*address):
    print("ID : {}".format(id))
    print("Name : {}".format(name))
    print("Age : {}".format(age))
    #print("Address : {}".format(address))
    for i,addr in enumerate(address):
        print("Address {} : {}".format(i+1,addr))
    

#emp(101,'Ram',28,['NSP','Rohini'])
#emp(101,'Ram',28,'NSP','Rohini','Rithala')

def student(**details):
    print(details)

student(name = 'Ram', age = 14, grade = 'A')
student(name = 'Shyam', age = 13, hobby = 'Cricket,Football')


