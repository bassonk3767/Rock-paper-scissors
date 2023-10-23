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

    while not False:
        response = input(question).lower()
        if response == "r" or response == "rock":
            return response


# Main routine...

# Ask the user for choice and check if it's valid
user_choice = Choice_checker("\n\n      Please choose:"
                             " Rock / Paper / Scissors\n\n      ~~~  ")

# print out choice for comparison purposes
