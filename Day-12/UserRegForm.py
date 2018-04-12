class User():
    # Bydefault - Public
    # _ = Protected Variable
    # __ = Private Variable
    __userdata = []
    # data = {}

    def __init__(self):
        # self.userdata = []
        self.data = {}

    def user_input(self):
        username = input("Enter your name : ")
        usermail = input("Enter your mail : ")
        userpwd = input("Enter your password : ")

        self.data['name'] = username
        self.data['mail'] = usermail
        self.data['pwd'] = userpwd

        self.__userdata.append(self.data)
        self.print_user()

    def print_user(self):
        print(self.__userdata)

for i in range(5):
    obj_1 = User()
    obj_1.user_input()
