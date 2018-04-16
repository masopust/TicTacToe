try:
    import TicTacToe.Common.commonVariables as common
    import TicTacToe.square as square
    import TicTacToe.clickManager as clickManager
    import TicTacToe.endValidator as endValidator
    import TicTacToe.field as playingField
except ModuleNotFoundError:
    import Common.common
    import square
    import field as playingField
    import clickManager
    import endValidator

def main():
    common.tk.title(common.GAME_NAME)
    position = calculate_center()
    common.tk.geometry("+{}+{}".format(position[0], position[1]))

    field = playingField.Field()
    validator = endValidator.EndValidator(field)
    clickManager.ClickManager(field, validator)

    common.tk.mainloop()

def calculate_center():
    dimensions = common.FIELD_SIZE
    positionRight = int(common.tk.winfo_screenwidth() / 2 - (dimensions + common.INFO_SIZE) / 2)
    positionDown = int(common.tk.winfo_screenheight() / 2 - dimensions / 2 - 50)
    return [positionRight, positionDown]