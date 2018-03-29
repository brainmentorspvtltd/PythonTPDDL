# e = []
# def even(num):
#     # return num % 2 == 0
#     if num % 2 == 0:
#         e.append(num)
#
#     return num

def even(num):
    return num % 2 == 0

numbers = [i for i in range(1,101)]

# for num in numbers:
#     even(num)

e = list(filter(even, numbers))
print(e)