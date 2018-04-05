try:
    import TicTacToe.common as common
except FileNotFoundError:
    import common
class Square:
    def __init__(self, x, y, padding):
        self.leftX = x
        self.rightX = x + padding
        self.topY = y
        self.bottomY = y + padding
        self.xPadding = common.X_PADDING
        self.status = None  # none - empty, true - circle, false - cross

    def click_inside(self, x, y):  # if the click is inside the square it will return true
        return self.leftX < x < self.rightX and self.topY < y < self.bottomY

    def set_status(self, stat):
        self.status = stat
