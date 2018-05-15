from player import *

class Cpu(Player):

    def __init__(self, name):
        super().__init__(name)

    def make_a_move(self, game):
        player = self
        tokens = [player.token for player in game.game_order]
        move = player.best_move(game, tokens, player, player)[0]
        game.board.update_visual(move, player.token)
        return move + 1

    # Generate best moves by scanning through combinations of patterns
    # and check against whether it'll lead to opponent winning the game or
    # the way around while keep track of scores of each move.
    def best_move(self, game, tokens, nextMove, player):
        # Always start at the middle if it's available and AI is first turn
        if (len(game.board.available_moves(tokens)) == 9):
            return [4]
        # Score system for analyzing each move
        if (game.ifPlayerWin(game.get_opponent(player))):
            return (-1, -10)
        elif (game.ifPlayerWin(player)):
            return (-1, 10)
        elif (game.tie()):
            return (-1, 0)

        moves = []
        # Simulate opponent's moves and generate best countermoves.
        for move in game.board.available_moves(tokens):
            game.board.insert_board(move, nextMove.token)
            # Recursively call best_move to simulate the next best move and next countermoves
            score = self.best_move(game, tokens, game.get_opponent(nextMove), player)[1]
            moves.append((move, score))
            # Undo the changes to reflect the current state of the board
            game.board.board[move] = move + 1

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
