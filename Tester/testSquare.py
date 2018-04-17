import unittest
try:
    from TicTacToe import square
except ModuleNotFoundError:
    import square
    import field as playingField
    import endValidator
    import clickManager


class SquareTester(unittest.TestCase):

    def test_incorrect_creation(self):
        input_x = "wrong input"
        input_y = 1
        input_padding = 30
        self.assertRaises(ValueError, square.Square, input_x, input_y, input_padding)
        self.assertRaises(ValueError, square.Square, input_y, input_x, input_padding)
        self.assertRaises(ValueError, square.Square, input_x, input_y, input_x)

    def test_correct_creation(self):
        input_x = 1
        input_y = 1
        input_padding = 30
        square.Square(input_x, input_y, input_padding)
        self.assertTrue("Class creation successful!")

    def test_correct_inside_click(self):
        input_x = 1
        input_y = 1
        sq = square.Square(0, 0, 2)
        self.assertEqual(True, sq.click_inside(input_x, input_y))
        self.assertEqual(True, sq.click_inside(input_y, input_x))

    def test_correct_outside_click(self):
        input_x = 100
        input_y = 1
        sq = square.Square(0, 0, 2)
        self.assertEqual(False, sq.click_inside(input_x, input_y))
        self.assertEqual(False, sq.click_inside(input_y, input_x))

    def test_incorrect_click(self):
        input_x = "wrong_input"
        input_y = 1
        sq = square.Square(0, 0, 2)
        self.assertRaises(TypeError, sq.click_inside, input_x, input_y)
        self.assertRaises(TypeError, sq.click_inside, input_y, input_x)

    def test_correct_click_creation(self):
        input_field = playingField.Field()
        input_validator = endValidator.EndValidator(input_field)
        clickManager.ClickManager(input_field, input_validator)
        self.assertTrue("Class creation successful!")

    def test_incorrect_switch(self):
        input_x = "wrong_input"
        input_y = 1
        input_field = playingField.Field()
        input_validator = endValidator.EndValidator(input_field)
        cm = clickManager.ClickManager(input_field, input_validator)
        self.assertRaises(TypeError, cm.switch_turns, input_x, input_y)
        self.assertRaises(TypeError, cm.switch_turns, input_y, input_x)

if __name__ == "__main__":
    unittest.main()
