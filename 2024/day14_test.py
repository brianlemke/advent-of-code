#!/usr/bin/env python3

import unittest
import day14 as solution

class TestSolution(unittest.TestCase):
    sample_input = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 12

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input, width=11, height=7))

if __name__ == '__main__':
    unittest.main()