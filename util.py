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

def set_player_token(player, tokenToCompare=None):
    ptoken = input("Please enter the token of your choice ({}): ".format(player))
    while not isTokenValid(ptoken, tokenToCompare):
        print("\nInvalid token for player '{}'. Please try again. \n".format(player))
        ptoken = input("Please enter the token of your choice ({}): ".format(player))
    return ptoken.upper()

def set_cpu_token(tokenToCompare=None):
    cpuToken = random.choice(string.ascii_uppercase)
    while not isTokenValid(cpuToken, tokenToCompare):
        cpuToken = cpuToken = random.choice(string.ascii_uppercase)
    return cpuToken.upper()

# Check to make sure the token enter matches the below criteria:
# Must be length of 1
# Must be a letter from A-Z, regardless of upper or lower case
def isTokenValid(token, tokenToCompare=None):
    if re.match("^[a-zA-Z]{1}$", token):
        # Check if player1 token has been set if not then current token will belong to player1
        # Otherwise compare current token with player1's to determine its validity
        if tokenToCompare is not None:
            if token.upper() != tokenToCompare:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
