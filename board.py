class Board:
    def __init__(self):
        # Initialize an empty 3x3 board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def reset(self):
        # Reset the board to empty
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def is_valid_move(self, row, col):
        # Check if a move is valid (empty spot)
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            return True
        return False

    def make_move(self, row, col, player):
        # Make a move on the board
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False

    def check_winner(self, player):
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def is_full(self):
        # Check if the board is full
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    return False
        return True

    def get_empty_cells(self):
        # Return a list of empty cells as (row, col) tuples
        empty_cells = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    empty_cells.append((row, col))
        return empty_cells

    def copy(self):
        # Create a deep copy of the board
        new_board = Board()
        for row in range(3):
            for col in range(3):
                new_board.board[row][col] = self.board[row][col]
        return new_board
