hello_msg = "Hello ! How are you ?"
bye_msg = "Bye, Take Care"

while True:

    user_message = input("Enter your message : ")
    user_message = user_message.lower()

    if user_message == "hi" or user_message == "hello" or user_message == "hey":
        print(hello_msg)

    elif user_message == "bye" or user_message == "see you" or user_message == "bie":
        print(bye_msg)

    else:
        print("I don't understand")