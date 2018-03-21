import random

hello_intent = ['hello','hi','hey','good morning','hie']

bye_intent = ['bye','see you','bie','take care']

while True:

    hello_msg = random.choice(hello_intent)
    bye_msg = random.choice(bye_intent)

    user_message = input("Enter your message : ")
    user_message = user_message.lower()

    if user_message in hello_intent:
        print(hello_msg)

    elif user_message in bye_intent:
        print(bye_msg)

    else:
        print("I don't understand")
        break
