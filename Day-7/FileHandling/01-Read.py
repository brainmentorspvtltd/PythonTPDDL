file = open('demo.txt')

# data = file.read()
#data = file.read()

# data = file.readline()
# data = file.readlines()
# print(len(data))
# for i in range(3):
#     line = file.readline()
#     print(line,  end="")

# print(data)


file.seek(5)

data = file.read()
print(data)

file.close()