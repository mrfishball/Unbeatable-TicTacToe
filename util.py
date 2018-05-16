import re
import random
import string

# Check to see if the player enters an invalid nameself
# Empty name will not be allowed
def get_name_input(playerNum=1):
    player = input("Please enter your name (Player {}): ".format(playerNum))
    while not player.strip():
        print("\nInvalid name. Please try again. \n")
        player = input("Please enter your name: ")
    return player.strip()

# Ask user for a token choice and validate that token
def get_token_input(player, tokens):
    ptoken = input("Please enter the token of your choice ({}): ".format(player))
    while not isTokenValid(ptoken, tokens):
        print("\nInvalid token for player '{}'. Please try again. \n".format(player))
        ptoken = input("Please enter the token of your choice ({}): ".format(player))
    ptoken = ptoken.lower()
    tokens.append(ptoken)
    return ptoken.upper()

def get_human_spot(board, player):
    spot = input("{}, please make a move on the board (1 - 9): ".format(player.name))
    while not board.isValidMove(spot):
      spot = input("{}, please make a move on the board (1 - 9): ".format(player.name))
    spot = int(spot)
    return spot-1

# Generate token for AI
def generate_token(tokens):
    cpuToken = random.choice(string.ascii_lowercase)
    while not isTokenValid(cpuToken, tokens):
        cpuToken = random.choice(string.ascii_lowercase)
    tokens.append(cpuToken)
    return cpuToken.upper()

# A helper function set_turn()
# Put players in the right order for the game to start
def set_turn_helper(game_order, picker, player2):
    print("{} will pick which player goes first.\n".format(picker.name))
    print("Would you like to go first or last, {}? (Enter number): ".format(picker.name))
    print("\n1. Go first")
    print("2. Go last\n")

    choice = input("Your choice is: ")
    while not re.match("^[1-2]{1}$", choice):
        print("\nInvalid selection. Please try again. \n")
        choice = input("Your choice is: ")

    if choice == "1":
        game_order.append(picker)
        game_order.append(player2)
    else:
        game_order.append(player2)
        game_order.append(picker)

# Check to make sure the token enter matches the below criteria:
# Must be length of 1
# Must be a letter from A-Z, regardless of upper or lower case
def isTokenValid(token, tokens):
    token = token.lower()
    if re.match("^[a-zA-Z]{1}$", token):
        if token in tokens:
            return False
        else:
            return True
    else:
        return False

def rolldice():
    return random.randint(1, 6)
