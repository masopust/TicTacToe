try:
    import TicTacToe.field as field
    import TicTacToe.common as common
except FileNotFoundError:
    import field
    import common

from random import randint

class Bot:
    def __init__(self, field, validator):
        self.field = field
        self.validator = validator

    def bot_on(self):
        return int(self.field.var.get()) == 1  # it means that the mode is single player

    def get_empty_spots(self):
        grid = self.field.grid
        fields = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x].status is None:
                    fields.append((x, y))
        return fields

    def play(self):
        empty = self.get_empty_spots()
        if len(empty) == 0:
            if self.validator.contunioation("Draw!\n"):
                self.play()
                return
        num = randint(0, len(empty) - 1)
        x = empty[num][0]
        y = empty[num][1]
        if not common.PLAYER_TURN:
            self.field.draw_info_circle()
            self.field.draw_cross(y, x)
        else:
            self.field.draw_info_cross()
            self.field.draw_circle(y, x)
