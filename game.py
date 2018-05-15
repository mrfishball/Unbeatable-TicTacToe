import re
import random
import util
from board import *
from human import *
from cpu import *

class Game:

  def __init__(self):
    self.board = Board()
    self.player1 = None
    self.player2 = None
    self.game_order = [] # Turn goes according to the player's position in the array
    self.game_over = False
    self.winner = None

  def start_game(self):
    print("\nWelcome to Tic Tac Toe Classic!")
    gameMode = self.set_game_mode()
    self.set_players(gameMode)
    self.set_token(gameMode)
    self.set_turn(gameMode)
    self.board.draw_board()

    while not self.game_over:
      # Loop through the array to keep correct turns
      for player in self.game_order:
          
          player_name = player.name
          player_token = player.token

          move = player.make_a_move(self)
          self.board.draw_board()
          print("\n'{} ({})' chose spot '{}'".format(player_name, player_token, move))

          # If a player wins, update the winner status and exist the game
          if (self.ifPlayerWin(player)):
              self.winner = player_name
              self.game_over = True
              print("\n{} win!".format(player_name))
              break

          # If it's a tie, update the game_over status and exist the game
          if (self.tie()):
              self.game_over = True
              print("\nIt's a tie!")
              break

  def set_game_mode(self):
      print("\nSelect a game mode: \n")
      print("1. Play against a super computer")
      print("2. Play with a friend")
      print("3. Spectate a game (CPU vs CPU) \n")
      gameMode = input("Your choice is (Enter the number): ")

      # If the user input is not an integer or not in range of
      # the menu options, throw an error and ask for input until it's valid
      while not re.match("^[1-3]{1}$", gameMode):
          print("\nInvalid entry. Please try again. \n")
          gameMode = input("Your choice is (Enter the number): ")
      print("Setting up the game... \n")
      return int(gameMode)

  def set_players(self, gameMode):
      player1 = None
      player2 = None

      if (gameMode == 1):
          name1 = util.get_name_input()
          player1 = Human(name1)
          player2 = Cpu("Iris")

      elif (gameMode == 2):
          name1 = util.get_name_input()
          name2 = util.get_name_input(2)
          player1 = Human(name1)
          player2 = Human(name2)

      else:
          player1 = Cpu("Iris (AI)")
          player2 = Cpu("Betty (AI)")

      self.player1 = player1
      self.player2 = player2

  # Player can use any letters as tokens
  # Numbers and special unicode characters will not be allowed
  def set_token(self, gameMode):
      tokens = []
      p1Token = None
      p2Token = None
      player1 = self.player1.name
      player2 = self.player2.name

      if (gameMode == 3):
          p1Token = util.generate_token(tokens)
          p2Token = util.generate_token(tokens)

      else:
          print("\nSelect a token: ")
          print("A token is a letter (A to Z) that will be used to mark your moves on the board. \n")

          if (gameMode == 2):
              p1Token = util.get_token_input(player1, tokens)
              p2Token = util.get_token_input(player2, tokens)

          else:
              p1Token = util.get_token_input(player1, tokens)
              p2Token = util.generate_token(tokens)

      self.player1.set_token(p1Token)
      self.player2.set_token(p2Token)

      print("\nThe token for '{}' is '{}'".format(player1, p1Token))
      print("The token for '{}' is '{}'".format(player2, p2Token))

  # Pick which player goes first
  # Only if versus mode is selected then players will roll dice to determine who gets to
  # choose to go first or last
  def set_turn(self, gameMode):
      print("\nTurn Selection:")
      print("You can choose to go first or let the other player go first.\n")

      if (gameMode == 3):
          self.game_order.append(self.player1)
          self.game_order.append(self.player2)
          random.shuffle(self.game_order)

      elif (gameMode == 2):
          print("Roll dice to determine who gets to choose turn. \n")

          # Set initial value to None for both to ensure the while loop entry
          # which will handle the actual dice roll
          p1dice = None
          p2dice = None
          while p1dice == p2dice:
              p1dice = util.rolldice()
              p2dice = util.rolldice()

          print("{} rolled {}".format(self.player1.name, p1dice))
          print("{} rolled {}\n".format(self.player2.name, p2dice))

          if p1dice > p2dice:
              util.set_turn_helper(self.game_order, self.player1, self.player2)
          else:
              util.set_turn_helper(self.game_order, self.player2, self.player1)
      else:
          util.set_turn_helper(self.game_order, self.player1, self.player2)

      print("\n{} will go first.".format(self.game_order[0].name))
      print("{} will go last.".format(self.game_order[1].name))

  # Get the next player to make a move.
  def get_opponent(self, player):
      if player == self.player1:
          return self.player2
      return self.player1

  # Check if the game's been won by a player
  def ifPlayerWin(self, player):
      board = re.sub('[()]', '', self.board.board)
      token = player.token
      return (board[0] == board[1] == board[2] == token) or \
        (board[3] == board[4] == board[5] == token) or \
        (board[6] == board[7] == board[8] == token) or \
        (board[0] == board[3] == board[6] == token) or \
        (board[1] == board[4] == board[7] == token) or \
        (board[2] == board[5] == board[8] == token) or \
        (board[0] == board[4] == board[8] == token) or \
        (board[2] == board[4] == board[6] == token)

  # Check if game is tie
  def tie(self):
    return len([spot for spot in self.board.board if spot == self.player1.token
        or spot == self.player2.token]) == 9

if __name__ == '__main__':
  game = Game()
  game.start_game()
