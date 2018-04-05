import TicTacToe.common as common
import tkinter.messagebox
import sys


class EndValidator:
    def __init__(self, field):
        self.field = field
        self.grid = field.grid

    def check_column(self, x, lastPlayer):
        for yLine in range(common.NUMBER_OF_COLUMNS):
            if self.grid[yLine][x].status != lastPlayer:
                return False
        return True

    def check_line(self, y, lastPlayer):
        for xLine in range(common.NUMBER_OF_COLUMNS):
            if self.grid[y][xLine].status != lastPlayer:
                return False
        return True

    def check_Ldiag(self, lastPlayer):
        for x in range(common.NUMBER_OF_COLUMNS):
            if self.grid[x][x].status != lastPlayer:
                return False
        return True

    def check_Ddiag(self, lastPlayer):
        for x in range(common.NUMBER_OF_COLUMNS):
            if self.grid[x][common.NUMBER_OF_COLUMNS - x - 1].status != lastPlayer:
                return False
        return True

    def check_diagonals(self, lastPlayer):
        if self.check_Ddiag(lastPlayer) or self.check_Ldiag(lastPlayer):
            return True
        return False

    def end_validator(self, x, y, lastPlayer):
        if self.check_column(x, lastPlayer) or self.check_line(y, lastPlayer) or self.check_diagonals(lastPlayer):
            text = "Player 2 wins!\n"
            if lastPlayer:
                text = "Player 1 wins!\n"
            result = tkinter.messagebox.askyesno("The end", text + "Do you want to continue playing?")
            if not result:
                sys.exit(0)
            else:
                print("reset")
                self.field.reset()

