# --- Day 9: Encoding Error ---
from typing import List, Tuple

from utils import read_file


def do_work(puzzle_input: List[int], preamble: int, part: int) -> int:
    if part == 1:
        return xmas_validator(puzzle_input, preamble)
    else:
        return part2(puzzle_input, preamble)


def xmas_validator(values: List[int], preamble: int) -> int:
    pos = preamble
    is_valid = True
    val = 0
    while pos < len(values) and is_valid:
        # cut list to len preamble
        pairs_list = values[pos - preamble:pos]
        val = values[pos]
        # get all unique pairs
        pairs = [(pairs_list[v1], pairs_list[v2]) for v1 in range(len(pairs_list)) for v2 in
                 range(v1 + 1, len(pairs_list))]
        for pair in pairs:
            is_valid = validate_pair(pair, val)
            if is_valid:
                break
        pos += 1
    return val


def validate_pair(pair: Tuple[int, int], value: int) -> bool:
    if sum(pair) == value:
        return True
    return False


def part2(values: List[int], preamble: int) -> int:
    invalid_num = xmas_validator(values, preamble)
    found = False
    pos = 0
    end = 0
    while pos < len(values) and not found:
        for n in range(len(values)):
            calc = sum(values[pos:pos + n + 1])
            if calc == invalid_num:
                found = True
                end = pos + n + 1
                break
            elif calc > invalid_num:
                break
        pos += 1
    cont_nums = values[pos - 1:end]
    return max(cont_nums) + min(cont_nums)


def driver(file: str, preamble: int, part: int) -> int:
    file = read_file(file)
    puzzle_input = [int(v) for v in file]
    return do_work(puzzle_input, preamble, part)


def solve_pt1a():
    return driver("D09P01a.txt", 5, 1)


def solve_pt1b():
    return driver("D09P01b.txt", 25, 1)


def solve_pt2a():
    return driver("D09P01a.txt", 5, 2)


def solve_pt2b():
    return driver("D09P01b.txt", 25, 2)


print(f"Day 9 Part 1a Answer: {solve_pt1a()}")
print(f"Day 9 Part 1b Answer: {solve_pt1b()}")
print(f"Day 9 Part 2a Answer: {solve_pt2a()}")
print(f"Day 9 Part 2b Answer: {solve_pt2b()}")

# Day 9 Part 1a Answer: 127
# Day 9 Part 1b Answer: 731031916
# Day 9 Part 2a Answer: 62
# Day 9 Part 2b Answer: 93396727
