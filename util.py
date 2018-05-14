import re
import random
import string

# Check to see if the player enters an invalid nameself
# Empty name will not be allowed
def set_player_name(playerNum=1):
    player = input("Please enter your name (Player {}): ".format(playerNum))
    while not player.strip():
        print("\nInvalid name. Please try again. \n")
        player = input("Please enter your name: ")
    return player

# Setting up player objects to keep track of the progress of the game for each player
def set_player_object(game, player1, flag1, player2, flag2):
    game.player1["name"] = player1
    game.player2["name"] = player2
    game.player1["type"] = flag1
    game.player2["type"] = flag2

# Ask user for a token choice and validate that token
def set_player_token(player, tokenToCompare=None):
    ptoken = input("Please enter the token of your choice ({}): ".format(player))
    while not isTokenValid(ptoken, tokenToCompare):
        print("\nInvalid token for player '{}'. Please try again. \n".format(player))
        ptoken = input("Please enter the token of your choice ({}): ".format(player))
    return ptoken.upper()


def set_cpu_token(tokenToCompare=None):
    cpuToken = random.choice(string.ascii_uppercase)
    while not isTokenValid(cpuToken, tokenToCompare):
        cpuToken = random.choice(string.ascii_uppercase)
    return cpuToken

# A helper function set_turn()
# Put players in the right order for the game to start
def set_turn_helper(game, picker, player2):
    print("{} will pick which player goes first.\n".format(picker["name"]))
    print("Would you like to go first or last, {}? (Enter number): ".format(picker["name"]))
    print("\n1. Go first")
    print("2. Go last\n")

    choice = input("Your choice is: ")
    while not re.match("^[1-2]{1}$", choice):
        print("\nInvalid selection. Please try again. \n")
        choice = input("Your choice is: ")

    if choice == "1":
        game.game_order.append(picker)
        game.game_order.append(player2)
    else:
        game.game_order.append(player2)
        game.game_order.append(picker)

    print("\n{} will go first.".format(game.game_order[0]["name"]))
    print("{} will go last.".format(game.game_order[1]["name"]))

# Check to make sure the token enter matches the below criteria:
# Must be length of 1
# Must be a letter from A-Z, regardless of upper or lower case
def isTokenValid(token, tokenToCompare=None):
    if re.match("^[a-zA-Z]{1}$", token):
        if tokenToCompare is not None:
            if token != tokenToCompare:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def rolldice():
    return random.randint(1, 6)
