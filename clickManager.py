try:
    import TicTacToe.Common.commonVariables as common
    import TicTacToe.bot as bot
except ModuleNotFoundError:
    import Common.commonVariables as common
    import bot


class ClickManager():
    def __init__(self, field, validator):
        self.field = field
        self.validator = validator
        self.bot = bot.Bot(self.field, self.validator)
        field.canvas.bind("<Button-1>", self.click)  # right click

    def click(self, event):
        for y in range(len(self.field.grid)):
            for x in range(len(self.field.grid[y])):
                square = self.field.grid[y][x]
                if square.click_inside(event.x, event.y):  # player clicked this square
                    if square.status is None:  # place is empty
                        self.handle_drawing(x, y)
                        if not self.switch_turns(x, y):
                            break

    def switch_turns(self, x, y):
        restart = self.validator.end_validator(x, y, common.PLAYER_TURN)
        self.switch_player()
        if restart:
            return False
        return True

    def handle_drawing(self, x, y):
        if common.PLAYER_TURN:
            self.field.draw_info_cross()
            self.field.draw_circle(y, x)
        else:
            self.field.draw_info_circle()
            self.field.draw_cross(y, x)
        if self.bot.bot_on() and self.switch_turns(x, y):
            self.bot.play()
        common.MOVE_COUNTER += 1

    def switch_player(self):
        if common.PLAYER_TURN:
            common.PLAYER_TURN = False
        else:
            common.PLAYER_TURN = True