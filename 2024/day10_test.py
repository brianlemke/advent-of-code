#!/usr/bin/env python3

import unittest
import day10 as solution

class TestSolution(unittest.TestCase):
    sample_input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 36

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 81

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input))

if __name__ == '__main__':
    unittest.main()