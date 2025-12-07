#!/usr/bin/env python3

import unittest
import day6 as solution

class TestSolution(unittest.TestCase):
    sample_input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 4277556

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 3263827

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input))

if __name__ == '__main__':
    unittest.main()