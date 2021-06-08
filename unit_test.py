# ----------unittest.py-----------
# Beau McCartney
# June 2021

import unittest
import Sudoku

class TestHelperMethods(unittest.TestCase):

    def test_placecheck_false(self):
        fhand = open('lib/puzzle1.txt', 'r')
        testboard = Sudoku.init_board(fhand)
        self.assertFalse(Sudoku.check_if_placeable(testboard, 1, 0, 0))

    def test_placecheck_true(self):
        fhand = open('lib/puzzle1.txt', 'r')
        testboard = Sudoku.init_board(fhand)
        self.assertTrue(Sudoku.check_if_placeable(testboard, 4, 0, 0))

    def test_placecheck_true_on_assigned_square(self):
        fhand = open('lib/puzzle1.txt', 'r')
        testboard = Sudoku.init_board(fhand)
        testboard[0][0] = 4
        print("\nPlacecheck assigned true board:")
        Sudoku.print_board(testboard)
        self.assertTrue(Sudoku.check_if_placeable(testboard, 4, 0, 0))

    def test_placecheck_false_on_assigned_square(self):
        fhand = open('lib/puzzle1.txt', 'r')
        testboard = Sudoku.init_board(fhand)
        testboard[0][0] = 1
        print("\nPlacecheck assigned true board:")
        Sudoku.print_board(testboard)
        self.assertFalse(Sudoku.check_if_placeable(testboard, 1, 0, 0))

    def test_count_remaining(self):
        fhand = open('lib/puzzle1.txt', 'r')
        testboard = Sudoku.init_board(fhand)
        self.assertEqual(49, Sudoku.count_remaining(testboard))

    def test_check_valid_true(self):
        fhand = open('lib/puzzle1.txt', 'r')
        testboard = Sudoku.init_board(fhand)
        self.assertTrue(Sudoku.check_valid(testboard))

    def test_check_valid_false(self):
        fhand = open('lib/puzzle1.txt', 'r')
        testboard = Sudoku.init_board(fhand)
        testboard[0][0] = 1
        self.assertFalse(Sudoku.check_valid(testboard))

if __name__ == "__main__":
    unittest.main()
