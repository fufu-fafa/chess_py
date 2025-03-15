from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'white'
        self.running = True
    
    def switch_turn(self):
        """Switch the turn between players."""
        self.turn = 'black' if self.turn == 'white' else 'white'
    
    def is_valid_move(self, start, end):
        """Check if a move is valid (basic validation, no full chess rules)."""
        piece = self.board.board[start[0]][start[1]]
        if not piece or piece[1] != self.turn:
            return False
        return True
    
    def play_turn(self, start, end):
        """Execute a player's move if valid."""
        if self.is_valid_move(start, end):
            self.board.move_piece(start, end)
            self.switch_turn()
            return True
        else:
            print("Invalid move. Try again.")
            return False
    
    def display_board(self):
        """Display the current board state."""
        self.board.display()
    
    def start(self):
        """Start the game loop."""
        while self.running:
            self.display_board()
            print(f"{self.turn}'s turn. Enter move (e.g., 'e2 e4'):")
            move = input().strip().lower()
            
            if move == 'quit':
                print("Game over.")
                self.running = False
                break
            
            try:
                start, end = move.split()
                start = (8 - int(start[1]), ord(start[0]) - ord('a'))
                end = (8 - int(end[1]), ord(end[0]) - ord('a'))
                self.play_turn(start, end)
            except Exception as e:
                print("Invalid input format. Use notation like 'e2 e4'.")

