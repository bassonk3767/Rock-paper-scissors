# Function...

# Function that check the amount of rounds that the player wam=nts to play
def check_rounds():
    while True:
        response = input("\n\n      How many rounds wou"
                         "ld you like to play?\n\n     ~~~  ")
        round_error = "\n\n     Please type either <enter> " \
                      "or an integer  that is higher than 0"
        if response != "":
            try:
                # converting input so that it can be checked by length
                response = int(response)

                if response < 1:
                    print(round_error)
                    return response

            # If response by any chance has an unexpected error
            except ValueError:
                print(round_error)
                continue

        return response


# Main routine...
chosen = ""

rounds_played = 0
choose_instruction = "\n\n     Please choose rock" \
                      " (r), paper (p), scissors (s)\n\n    ~~~ "

# Ask user for # of rounds, and they can <enter> for infinite rounds mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print("\n\n     ")
    if rounds == "":
        heading = "Continuous Mode: Round #{}".format(rounds_played)
        print(heading)
        choose = input("\n\n    {} or 'xxx' to end".format(choose_instruction))
        if choose == "xxx":
            break
    else:
        heading = "\n\n     Round #{} of {}".format(rounds_played +1,rounds)
        print(heading)
        choose = input(choose_instruction)
        if rounds_played == rounds - 1:
            end_game = "yes"


    # Rest of loop / game
    if choose == "rock" or choose == "r":
        chosen = "rock"

    elif choose == "paper" or choose == "p":
        chosen = "paper"

    elif choose == "scissors" or choose == "s":
        chosen = "scissors"

    print("\n\n     You choose {}".format(chosen))

    rounds_played += 1

print("\n\n     Thank you for playing.")