hello_intent = ['hello','hi','hey','good morning','hie']

bye_intent = ['bye','see you','bie','take care']

hello_msg = "Hello ! How are you ?"
bye_msg = "Bye, Take Care"

while True:

    user_message = input("Enter your message : ")
    user_message = user_message.lower()

    if user_message in hello_intent:
        print(hello_msg)

    elif user_message in bye_intent:
        print(bye_msg)

    else:
        print("I don't understand")
