import TicTacToe.common as common
import TicTacToe.field as fi
import TicTacToe.clickManager as clickManager
import TicTacToe.endValidator as endValidator


def main():
    common.tk.title(common.GAME_NAME)

    field = fi.Field()
    validator = endValidator.EndValidator(field)
    clickManager.ClickManager(field, validator)

    common.tk.mainloop()
