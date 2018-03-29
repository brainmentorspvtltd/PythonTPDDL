def parent(x):
    print("Parent function")
    x()

def child():
    print("Child function")

parent(child)