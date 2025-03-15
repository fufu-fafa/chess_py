class Board:
    def __init__(self):
        self.board = self._initialize_board()

    def _initialize_board(self):
        """Initialize the chessboard with pieces in starting positions."""
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Pawns
        for i in range(8):
            board[1][i] = ('P', 'white')  # White Pawns
            board[6][i] = ('P', 'black')  # Black Pawns
        
        # Other Pieces
        piece_order = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i, piece in enumerate(piece_order):
            board[0][i] = (piece, 'white')  # White back row
            board[7][i] = (piece, 'black')  # Black back row
        
        return board

    def display(self):
        """Prints the chessboard in a readable format."""
        for row in self.board:
            print(' '.join([f'{p[0][0]}({p[1][0]})' if p else '----' for p in row]))
        print('\n')
    
    def move_piece(self, start, end):
        """Move a piece from start to end if the move is valid."""
        sx, sy = start
        ex, ey = end
        
        if not (0 <= sx < 8 and 0 <= sy < 8 and 0 <= ex < 8 and 0 <= ey < 8):
            print("Invalid move: Out of bounds.")
            return False
        
        piece = self.board[sx][sy]
        if not piece:
            print("Invalid move: No piece at the start position.")
            return False
        
        self.board[ex][ey] = piece
        self.board[sx][sy] = None
        return True

