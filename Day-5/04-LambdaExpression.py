# Map - Returning Logic
# Filter - Returning Conditions
# Lambda Expression - Anonymous Functions

# def add(x,y):
#     return x + y

add = lambda x,y : x + y
print(add(2,3))

# t = lambda c : 9 / 5 * c + 32

# Temp Conv
f = list(map(lambda c : 9 / 5 * c + 32, [33.4,32.1,35.6,37.2,31.2]))
print(f)

# Even numbers
e = list(filter(lambda num : num % 2 == 0, [i for i in range(1,101)]))
print(e)