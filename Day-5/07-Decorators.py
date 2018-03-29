# Decorators

def parent(x):
    print("Parent function")
    if True:
        return x()

@parent
def child():
    print("Child function")

@parent
def child_1():
    print("Child_1 function")