try:
    from TicTacToe import endValidator
    from TicTacToe import common
except FileNotFoundError:
    import endValidator
    import common

class Bot():
    def __init__(self, field):
        self.field = field
        self.grid = self.field.grid
        self.endValidator = endValidator.EndValidator(self.field)

    def get_empty_squares(self):
        list = []
        for x in range(common.NUMBER_OF_COLUMNS):
            for y in range(common.NUMBER_OF_COLUMNS):
                if self.grid[x][y].status is None:
                    list.append(self.grid[x][y])
        return list

    def check_end(self, x, y, lastPlayer):
        return self.endValidator.win(x, y, lastPlayer)

    def miniMax(self):
        empty = self.get_empty_squares()
        for x in range(common.NUMBER_OF_COLUMNS):
            resultOne = self.check_end(x, common.NUMBER_OF_COLUMNS - x - 1, True)
            resultTwo = self.check_end(x, common.NUMBER_OF_COLUMNS - x - 1, False)
            if resultOne:
                return -1  # human win
            if resultTwo:
                return 1
            if len(empty) == common.NUMBER_OF_COLUMNS ** 2:
                return 0