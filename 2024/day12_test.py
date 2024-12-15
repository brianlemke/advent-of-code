#!/usr/bin/env python3

import unittest
import day12 as solution

class TestSolution(unittest.TestCase):
    sample_input_a = """
AAAA
BBCD
BBCC
EEEC
""".splitlines(keepends = True)[1:]
    
    sample_input_b = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
""".splitlines(keepends = True)[1:]
    
    sample_input = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".splitlines(keepends = True)[1:]
    
    def test_part_one_a(self):
        self.assertEqual(140, solution.solve_a(self.sample_input_a))

    def test_part_one_b(self):
        self.assertEqual(772, solution.solve_a(self.sample_input_b))

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = 1930

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input))

    def test_part_two_a(self):
        self.assertEqual(80, solution.solve_b(self.sample_input_a))
        
    def test_part_two_b(self):
        self.assertEqual(436, solution.solve_b(self.sample_input_b))

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 1206

        self.assertEqual(sample_solution, solution.solve_b(self.sample_input))

if __name__ == '__main__':
    unittest.main()