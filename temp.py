# Generate best moves by scanning through combinations of patterns
# and check against whether it'll lead to opponent winning the game or
# the way around while keep track of scores of each move.
def best_move(self, board, nextMove, player):

    # Always start at the middle if it's available and AI is first turn
    if (len(board.available_moves()) == 9):
        return [4]
    # Score system for analyzing each move
    if (Game.ifPlayerWin(board, player.opponent)):
        return (-1, -10)
    elif (Game.ifPlayerWin(board, player)):
        return (-1, 10)
    elif (Game.tie(board, player, player.opponent)):
        return (-1, 0)

    moves = []
    # Simulate opponent's moves and generate best countermoves.
    for move in board.available_moves():
        board.insert_board(move, nextMove.token)
        # Recursively call best_move to simulate the next best move and next countermoves
        score = self.best_move(board, nextMove.opponent, player)[1]
        moves.append((move, score))
        # Undo the changes to reflect the current state of the board
        board.board[move] = move + 1

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
