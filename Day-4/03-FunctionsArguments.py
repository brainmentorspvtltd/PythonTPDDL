##x = 10
##y = 5

def add(x=0,y=0):
    z = x + y
    print("Sum is",z)

def sub(x=0,y=0):
    #z = x - y
    z = x - y if x > y else y - x
    print("Diff is",z)

add(y=12)
sub(x=10,y=2)
