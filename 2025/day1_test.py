#!/usr/bin/env python3

import unittest
import day1 as solution

class TestSolution(unittest.TestCase):
    sample_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 3

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 6

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input))

if __name__ == '__main__':
    unittest.main()