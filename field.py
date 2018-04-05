import TicTacToe.common as common
import TicTacToe.square as square


class Field:
    def __init__(self):
        self.canvas = common.canvas
        common.tk.geometry(str(common.FIELD_SIZE) + "x" + str(common.FIELD_SIZE))  # dimensions
        common.tk.resizable(0, 0)  # Don't allow resizing in the x or y direction
        self.grid = []

        self.draw_lines()
        self.initialize_field()

    def reset(self):
        self.grid = []
        self.initialize_field()
        self.canvas.delete("all")
        self.draw_lines()

    def draw_lines(self):
        for x in range(common.NUMBER_OF_COLUMNS - 1):  # there is always one line less than columns
            padding = (x + 1) * (common.FIELD_SIZE / common.NUMBER_OF_COLUMNS)  # + 1 is to avoid zero
            self.canvas.create_line(padding, 0, padding, common.FIELD_SIZE)  # vertical line
            self.canvas.create_line(0, padding, common.FIELD_SIZE, padding)  # horizontal line
            self.canvas.pack(fill=common.both, expand=1)

    def initialize_field(self):  # the field consist of 9 "little" fields (squares)
        for y in range(common.NUMBER_OF_COLUMNS):
            self.grid.append([])
            for x in range(common.NUMBER_OF_COLUMNS):
                xPos = x * (common.FIELD_SIZE / common.NUMBER_OF_COLUMNS)
                yPos = y * (common.FIELD_SIZE / common.NUMBER_OF_COLUMNS)
                padd = common.FIELD_SIZE / common.NUMBER_OF_COLUMNS
                self.grid[y].append(square.Square(xPos, yPos, padd))

    def draw_cross(self, x, y):
        square = self.grid[x][y]
        self.canvas.create_line(square.leftX + square.xPadding, square.bottomY - square.xPadding,  # B to T line
                                square.rightX - square.xPadding, square.topY + square.xPadding,
                                fill=common.CROSS_COLOR, width=common.LINE_WIDTH)
        self.canvas.create_line(square.leftX + square.xPadding, square.topY + square.xPadding,  # T to B line
                                square.rightX - square.xPadding, square.bottomY - square.xPadding,
                                fill=common.CROSS_COLOR, width=common.LINE_WIDTH)
        self.canvas.pack(fill=common.both, expand=1)
        square.set_status(False)

    def draw_circle(self, x, y):
        square = self.grid[x][y]
        pad = square.xPadding
        self.canvas.create_oval(square.leftX + pad, square.bottomY - pad, square.rightX - pad, square.topY + pad,
                                fill=common.BACKGROUND_COLOR, outline=common.CIRCLE_COLOR, width=common.LINE_WIDTH)
        self.canvas.pack(fill=common.both, expand=1)
        square.set_status(True)
