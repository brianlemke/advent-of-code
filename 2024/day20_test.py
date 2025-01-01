#!/usr/bin/env python3

import unittest
import day20 as solution

class TestSolution(unittest.TestCase):
    sample_input = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        self.assertEqual(5, solution.solve_a(self.sample_input, timesave=16))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = None

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input))

if __name__ == '__main__':
    unittest.main()