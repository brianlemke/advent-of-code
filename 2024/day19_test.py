#!/usr/bin/env python3

import unittest
import day19 as solution

class TestSolution(unittest.TestCase):
    sample_input = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 6

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 16

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input))

if __name__ == '__main__':
    unittest.main()