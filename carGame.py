game_running = True
command = ''
last_command = ''

while game_running:
    command = input("command -> ").title()
    if command == 'Help':
        print("""
Try these commands:
"Start" -Starts your car
"Stop" -Stops your car
"Quit" -Ends the Game
"Help" -Gives the user options
        """)
    elif command == 'Start' and last_command == 'Start':
        print('your car has already started')
    elif command == 'Stop' and last_command == 'Stop':
        print('your car is already stoped')
    elif command == 'Start':
        last_command = command
        print('your car has started')
    elif command == 'Stop':
        last_command = command
        print('your car has stoped')
    elif command == 'Quit':
        break
    else:
        print('I dont understand that command, type "Help" for input options')