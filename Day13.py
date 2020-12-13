# --- Day 13: Shuttle Search ---
import math
from itertools import count
from typing import List, Dict

from utils import read_file


def do_work(notes: List[str], part: int):
    if part == 1:
        timestamp = int(notes[0])
        routes = list(map(int, filter(lambda x: x != 'x', notes[1].split(','))))
        return part1(timestamp, routes)
    else:
        routes = {}
        for iter, x in enumerate(notes[1].split(',')):
            if x != 'x':
                routes[int(x)] = iter
        return part2(routes)


def part1(timestamp: int, routes: List[int]):
    closest = {}
    for route in routes:
        calc = timestamp / route
        ceil = (math.ceil(calc) * route) - timestamp
        floor = (math.floor(calc) * route) - timestamp
        val = floor if 0 <= floor < ceil else ceil
        closest[route] = val
    lowest = min(closest.values())
    for route, val in closest.items():
        if val == lowest:
            return route * val


def part2(routes: Dict) -> int:
    idx = 0
    step = 1
    for route, place in routes.items():
        for t in count(idx, step):
            if not (t + place) % route:
                idx = t
                step *= route
                break
    return t


def driver(file: str, part: int):
    puzzle_input = read_file(file)
    notes = [v for v in puzzle_input]
    return do_work(notes, part)


def solve_pt1a():
    return driver('D013P01a.txt', 1)


def solve_pt1b():
    return driver('D013P01b.txt', 1)


def solve_pt2a():
    return driver('D013P01a.txt', 2)


def solve_pt2b():
    return driver('D013P01b.txt', 2)


print(f"Day 13 Part 1a Answer: {solve_pt1a()}")
print(f"Day 13 Part 1b Answer: {solve_pt1b()}")
print(f"Day 13 Part 2a Answer: {solve_pt2a()}")
print(f"Day 13 Part 2b Answer: {solve_pt2b()}")
