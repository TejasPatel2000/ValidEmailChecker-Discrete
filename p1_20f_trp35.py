def dfachecker(uStr):
    # Tejas Patel
    # trp35
    # Project 1- Nakayama

    # Set up language using variables
    gamma = "abcdefghijklmnopqrstuvwxyz"
    delta = "."
    phi = "@"
    state_num = 0
    stateChange = False
    # Mention Starting state as per instructions
    print("Starting State: q0")
    # Iterate through every letter in the string to go through state changes
    for char in uStr:
        # Made this variable to prevent code from doing multiple state checks on one char
        stateChange = False

        # What to do in state 10
        if state_num == 10 and char in gamma and stateChange == False:
            state_num = 6
            stateChange = True
        elif state_num == 10 and char in delta and stateChange == False:
            state_num = 7
            stateChange = True
        elif state_num == 10 and stateChange == False:
            # State 11 is the Trap State
            state_num = 11
            stateChange = True

        # What to do in state 9
        if state_num == 9 and char == "u" and stateChange == False:
            state_num = 10
        elif state_num == 9 and char in gamma and stateChange == False:
            state_num = 6
        elif state_num == 9 and char in delta and stateChange == False:
            state_num = 7
            stateChange = True
        elif state_num == 9 and stateChange == False:
            state_num = 11

        # What to do in state 8
        if state_num == 8 and char == "d" and stateChange == False:
            state_num = 9
            stateChange = True
        elif state_num == 8 and char in gamma and stateChange == False:
            state_num = 6
            stateChange = True
        elif state_num == 8 and char in delta and stateChange == False:
            state_num = 7
            stateChange = True
        elif state_num == 8 and stateChange == False:
            state_num = 11

        # What to do in state 7
        if state_num == 7 and char == "e" and stateChange == False:
            state_num = 8
            stateChange = True
        elif state_num == 7 and char in gamma and stateChange == False:
            state_num = 6
            stateChange = True
        elif state_num == 7 and stateChange == False:
            state_num = 11
            stateChange = True

        # What to do in state 6
        if state_num == 6 and char in gamma and stateChange == False:
            state_num = 6
            stateChange = True
        elif state_num == 6 and char in delta and stateChange == False:
            state_num = 7
            stateChange = True
        elif state_num == 6 and stateChange == False:
            state_num = 11
            stateChange = True

        # What to do in state 5
        if state_num == 5 and char == "e" and stateChange == False:
            state_num = 8
            stateChange = True
        elif state_num == 5 and char in gamma and stateChange == False:
            state_num = 6
            stateChange = True
        elif state_num == 5 and stateChange == False:
            state_num = 11
            stateChange = True

        # What to do in state 4
        if state_num == 4 and char in gamma and stateChange == False:
            state_num = 4
            stateChange = True
        elif state_num == 4 and char in delta and stateChange == False:
            state_num = 5
            stateChange = True
        elif state_num == 4 and stateChange == False:
            state_num = 11
            stateChange = True

        # What to do in state 3
        if state_num == 3 and (char in gamma) and (stateChange == False):
            state_num = 4
            stateChange = True
        elif state_num == 3 and char not in gamma and stateChange == False:
            state_num = 11
            stateChange = True

        # what to do in state 2
        if state_num == 2 and (char in gamma) and (stateChange == False):
            state_num = 1
            stateChange = True
        elif state_num == 2 and (char not in gamma) and stateChange == False:
            state_num = 11
            stateChange = True

        # What to do in in state 1
        if state_num == 1 and (char in delta) and (stateChange == False):
            state_num = 2
            stateChange = True
        elif state_num == 1 and char in gamma and stateChange == False:
            state_num = 1
            stateChange = True
        elif state_num == 1 and char in phi and stateChange == False:
            state_num = 3
            stateChange = True
        elif state_num == 1 and stateChange==False:
            state_num = 11
            stateChange = True

        # What to do in in state 0
        if state_num == 0 and char in gamma and stateChange == False:
            state_num = 1
        elif state_num == 0 and stateChange == False:
            state_num = 11

        # Print char and state you are currently in
        print("Character: " + char + " State Number: q" + str(state_num))
    # Print whether or not the email is valid
    if state_num == 10:
        print("Email IS Valid")
    else:
        print("Email IS NOT Valid")

def main():
    # print Header
    print(
        "Project 1 for CS 341\nSemester: Fall 2020\nWritten by: Tejas Patel, trp35\nInstructor: Marvin Nakayama, marvin@njit.edu")
    print("\n")
    # get user input
    userInput = input("Hello, would you like to check your email? Enter y if so!")
    # check email and call method
    if userInput == "y":
        userString = input("Enter an email address: ")
        dfachecker(userString)
    else:
        print("Okay, thank you have a nice day!")


if __name__ == "__main__":
    main()
