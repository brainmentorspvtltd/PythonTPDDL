# Using Map()

def temp_conv(c):
    return 9 / 5 * c + 32

cel = [33.4,32.1,35.6,37.2,31.2]

# f = []
#
# for temp in cel:
#     print(temp_conv(temp))
#     f.append(temp_conv(temp))

f = list(map(temp_conv, cel))
print(f)