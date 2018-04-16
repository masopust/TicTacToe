try:
    import TicTacToe.Common.commonVariables as common
    import TicTacToe.Common.commonFunctions as commonFunctions
    import TicTacToe.square as square
except ModuleNotFoundError:
    import Common.common
    import square
    import Common.commonFunctions


class Field:
    def __init__(self):
        self.canvas = common.canvas
        self.frame = common.frame
        common.tk.geometry(str(common.FIELD_SIZE + common.INFO_SIZE) + "x" + str(common.FIELD_SIZE))  # dimensions
        common.tk.resizable(0, 0)  # Don't allow resizing in the x or y direction

        self.var = common.tkinter.IntVar()
        self.entryText = common.tkinter.StringVar()
        self.whoseTurnCanvas = common.tkinter.Canvas(self.frame, bg=common.INFO_BACKGROUND)
        self.grid = []

        self.initialize_frame()
        self.draw_lines()
        self.initialize_field()

    def initialize_frame(self):
        self.frame.place(x=common.FIELD_SIZE, y=0)
        self.frame.config(background=common.INFO_BACKGROUND)
        common.tkinter.Label(self.frame, text="TIC TAC TOE", font=("Helvetica", 20)).pack()
        common.tkinter.Label(self.frame, text="Mode:", font=("Helvetica", 10)).pack(pady=30)

        self.initialize_radioBox()

        common.tkinter.Label(self.frame, text="Size of the field (3-5): ", font=("Helvetica", 10)).pack(pady=30)
        common.tkinter.Entry(self.frame, text=self.entryText, justify="center", width=5).pack(pady=5)
        self.entryText.set("3")

        common.tkinter.Button(self.frame, text="RESET", command=self.reset, padx=20).pack(pady=10)
        self.whoseTurnCanvas.pack()
        self.draw_info_circle()
        self.frame.pack_propagate(False)

    def initialize_radioBox(self):
        # one player is disabled for now
        c1 = common.tkinter.Radiobutton(self.frame, text="One Player", variable=self.var, value=1, command=self.reset)
        c1.pack()
        c2 = common.tkinter.Radiobutton(self.frame, text="Two Players", variable=self.var, value=2, command=self.reset)
        c2.select()
        c2.pack()

    def reset(self):
        common.MOVE_COUNTER = 0
        if commonFunctions.validate_numbers(self.entryText.get()):
            new_number_of_columns = int(self.entryText.get())
        else:
            new_number_of_columns = 3
            self.entryText.set(3)
        if 2 < new_number_of_columns < 6:
            common.NUMBER_OF_COLUMNS = new_number_of_columns
        else:
            self.entryText.set(3)
        self.grid = []
        self.initialize_field()
        self.canvas.delete("all")
        self.draw_lines()

    def draw_lines(self):
        for x in range(common.NUMBER_OF_COLUMNS):
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

    def clear_info(self):
        self.whoseTurnCanvas.delete("all")

    def draw_info_circle(self):
        self.clear_info()
        self.whoseTurnCanvas.create_oval(100, 30, 200, 130,
                                         fill=common.INFO_BACKGROUND, outline=common.CIRCLE_COLOR, width=common.LINE_WIDTH)
        self.whoseTurnCanvas.pack(fill=common.both, expand=1)

    def draw_info_cross(self):
        self.clear_info()
        self.whoseTurnCanvas.create_line(100, 30, 200, 130,
                                         fill=common.CROSS_COLOR, width=common.LINE_WIDTH)
        self.whoseTurnCanvas.create_line(100, 130, 200, 30,
                                         fill=common.CROSS_COLOR, width=common.LINE_WIDTH)
        self.whoseTurnCanvas.pack(fill=common.both, expand=1)