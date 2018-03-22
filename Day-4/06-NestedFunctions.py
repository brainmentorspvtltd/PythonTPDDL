# Nested Functions
# Closures
def outer():
    x = 10
    def inner(i,j):
        print("X is",x+1)
        print("i,j",i,j)
    def inner_2():
        print("X is",x-1)
    # inner()
    # inner_2()
    return inner,inner_2

x,y = outer()
x(12,13)
y()

def logic():
    y()

# logic()