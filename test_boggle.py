import unittest
import boggle
from string import ascii_uppercase

class TestBoggle(unittest.TestCase):
    def test_can_create_an_empty_grid(self):
        grid = boggle.make_grid(0, 0)
        self.assertEqual(len(grid), 0, "A grid with no rows or cols has no items" )
    
    def test_grid_size_is_width_times_height(self):
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)

    def test_grid_coordinates(self):
        grid = boggle.make_grid(2, 2)
        self.assertTrue((0,0) in grid)
        self.assertTrue((0,1) in grid)
        self.assertTrue((1,0) in grid)
        self.assertTrue((1,1) in grid)
        self.assertTrue((2,2) not in grid)

    def test_grid_is_filled_with_letters(self):
        grid = boggle.make_grid(2, 3)
        for L in grid.values():
            self.assertTrue(L in ascii_uppercase)

    def test_neighbours_of_position(self):
        neighbours = boggle.neighbours_of_position(1, 2)
        self.assertTrue((0,1) in neighbours)
        self.assertTrue((0,2) in neighbours)
        self.assertTrue((0,3) in neighbours)
        self.assertTrue((1,1) in neighbours)
        self.assertTrue((1,3) in neighbours)
        self.assertTrue((2,1) in neighbours)
        self.assertTrue((2,2) in neighbours)
        self.assertTrue((2,3) in neighbours)
    
    def test_all_grid_neighbours(self):
        grid = boggle.make_grid(2, 2)
        neighbours = boggle.all_grid_neighbours(grid)
        self.assertEqual(len(neighbours), len(grid))
        for pos in grid:
            others = list(grid) #creates a new list from the dictionaries key
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))
    
    def test_converting_to_path_to_a_word(self):
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
        twoLetterWord = noggle.path_to_word(grid, [(0, 0), (1, 1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])


if __name__ == '__main__':
    unittest.main()

