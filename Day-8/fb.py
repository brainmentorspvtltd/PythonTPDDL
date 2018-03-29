from datetime import datetime
import csv

# time = datetime.now().time()

users = []
userdata = {}

# [
#     {'name':'Ram','email':'ram@gmail','pwd':'1234'},
#     {'name':'Ram','email':'ram@gmail','pwd':'1234'},
# ]


posts = []
postData = {}

def userPost(username):
    print("Hello {}".format(username))
    post = input("Enter your post : ")

    date = datetime.now().date()

    postData['post'] = post
    postData['username'] = username
    postData['date'] = date.isoformat()

    posts.append(postData.copy())

    for p in posts:
        print(p)

    login_success(username)

def viewProfile(username):
    print("Your Profile : ")

    data = list(filter(lambda n : n['name'] == username, users))
    post = list(filter(lambda n : n['username'] == username, posts))
    for d in data:
        print("Name :",d['name'])
        print("Email :",d['mail'])
        for p in post:
            print("Post :",p['post'])
            print("On :",p['date'])

def updateProfile(username):
    to_update = input("What do you want to update: ")
    update_val = input("Enter updated {}".format(to_update))
    to_update = to_update.lower()
    user = list(filter(lambda n : n['name'] == username, users))

    for u in user:
        u[to_update] = update_val

    for user in users:
        print(user)

def deleteProfile(username):
    pass

def logout(*args):
    pass

def login_success(username):

    print("""
    1. Post Something
    2. View Profile
    3. Update Profile
    4. Delete Profile
    5. Logout
    """)

    todo = {
        "1" : userPost,
        "2" : viewProfile,
        "3" : updateProfile,
        "4" : deleteProfile,
        "5" : logout
    }

    user_ch = input("Enter your choice : ")
    todo.get(user_ch)(username)

def login():
    usermail = input("Enter your mailID : ")
    userpwd = input("Enter your password : ")
    username = None
    success = True
    with open('users.csv') as file:
        reader = csv.reader(file)

        for user in reader:
            print(user)
        # for u in user:
            # if u[1] == usermail and u[2] == userpwd:
            if usermail in user and userpwd in user:
                success = True
                username = user[0]
                break
            else:
                success = False
        if success:
            print("Login Success...")
            login_success(username)

        elif not success:
            print("Login Failed...")

def register():
    username = input("Enter your name : ")

    flag = True
    while flag:
        usermail = input("Enter your mailID : ")

        if len(users) >= 1:
            for user in users:
                if user['mail'] == usermail:
                    print("User Already Exist")
                    break
            else:
                flag = False
        else:
            break

    userpwd = input("Enter your password : ")
    confpwd = input("Confirm password : ")

    userdata['name'] = username
    userdata['mail'] = usermail
    userdata['password'] = confpwd

    users.append(userdata.copy())

    for data in users:
        print(data)

    saveUser()


def saveUser():
    with open('users.csv','w', newline='') as file:
        writer = csv.writer(file)

        for user in users:
            writer.writerow(user.values())


def loadUser():
    pass


def errHandler():
    print("Wrong Choice...")

while True:
    print("""
    1. Login
    2. Register
    """)

    user_ch = input("Enter your choice : ")

    todo = {
        "1" : login,
        "2" : register
    }

    todo.get(user_ch, errHandler)()