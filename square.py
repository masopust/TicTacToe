try:
    import TicTacToe.Common.commonVariables as common
    import TicTacToe.Common.commonFunctions as commonFunctions
except ModuleNotFoundError:
    import Common.commonVariables as common
    import Common.commonFunctions


class Square:
    def __init__(self, x, y, padding):
        if not commonFunctions.validate_numbers([x, y, padding]):
            raise ValueError
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