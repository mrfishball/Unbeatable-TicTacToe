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
    self.tokens = []
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
          player_name = player.get_name()
          player_token = player.get_token()
          move = None
          # Check player type to determine whether to ask for an input for the move or to generate a move
          if player["type"] == Game.HUMAN:
              move = self.get_human_spot(self.board, player)
          else:
              # If play is CPU type, generate moves
              move = self.best_move(self.board, player, player)[0]

          self.make_a_move(move, player)
          self.board.draw_board()
          print("\n'{} ({})' chose spot '{}'".format(player_name, player_token, move+1))

          # If a player wins, update the winner status and exist the game
          if (self.ifPlayerWin(player)):
              self.winner = player_name
              self.game_over = True
              print("\n{} win!".format(player_name))
              break

          # If it's a tie, update the game_over status and exist the game
          if (self.tie(self.board)):
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
      player1 = self.player1.get_name()
      player2 = self.player2.get_name()

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

          print("{} rolled {}".format(self.player1.get_name(), p1dice))
          print("{} rolled {}\n".format(self.player2.get_name(), p2dice))

          if p1dice > p2dice:
              util.set_turn_helper(self, self.player1, self.player2)
          else:
              util.set_turn_helper(self, self.player2, self.player1)
      else:
          util.set_turn_helper(self, self.player1, self.player2)

      print("\n{} will go first.".format(self.game_order[0].get_name()))
      print("{} will go last.".format(self.game_order[1].get_name()))

  # Prompt players(human players only) to make a valid move before registering it
  # in make_a_move function
  def get_human_spot(self, board, player):
    spot = input("{}, please make a move on the board (1 - 9): ".format(player["name"]))
    while not self.isValidMove(board, spot):
      # print("\nThis is not a valid move. Please try again.")
      spot = input("{}, please make a move on the board (1 - 9): ".format(player["name"]))
    spot = int(spot)
    return spot-1

  # Get the next player to make a move.
  def get_opponent(self, player):
      if player == self.player1:
          return self.player2
      return self.player1

  # Check if the game's been won by a player
  def ifPlayerWin(self, player):
      # Check horizontal win patterns
      for i in range(0, 7, 3):
          if (self.board[i] == player["token"] and self.board[i+1] == player["token"]
            and self.board[i+2] == player["token"]):
             return True
      # Check vertical win patterns
      for i in range(0, 3):
          if (self.board[i] == player["token"] and self.board[i+3] == player["token"]
            and self.board[i+6] == player["token"]):
             return True
      # Check diagonal win patterns
      if (self.board[0] == player["token"] and self.board[4] == player["token"]
        and self.board[8] == player["token"]):
         return True
      if (self.board[2] == player["token"] and self.board[4] == player["token"]
        and self.board[6] == player["token"]):
         return True
      return False

  # Check if game is tie
  def tie(self, board):
    return len([spot for spot in board if spot == self.player1["token"]
        or spot == self.player2["token"]]) == 9

  # Generate available spots on the board
  def available_moves(self, board):
      return [pos for pos, spot in enumerate(board) if spot != self.player1["token"] and spot != self.player2["token"]]

  # Generate best moves by scanning through combinations of patterns
  # and check against whether it'll lead to opponent winning the game or
  # the way around while keep track of scores of each move.
  def best_move(self, board, nextMove, player):

      # Always start at the middle if it's available and AI is first turn
      if (len(self.available_moves(board)) == 9):
          return [4]

      # Score system for analyzing each move
      if (self.ifPlayerWin(self.get_opponent(player))):
          return (-1, -10)
      elif (self.ifPlayerWin(player)):
          return (-1, 10)
      elif (self.tie(board)):
          return (-1, 0)

      moves = []
      # Simulate opponent's moves and generate best countermoves.
      for move in self.available_moves(board):
          self.make_a_move(move, nextMove)
          # Recursively call best_move to simulate the next best move and next countermoves
          score = self.best_move(board, self.get_opponent(nextMove), player)[1]
          moves.append((move, score))
          # Undo the changes to reflect the current state of the board
          board[move] = move + 1

      # if the AI player is the player making the next move, then
      # we want to get the best move, move with the highest score
      if(nextMove == player):
          maxScore = moves[0][1]
          bestMove = moves[0]
          for move in moves:
              if (move[1] > maxScore):
                  bestMove = move
                  maxScore = move[1]
          return bestMove
      # if the next player is the opponent, get the move with
      # the lowest score
      else:
          minScore = moves[0][1]
          minMove = moves[0]
          for move in moves:
              if (move[1] < minScore):
                  minMove = move
                  minScore = move[1]
          return minMove

if __name__ == '__main__':
  game = Game()
  game.start_game()
