class Piece:
    def __init__(self, color):
        self.color = color
    
    def is_valid_move(self, start, end, board):
        """To be implemented in specific piece subclasses."""
        raise NotImplementedError

class Pawn(Piece):
    def is_valid_move(self, start, end, board):
        sx, sy = start
        ex, ey = end
        direction = -1 if self.color == 'white' else 1
        
        # Move one step forward
        if sx + direction == ex and sy == ey and board[ex][ey] is None:
            return True
        
        # Move two steps forward from starting position
        if (sx == 1 and self.color == 'black' or sx == 6 and self.color == 'white') and sx + 2 * direction == ex and sy == ey and board[ex][ey] is None:
            return True
        
        # Capture diagonally
        if sx + direction == ex and abs(sy - ey) == 1 and board[ex][ey] is not None and board[ex][ey].color != self.color:
            return True
        
        return False

class Rook(Piece):
    def is_valid_move(self, start, end, board):
        sx, sy = start
        ex, ey = end
        
        if sx != ex and sy != ey:
            return False  # Rook moves only straight
        
        # Check if the path is clear
        step_x = 0 if sx == ex else (1 if ex > sx else -1)
        step_y = 0 if sy == ey else (1 if ey > sy else -1)
        x, y = sx + step_x, sy + step_y
        
        while (x, y) != (ex, ey):
            if board[x][y] is not None:
                return False
            x, y = x + step_x, y + step_y
        
        return True

