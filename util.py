# Check to see if the player enters an invalid nameself
# Empty name will not be allowed
def set_player_name(playerNum=1):
    player = input("Please enter your name (Player {}): ".format(playerNum))
    while not player.strip():
        print("\nInvalid name. Please try again. \n")
        player = input("Please enter your name: ")
    return player

# Setting up player objects to keep track of the progress of the game for each player
def set_players_object(self, player1, flag1, player2, flag2):
    self.player1["name"] = player1
    self.player2["name"] = player2
    self.player1["type"] = flag1
    self.player2["type"] = flag2
