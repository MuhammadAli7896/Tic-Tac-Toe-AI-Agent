class AlphaBetaAgent:
    def __init__(self, player):
        self.player = player  # 'O' for the AI
        self.opponent = 'X' if player == 'O' else 'O'

    def get_best_move(self, board):
        """
        Use the minimax algorithm with alpha-beta pruning to determine the best move.
        Returns (row, col) of the best move.
        """
        # Find the best move using alpha-beta pruning
        best_score = float('-inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')

        for row, col in board.get_empty_cells():
            # Try this move
            board_copy = board.copy()
            board_copy.make_move(row, col, self.player)

            # Calculate score for this move using minimax with alpha-beta pruning
            score = self.minimax(board_copy, 0, False, alpha, beta)

            # Update best move if needed
            if score > best_score:
                best_score = score
                best_move = (row, col)

            # Update alpha
            alpha = max(alpha, best_score)

        return best_move

    def minimax(self, board, depth, is_maximizing, alpha, beta):
        """
        Minimax algorithm with alpha-beta pruning implementation.
        
        Args:
            board: Current board state
            depth: Current depth in the game tree
            is_maximizing: Whether the current move is maximizing or minimizing
            alpha: Best value that the maximizer can guarantee at that level or above
            beta: Best value that the minimizer can guarantee at that level or above
            
        Returns:
            score: The best score the maximizing/minimizing player can get
        """
        # Terminal conditions
        if board.check_winner(self.player):
            return 10 - depth  # AI wins
        elif board.check_winner(self.opponent):
            return depth - 10  # Player wins
        elif board.is_full():
            return 0  # Tie game

        if is_maximizing:
            # Maximizing player (AI)
            best_score = float('-inf')

            for row, col in board.get_empty_cells():
                board_copy = board.copy()
                board_copy.make_move(row, col, self.player)
                score = self.minimax(board_copy, depth + 1, False, alpha, beta)
                best_score = max(score, best_score)

                # Alpha-beta pruning
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Beta cutoff

            return best_score

        else:
            # Minimizing player (human)
            best_score = float('inf')

            for row, col in board.get_empty_cells():
                board_copy = board.copy()
                board_copy.make_move(row, col, self.opponent)
                score = self.minimax(board_copy, depth + 1, True, alpha, beta)
                best_score = min(score, best_score)

                # Alpha-beta pruning
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Alpha cutoff

            return best_score
