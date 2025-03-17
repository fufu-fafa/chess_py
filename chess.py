class chess:
    def __init__(self):
        self.board = self.create_board()
        self.turn = "white"

    # pieces rule
    def validate_move(self, piece, start_row, start_col, end_row, end_col):
        delta_row = end_row - start_row
        delta_col = end_col - start_col
        target_piece = self.board[end_row][end_col]

        is_white = piece.isupper()
        if (self.turn == "white" and not is_white) or (self.turn == "black" and is_white):
            print("You cannot move the opponent's piece!")
            return False

        # Check same-color capture
        if target_piece != "." and (target_piece.isupper() == piece.isupper()):
            print("Cannot capture your own piece!")
            return False

        piece_type = piece.lower()

        if piece_type == "p":  # Pawn
            direction = -1 if is_white else 1
            start_rank = 6 if is_white else 1

            # Move forward
            if delta_col == 0:
                if delta_row == direction and target_piece == ".":
                    return True
                # Double move from starting position
                if start_row == start_rank and delta_row == 2 * direction:
                    intermediate_row = start_row + direction
                    if self.board[intermediate_row][start_col] == "." and target_piece == ".":
                        return True
            # Capture diagonally
            if abs(delta_col) == 1 and delta_row == direction and target_piece != ".":
                return True
            return False

        elif piece_type == "r":  # Rook
            if delta_row != 0 and delta_col != 0:
                return False
            if not self.is_path_clear(start_row, start_col, end_row, end_col):
                return False
            return True

        elif piece_type == "n":  # Knight
            if (abs(delta_row), abs(delta_col)) in [(2, 1), (1, 2)]:
                return True
            return False

        elif piece_type == "b":  # Bishop
            if abs(delta_row) != abs(delta_col):
                return False
            if not self.is_path_clear(start_row, start_col, end_row, end_col):
                return False
            return True

        elif piece_type == "q":  # Queen
            if abs(delta_row) == abs(delta_col) or delta_row == 0 or delta_col == 0:
                if not self.is_path_clear(start_row, start_col, end_row, end_col):
                    return False
                return True
            return False

        elif piece_type == "k":  # King
            if abs(delta_row) <= 1 and abs(delta_col) <= 1:
                return True
            return False

        return False
    
    def is_path_clear(self, start_row, start_col, end_row, end_col):
        row_step = (end_row - start_row) // max(1, abs(end_row - start_row)) if start_row != end_row else 0
        col_step = (end_col - start_col) // max(1, abs(end_col - start_col)) if start_col != end_col else 0

        current_row, current_col = start_row + row_step, start_col + col_step
        while (current_row, current_col) != (end_row, end_col):
            if self.board[current_row][current_col] != ".":
                return False
            current_row += row_step
            current_col += col_step
        return True

    def create_board(self):
        """Initializes the chessboard with pieces in their starting positions."""
        board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],  
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],  
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]
        return board

    def print_board(self):
        """Prints the current state of the board."""
        print("\n  a b c d e f g h")
        print("  ---------------")
        for i, row in enumerate(self.board):
            print(f"{8 - i}|{' '.join(row)}|{8 - i}")
        print("  ---------------")
        print("  a b c d e f g h")

    def move_piece(self, start, end):
        """Moves a piece from start position to end position."""
        start_col = ord(start[0]) - ord("a")
        start_row = 8 - int(start[1])
        end_col = ord(end[0]) - ord("a")
        end_row = 8 - int(end[1])

        piece = self.board[start_row][start_col]
        if piece == ".":
            print("No piece at the selected position!")
            return False

        if self.validate_move(piece, start_row, start_col, end_row, end_col):
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = "."
            self.turn = "black" if self.turn == "white" else "white"
            return True
        else:
            print("Illegal move!")
            return False


    def play(self):
        """Main game loop."""
        while True:
            self.print_board()
            move = input(f"{self.turn.capitalize()}'s move (e.g., e2 e4): ").strip().lower()
            if move == "exit":
                print("Game over!")
                break

            try:
                start, end = move.split()
                if self.move_piece(start, end):
                    continue
            except ValueError:
                pass

            print("Invalid move! Try again.")


if __name__ == "__main__":
    game = chess()
    game.play()

