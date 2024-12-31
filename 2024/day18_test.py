#!/usr/bin/env python3

import unittest
import day18 as solution

class TestSolution(unittest.TestCase):
    sample_input = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 22

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input, size=7, bytes=12))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = '6,1'

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input, size=7, bytes=12))

if __name__ == '__main__':
    unittest.main()