import tkinter

# parameters
GAME_NAME = "Tic Tac Toe"
FIELD_SIZE = 500  # don't change
NUMBER_OF_COLUMNS = 3
INFO_SIZE = 300
X_PADDING = 20  # distance between the line and the X
LINE_WIDTH = 10  # of X or O
CROSS_COLOR = "red"
CIRCLE_COLOR = "blue"
BACKGROUND_COLOR = "grey"
INFO_BACKGROUND = "white"


# global variables.. changing!!
PLAYER_TURN = True  # circle start the game
MOVE_COUNTER = 0


# common
tk = tkinter.Tk()
canvas = tkinter.Canvas(bg=BACKGROUND_COLOR)
both = tkinter.BOTH
frame = tkinter.Frame(tk, width=INFO_SIZE, height=FIELD_SIZE)
tkinter = tkinter
