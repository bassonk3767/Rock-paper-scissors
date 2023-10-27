import random as rnd

# Function that checks the games rounds
def choice_checker(question, valid_list,error):

    valid = False
    while not valid:

        # Ask user to make a decision (and put choice in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response == "scissors":
            return response

        elif response == "xxx":
            return response
        else:
            print(error)

# Main routine

# Loop for testing purposes
error = "\n\nERROR:\n"
user_choice = ""
while user_choice != "xxx":

    # Asking user to decide and check if it's valid
    user_choice = choice_checker("Choose rock / ")