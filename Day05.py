# --- Day 5: Binary Boarding ---
from typing import List

from utils import read_file


def do_work(boarding_passes: List[str]):
    seat_ids = []
    for pass_ in boarding_passes:
        seat_ids.append(boarding_pass_to_decimal(pass_))
    return seat_ids


def boarding_pass_to_decimal(boarding_pass: str):
    converted_pass = boarding_pass.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
    return int(converted_pass, 2)


def missing_elements(elements: List) -> List[int]:
    all_seats = sorted(list(map(int, elements)))
    return sorted(set(range(all_seats[0], all_seats[-1] + 1)).difference(elements))


def driver(file: str, part: int):
    puzzle_input = read_file(file)
    passes = [v for v in puzzle_input]
    if part == 1:
        return max(do_work(passes))
    else:
        return missing_elements(do_work(passes))


def solve_pt1a():
    return do_work(["BFFFBBFRRR"])[0]


def solve_pt1b():
    return do_work(["FFFBBBFRRR"])[0]


def solve_pt1c():
    return do_work(["BBFFBBFRLL"])[0]


def solve_pt1d():
    return driver("D05P01.txt", 1)


def solve_pt2a():
    return sorted(driver("D05P01.txt", 2))[0]


print(f"Day 5 Part 1a Answer: {solve_pt1a()}")
print(f"Day 5 Part 1b Answer: {solve_pt1b()}")
print(f"Day 5 Part 1c Answer: {solve_pt1c()}")
print(f"Day 5 Part 1d Answer: {solve_pt1d()}")
print(f"Day 5 Part 2a Answer: {solve_pt2a()}")

# Day 5 Part 1a Answer: 567
# Day 5 Part 1b Answer: 119
# Day 5 Part 1c Answer: 820
# Day 5 Part 1d Answer: 911
# Day 5 Part 2a Answer: 629
