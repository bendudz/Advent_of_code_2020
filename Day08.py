# --- Day 8: Handheld Halting ---
import operator
from typing import List, Tuple

ops = {'+': operator.add, '-': operator.sub}


def do_work(instructions: List[List[str]], part: int) -> int:
    if part == 1:
        return part1(instructions)[0]
    else:
        return part2(instructions)


def part1(instructions: List[List[str]]) -> Tuple[int, bool]:
    visited = [False] * len(instructions)
    accumulator = 0
    pos = 0
    while pos < len(instructions) and not visited[pos]:
        visited[pos] = True
        op, arg = instructions[pos]
        oper, num = arg[:1], int(arg[1:])
        if op == "acc":
            accumulator = ops.get(oper)(accumulator, num)
            pos += 1
        elif op == "jmp":
            pos = ops.get(oper)(pos, num)
        else:
            pos += 1
    return accumulator, pos == len(instructions)


def part2(instructions: List[List[str]]) -> int:
    for pos, (op, _) in enumerate(instructions):
        if op in ('nop', 'jmp'):
            instructions[pos][0] = 'jmp' if op == 'nop' else 'nop'
            accumulator, done = part1(instructions)
            # restore the original instruction
            instructions[pos][0] = op
            if done:
                return accumulator


def driver(file: str, part: int) -> int:
    puzzle_input = ''.join(list(open(f'resources/{file}')))
    instructions = [p.split() for p in puzzle_input.strip().split('\n')]
    return do_work(instructions, part)


def solve_pt1a():
    return driver("D08P01a.txt", 1)


def solve_pt1b():
    return driver("D08P01b.txt", 1)


def solve_pt2a():
    return driver("D08P01c.txt", 2)


def solve_pt2b():
    return driver("D08P01b.txt", 2)


print(f"Day 8 Part 1a Answer: {solve_pt1a()}")
print(f"Day 8 Part 1b Answer: {solve_pt1b()}")
print(f"Day 8 Part 2a Answer: {solve_pt2a()}")
print(f"Day 8 Part 2b Answer: {solve_pt2b()}")

# Day 8 Part 1a Answer: 5
# Day 8 Part 1b Answer: 1818
# Day 8 Part 2a Answer: 8
# Day 8 Part 2b Answer: 631
