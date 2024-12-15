#!/usr/bin/env python3

import unittest
import day11 as solution

class TestSolution(unittest.TestCase):
    sample_input = """
125 17
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 55312

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 55312

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input, 25))

if __name__ == '__main__':
    unittest.main()