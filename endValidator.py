try:
    import TicTacToe.Common.commonVariables as common
except ModuleNotFoundError:
    import Common.common
import tkinter.messagebox
import sys


class EndValidator:
    def __init__(self, field):
        self.field = field

    def check_column(self, x, lastPlayer):
        for yLine in range(common.NUMBER_OF_COLUMNS):
            if self.field.grid[yLine][x].status != lastPlayer:
                return False
        return True

    def check_line(self, y, lastPlayer):
        for xLine in range(common.NUMBER_OF_COLUMNS):
            if self.field.grid[y][xLine].status != lastPlayer:
                return False
        return True

    def check_Ldiag(self, lastPlayer):
        for x in range(common.NUMBER_OF_COLUMNS):
            if self.field.grid[x][x].status != lastPlayer:
                return False
        return True

    def check_Ddiag(self, lastPlayer):
        for x in range(common.NUMBER_OF_COLUMNS):
            if self.field.grid[x][common.NUMBER_OF_COLUMNS - x - 1].status != lastPlayer:
                return False
        return True

    def check_diagonals(self, lastPlayer):
        if self.check_Ddiag(lastPlayer) or self.check_Ldiag(lastPlayer):
            return True
        return False

    def win(self, x, y, lastPlayer):
        return self.check_column(x, lastPlayer) or self.check_line(y, lastPlayer) or self.check_diagonals(lastPlayer)

    def draw(self):
        return common.MOVE_COUNTER == common.NUMBER_OF_COLUMNS ** 2  # every square is filed

    def end_validator(self, x, y, lastPlayer):
        if self.win(x, y, lastPlayer):
            text = "Player 2 wins!\n"
            if lastPlayer:
                text = "Player 1 wins!\n"
            self.contunioation(text)
            return True
        if self.draw():
            self.contunioation("Draw!\n")
            return True
        return False

    def contunioation(self, text):
        continueGame = tkinter.messagebox.askyesno("The end", text + "Do you want to continue playing?")
        if not continueGame:
            sys.exit(0)
        else:
            self.field.reset()
            return True
