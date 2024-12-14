#!/usr/bin/env python3

import unittest
import day9 as solution

class TestSolution(unittest.TestCase):
    sample_input = """
2333133121414131402
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 1928

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 2858

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input))

if __name__ == '__main__':
    unittest.main()