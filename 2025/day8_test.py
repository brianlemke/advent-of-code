#!/usr/bin/env python3

import unittest
import day8 as solution

class TestSolution(unittest.TestCase):
    sample_input = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 40

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input, 10))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 25272

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input))

if __name__ == '__main__':
    unittest.main()