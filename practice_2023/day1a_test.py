#!/usr/bin/env python3

import unittest
import day1a as solution

class TestSolution(unittest.TestCase):
    sample_solution = 142
    sample_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines(keepends = True)

    def test_sample_input(self):
        """Make sure the sample solution works"""

        self.assertEqual(self.sample_solution, solution.solve(self.sample_input))

if __name__ == '__main__':
    unittest.main()