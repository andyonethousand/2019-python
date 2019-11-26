import collections

# No board needed because all moves are valid in to empty spaces

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.rows = collections.defaultdict(int)
        self.cols = collections.defaultdict(int)
        self.diags = collections.defaultdict(int)
        
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        
        self.rows[(row, player)] += 1
        if self.rows[(row, player)] == self.size:
            return player
        
        self.cols[(col, player)] += 1
        if self.cols[(col, player)] == self.size:
            return player
        
        if row == col:
            self.diags[('#', player)] += 1
            if self.diags[('#', player)] == self.size:
                return player
                        
        if row == self.size - 1 - col:
            self.diags[('*', player)] += 1
            if self.diags[('*', player)] == self.size:
                return player
        
        return 0
