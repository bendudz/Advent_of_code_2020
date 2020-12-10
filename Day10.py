# --- Day 10: Adapter Array ---
from collections import Counter, defaultdict
from typing import List

from utils import read_file


def do_work(adapters: List[int], part: int) -> int:
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    sorted_list = sorted(adapters)

    if part == 1:
        return part1(sorted_list)
    else:
        return part2(sorted_list)


def part1(sorted_list: List[int]) -> int:
    diffs = [sorted_list[x + 1] - sorted_list[x] for x in range(len(sorted_list) - 1)]
    count_diffs = Counter(diffs)
    return count_diffs[1] * count_diffs[3]


def part2(sorted_list: List[int]) -> int:
    # Nice blog! https://skerritt.blog/dynamic-programming/
    ways = defaultdict(int, {0: 1})
    for i in range(len(sorted_list)):
        for j in range(1, 4):
            if sorted_list[i] - sorted_list[i - j] <= 3:
                ways[i] += ways[i - j]
    return max(ways.values())


def driver(file: str, part: int) -> int:
    file = read_file(file)
    puzzle_input = [int(v) for v in file]
    return do_work(puzzle_input, part)


def solve_pt1a():
    return driver("D010P01a.txt", 1)


def solve_pt1b():
    return driver("D010P01b.txt", 1)


def solve_pt1c():
    return driver("D010P01c.txt", 1)


def solve_pt2a():
    return driver("D010P01a.txt", 2)


def solve_pt2b():
    return driver("D010P01b.txt", 2)


def solve_pt2c():
    return driver("D010P01c.txt", 2)


print(f"Day 10 Part 1a Answer: {solve_pt1a()}")
print(f"Day 10 Part 1b Answer: {solve_pt1b()}")
print(f"Day 10 Part 1c Answer: {solve_pt1c()}")
print(f"Day 10 Part 2a Answer: {solve_pt2a()}")
print(f"Day 10 Part 2b Answer: {solve_pt2b()}")
print(f"Day 10 Part 2c Answer: {solve_pt2c()}")

# Day 10 Part 1a Answer: 35
# Day 10 Part 1b Answer: 220
# Day 10 Part 1c Answer: 2201
# Day 10 Part 2a Answer: 8
# Day 10 Part 2b Answer: 19208
# Day 10 Part 2c Answer: 169255295254528
