help_message = '''start - to start the car
stop - to stop the car
quit - to exit
'''
started = False

while True:
    user_command = input(">").lower()
    if user_command == "help":
        print(help_message)
    elif user_command == "start":
        if started:
            print("Car already started!")
        else:
            print("Car started...Ready to go!")
            started = True
    elif user_command == "stop":
        if not started:
            print("Car already stopped!")
        else:
            print("Car stopped.")
            started = False
    elif user_command == "quit":
        break
    else:
        print("I don't understand that...")
