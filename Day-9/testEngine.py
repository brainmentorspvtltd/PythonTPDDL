options = [
    ['1989','1990','1995','1986'],
    ['3.9','3.6','3.5','3.7'],
    ['date','time','datetime','datetimelocal'],
    ['ParentException','BaseException','Exception','SuperException'],
    ['exception','except','try','catch'],
    ['break','continue','pass','skip']
]

answers = ['1990','3.6','datetime','BaseException','except','pass']

count = 0

with open('questions.txt','r') as file:
    questions = file.readlines()
    # print(line)
    for i in range(len(questions)):
        print(questions[i])
        for index,j in enumerate(options[i]):
            print("{}. {}".format(index, j))
            # print(options[i][0],"   ", options[j][1])
            # print(options[i][2],"   ", options[j][3])
        print()

        user_ans = int(input("Enter your answer : "))
        if options[i][user_ans] == answers[i]:
            count += 1
            # print("Counter =",count)
        # else:
        #     print("Wrong...")

        print()

print("Total Score",count)

