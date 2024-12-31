#!/usr/bin/env python3

import unittest
import day17 as solution
from day17 import DebuggerOutput, Computer

class TestSolution(unittest.TestCase):
    sample_input = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".splitlines(keepends = True)[1:]

    def test_sample_a(self):
        """Make sure the sample solution works for part A"""
        sample_solution = '4,6,3,5,6,3,5,2,1,0'

        self.assertEqual(sample_solution, solution.solve_a(self.sample_input))
    
    def test_debugging_first(self):
        debugger = DebuggerOutput()
        debugger.c = 9
        pc = Computer(debugger)
        pc.process([2,6])
        self.assertEqual(1, pc.b)
    
    def test_debugging_second(self):
        debugger = DebuggerOutput()
        debugger.a = 10
        pc = Computer(debugger)
        pc.process([5,0,5,1,5,4])
        self.assertEqual('0,1,2', pc.pretty_output())
    
    def test_debugging_third(self):
        debugger = DebuggerOutput()
        debugger.a = 2024
        pc = Computer(debugger)
        pc.process([0,1,5,4,3,0])
        self.assertEqual('4,2,5,6,7,7,7,7,3,1,0', pc.pretty_output())
        self.assertEqual(0, pc.a)
    
    def test_debugging_fourth(self):
        debugger = DebuggerOutput()
        debugger.b = 29
        pc = Computer(debugger)
        pc.process([1,7])
        self.assertEqual(26, pc.b)
    
    def test_debugging_fifth(self):
        debugger = DebuggerOutput()
        debugger.b = 2024
        debugger.c = 43690
        pc = Computer(debugger)
        pc.process([4,0])
        self.assertEqual(44354, pc.b)

    def test_sample_b(self):
        """Make sure the sample solution works for part B"""
        sample_solution = 117440

        input = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0""".splitlines(keepends = True)[1:]

        self.assertEqual(sample_solution, solution.solve_b(input))

if __name__ == '__main__':
    unittest.main()