#!/usr/bin/env python3

import unittest
import day4 as solution

class TestSolution(unittest.TestCase):
    # I verified that the input is always square, same number of columns as lines
    sample_input ="""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines(keepends = True)

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 18

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 9

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input))

if __name__ == '__main__':
    unittest.main()