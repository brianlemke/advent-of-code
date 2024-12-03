#!/usr/bin/env python3

import unittest
import day2 as solution

class TestSolution(unittest.TestCase):
    sample_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".splitlines(keepends = True)

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 2

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 4

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input))

if __name__ == '__main__':
    unittest.main()