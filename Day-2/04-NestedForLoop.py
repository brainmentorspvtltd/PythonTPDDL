import time

# Nested For Loop

start = time.time()

for i in range(1,1000):
    for j in range(1,100):
        #print("Value of i is {} and j is {}".format(i,j))
        pass

end = time.time()
result = end - start
print("Total Time taken",result)

#for i in range(1,10):
    #pass
