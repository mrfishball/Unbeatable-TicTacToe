import re
import random
import util

class Game:

  # Flags for identifying a cpu player or a human player.
  CPU = "CPU"
  HUMAN = "Human"

  def __init__(self):
    self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    self.player1 = {}
    self.player2 = {}
    self.game_order = [] # Turn goes according to the player's position in the array
    self.game_over = False
    self.winner = None

  @staticmethod
  def rolldice():
      return random.randint(1, 6)

  def start_game(self):
    print("\nWelcome to the game Tic Tac Toe!")
    gameMode = self.set_game_mode()
    self.set_players(gameMode)
    self.set_token(gameMode)
    self.set_turn(gameMode)
    self.draw_board(self.board)

    while not self.game_over:
      # Loop through the array to keep correct turns
      for player in self.game_order:
          move = None
          # Check player type to determine whether to ask for an input for the move or to generate a move
          if player["type"] == Game.HUMAN:
              move = self.get_human_spot(self.board, player)
          else:
              # If play is CPU type, generate moves
              move = self.best_move(self.board, player, player)[0]

          self.make_a_move(move, player)
          self.draw_board(self.board)
          print("\nPlayer '{}({})' chose spot '{}'".format(player["name"], player["token"], move+1))

          # If a player wins, update the winner status and exist the game
          if (self.ifPlayerWin(player)):
              self.winner = player["name"]
              self.game_over = True
              print("\n{} won the game!".format(player["name"]))
              break

          # If it's a tie, update the game_over status and exist the game
          if (self.tie(self.board)):
              self.game_over = True
              print("\nIt's a tie!")
              break

  # Basic board structure
  # Added padding on both sides for better readibility
  def draw_board(self, board):
      print("""
        {} | {} | {}
       -----------
        {} | {} | {}
       -----------
        {} | {} | {}
      """.format(*board))

  # Select game mode from:
  # Single player mode (Human vs Comp)
  # Versus mode (Human vs Human)
  # Spectator mode (Comp vs Comp)
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

      if (gameMode == 1):
          player = util.set_player_name()
          util.set_player_object(self, player, Game.HUMAN, "COMP", Game.CPU)
      elif (gameMode == 2):
          player1 = util.set_player_name()
          player2 = util.set_player_name(2)
          util.set_player_object(self, player1, Game.HUMAN, player2, Game.HUMAN)
      else:
          util.set_player_object(self, "COMP 1", Game.CPU, "COMP 2", Game.CPU)

  # Player can use any letters as tokens
  # Numbers and special unicode characters will not be allowed
  def set_token(self, gameMode):

      print("\nSelect a token: ")
      print("A token is a letter (A to Z) that will be used to mark your moves on the board. \n")
      p1Token = None
      p2Token = None

      if (gameMode == 3):
          p1Token = util.set_cpu_token()
          p2Token = util.set_cpu_token(p1Token)

      elif (gameMode == 2):
          p1Token = util.set_player_token(self.player1["name"])
          p2Token = util.set_player_token(self.player2["name"], p1Token)

      else:
          p1Token = util.set_player_token(self.player1["name"])
          p2Token = util.set_cpu_token(p1Token)

      self.player1["token"] = p1Token
      self.player2["token"] = p2Token

      print("\nThe token for '{}' is '{}'".format(self.player1["name"], self.player1["token"]))
      print("The token for '{}' is '{}'".format(self.player2["name"], self.player2["token"]))

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

          print("\n{} will go first.".format(self.game_order[0]["name"]))
          print("{} will go last.".format(self.game_order[1]["name"]))

      elif (gameMode == 2):
          print("Roll dice to determine who gets to choose turn. \n")
          p1dice = Game.rolldice()
          p2dice = Game.rolldice()
          print("{} rolled {}".format(self.player1["name"], p1dice))
          print("{} rolled {}\n".format(self.player2["name"], p2dice))
          while p1dice == p2dice:
              p1dice = Game.rolldice()
              p2dice = Game.rolldice()
              print("{} rolled {}".format(self.player1["name"], p1dice))
              print("{} rolled {}\n".format(self.player2["name"], p2dice))
          if p1dice > p2dice:
              self.set_turn_helper(self.player1, self.player2)
          else:
              self.set_turn_helper(self.player2, self.player1)
      else:
          self.set_turn_helper(self.player1, self.player2)

  # A helper function set_turn()
  # Put players in the right order for the game to start
  def set_turn_helper(self, picker, player2):
      print("{} will pick which player goes first.\n".format(picker["name"]))
      print("Would you like to go first or last, {}? (Enter number): ".format(picker["name"]))
      print("\n1. Go first")
      print("2. Go last\n")
      choice = input("Your choice is: ")
      while not re.match("^[1-2]{1}$", choice):
          print("\nInvalid selection. Please try again. \n")
          choice = input("Your choice is: ")

      if choice == "1":
          self.game_order.append(picker)
          self.game_order.append(player2)
          print("\n{} will go first.".format(picker["name"]))
          print("{} will go last.".format(picker2["name"]))

      else:
          self.game_order.append(player2)
          self.game_order.append(picker)
          print("\n{} will go first.".format(player2["name"]))
          print("{} will go last.".format(picker["name"]))

  # Verify user input before making the move.
  def isValidMove(self, board, move):
      try:
          move = int(move)
          if move in board:
              return True
          else:
              print("\nThis spot is taken. Please try again.")
              return False
      except (TypeError, ValueError, IndexError) as e:
          print("\nThis is not a valid move. Please try again.")
          return False

  # Makes moves permanent on the board
  def make_a_move(self, position, player):
      self.board[position] = player["token"]

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
