import random as rnd


# Functions...

def statement_generator(statement, side, top_bottom):
    greeting = statement

    sides = side

    greeting = "{} {} {}".format(sides, greeting, sides)

    top_button = top_bottom * len(greeting)

    print("\n\n        {}\n        {}\n"
          "        {}".format(top_button, greeting, top_button))

    return ""

def Choice_checker(question):
    print("\n\n        {}".format(statement_generator("Rock / "
          "Paper / Scissors", " | ", "*")))

    error = "\n\n      Please choose from the options given. "

    while not False:
        response = input(question).lower()
        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response == "scissors":
            return response

        # Check for exit code
        elif response == "xxx":
            return response
        else:
            print(error)

# Main routine...

# List for checking response
yes_no_list = []
rps_list = ["rock","paper","scissors"]

# Loop for testing purposes
user_choice = ""
while user_choice !=  "xxx":

    # Ask the user for choice and check if it's valid
    user_choice = Choice_checker("\n\n      Please choose: Rock / Paper "
                                 "/ Scissors. (or xxx)\n\n      ~~~  ")

    # print out choice for comparison purposes
    print("\n\n     You chose {}".format(user_choice))