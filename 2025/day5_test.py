#!/usr/bin/env python3

import unittest
import day5 as solution

class TestSolution(unittest.TestCase):
    sample_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 3

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 14

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input))

if __name__ == '__main__':
    unittest.main()