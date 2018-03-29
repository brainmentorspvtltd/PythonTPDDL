file = open('demo_1.txt','w')

data = ["This file is written by using python",
        "This is another data"
        ]

# file.write(data)

for w in data:
    file.write(w+"\n")

file.close()