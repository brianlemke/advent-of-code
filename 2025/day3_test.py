#!/usr/bin/env python3

import unittest
import day3 as solution

class TestSolution(unittest.TestCase):
    sample_input = """
987654321111111
811111111111119
234234234234278
818181911112111
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 357

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 3121910778619

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input))

if __name__ == '__main__':
    unittest.main()