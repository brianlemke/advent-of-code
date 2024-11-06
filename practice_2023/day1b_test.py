#!/usr/bin/env python3

import unittest
import day1b as solution

class TestSolution(unittest.TestCase):
    sample_solution = 281
    sample_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines(keepends = True)

    def test_sample_input(self):
        """Make sure the sample solution works"""

        self.assertEqual(self.sample_solution, solution.solve(self.sample_input))

if __name__ == '__main__':
    unittest.main()