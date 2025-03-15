class chess:
    def __init__(self):
        self.board = self.create_board()
        self.turn = "white"

    def create_board(self):
        """Initializes the chessboard with pieces in their starting positions."""
        board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"],
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

        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = "."

        self.turn = "black" if self.turn == "white" else "white"
        return True

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

