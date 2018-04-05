import TicTacToe.common as common


class ClickManager():
    def __init__(self, field, validator):
        self.field = field
        self.validator = validator
        field.canvas.bind("<Button-1>", self.click)  # right click

    def click(self, event):
        for y in range(len(self.field.grid)):
            for x in range(len(self.field.grid[y])):
                square = self.field.grid[y][x]
                if square.click_inside(event.x, event.y):  # player clicked this square
                    if square.status is None:  # place is empty
                        if common.PLAYER_TURN:
                            self.field.draw_circle(y, x)
                        else:
                            self.field.draw_cross(y, x)
                        self.validator.end_validator(x, y, common.PLAYER_TURN)
                        self.switch_player()

    def switch_player(self):
        if common.PLAYER_TURN:
            common.PLAYER_TURN = False
        else:
            common.PLAYER_TURN = True
