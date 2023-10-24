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
                    continue

            # If response by any chance has an unexpected error
            except ValueError:
                print(round_error)
                continue
    return ""


# Main routine...

rounds_played = 0
choose_instructions = "\n\n     Please choose rock" \
                      " (r), paper (p), scissors (s)"

# Ask user for # of rounds, and they can <enter> for infinite rounds mode
rounds = check_rounds()
