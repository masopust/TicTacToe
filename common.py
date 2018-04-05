import tkinter

GAME_NAME = "Tic Tac Toe"
FIELD_SIZE = 400
NUMBER_OF_COLUMNS = 3
X_PADDING = 20
LINE_WIDTH = 10
CROSS_COLOR = "red"
CIRCLE_COLOR = "blue"
BACKGROUND_COLOR = "white"
PLAYER_TURN = True  # circle start

tk = tkinter.Tk()
canvas = tkinter.Canvas(bg=BACKGROUND_COLOR)
both = tkinter.BOTH
frame = tkinter.Frame()