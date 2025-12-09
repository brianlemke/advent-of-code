#!/usr/bin/env python3

# https://adventofcode.com/2024/day/8

import argparse
import math
from queue import PriorityQueue

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2025_day8.txt')

class Circuit:
    def __init__(self, boxes:list[tuple[int,int,int]]=[]):
        self.boxes:set[tuple[int,int,int]] = set(boxes)
    
    def has_box(self, box:tuple[int,int,int]):
        return box in self.boxes
    
    def circuit_size(self):
        return len(self.boxes)

    def add_box(self, box:tuple[int,int,int]):
        self.boxes.add(box)
    
    def merge_circuits(self, other:list['Circuit']):
        self.boxes = self.boxes.union(*[c.boxes for c in other])

    def can_merge(self, other:'Circuit'):
        return len(self.boxes.intersection(other.boxes))
    
def distance(a:tuple[int,int,int], b:tuple[int,int,int]):
    return math.sqrt(
        abs(a[0] - b[0]) ** 2 +
        abs(a[1] - b[1]) ** 2 +
        abs(a[2] - b[2]) ** 2
    )

def solve_a(inputfile, num_connections:int):
    """Read the file and return a solution for Part One"""
    boxes:list[tuple[int, int, int]] = [tuple([int(x) for x in row.strip().split(',')]) for row in inputfile]
    pq = PriorityQueue() # distance -> (index_a, index_b)
    for i in range(0, len(boxes)):
        for j in range(i+1, len(boxes)):
            pq.put((distance(boxes[i], boxes[j]), (i,j)), block=False)

    circuits:list[Circuit] = []
    
    # Pop off the first N pairs to connect
    for _ in range(0, num_connections):
        item = pq.get(block=False)
        a = boxes[item[1][0]]
        b = boxes[item[1][1]]
        new_circuit = Circuit([a,b])

        # Merge all circuits that can be joined with the new circuit
        intersections:list[int] = [i for i,c in enumerate(circuits) if new_circuit.can_merge(c)]
        new_circuit.merge_circuits([circuits[i] for i in intersections])
        circuits = [c for i,c in enumerate(circuits) if i not in intersections]
        circuits.append(new_circuit)

    # Now find the three biggest circuits
    circuits.sort(key=lambda c: c.circuit_size(), reverse=True)
    return circuits[0].circuit_size() * circuits[1].circuit_size() * circuits[2].circuit_size()

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    boxes:list[tuple[int, int, int]] = [tuple([int(x) for x in row.strip().split(',')]) for row in inputfile]
    pq = PriorityQueue() # distance -> (index_a, index_b)
    for i in range(0, len(boxes)):
        for j in range(i+1, len(boxes)):
            pq.put((distance(boxes[i], boxes[j]), (i,j)), block=False)

    circuits:list[Circuit] = []
    
    # Pop off pairs until we have a single circuit the size of the input
    while True:
        item = pq.get(block=False)
        a = boxes[item[1][0]]
        b = boxes[item[1][1]]
        new_circuit = Circuit([a,b])

        # Merge all circuits that can be joined with the new circuit
        intersections:list[int] = [i for i,c in enumerate(circuits) if new_circuit.can_merge(c)]
        new_circuit.merge_circuits([circuits[i] for i in intersections])
        circuits = [c for i,c in enumerate(circuits) if i not in intersections]
        circuits.append(new_circuit)

        # Check if we are done
        if len(circuits) == 1 and circuits[0].circuit_size() == len(boxes):
            return a[0] * b[0]

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile), 1000)
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
