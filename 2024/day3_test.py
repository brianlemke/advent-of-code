#!/usr/bin/env python3

import unittest
import day3 as solution

class TestSolution(unittest.TestCase):
    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
        sample_solution = 161

        self.assertEqual(sample_solution, solution.solve_a(sample_input))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
        sample_solution = 48

        self.assertEqual(sample_solution, solution.solve_b(sample_input))

if __name__ == '__main__':
    unittest.main()