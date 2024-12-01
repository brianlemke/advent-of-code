#!/usr/bin/env python3

import unittest
import day1b as solution

class TestSolution(unittest.TestCase):
    sample_solution = 31
    sample_input = """3   4
4   3
2   5
1   3
3   9
3   3""".splitlines(keepends = True)

    def test_sample_input(self):
        """Make sure the sample solution works"""

        self.assertEqual(self.sample_solution, solution.solve(self.sample_input))

if __name__ == '__main__':
    unittest.main()