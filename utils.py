def print_board(board):
    """Prints the board in a readable format."""
    for row in board:
        print(' '.join([f'{p[0][0]}({p[1][0]})' if p else '--' for p in row]))
    print('\n')

def parse_move(move):
    """Convert chess notation (e.g., 'e2 e4') to board indices."""
    try:
        start, end = move.split()
        start = (8 - int(start[1]), ord(start[0]) - ord('a'))
        end = (8 - int(end[1]), ord(end[0]) - ord('a'))
        return start, end
    except Exception:
        return None

