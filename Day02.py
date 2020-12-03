# --- Day 2: Password Philosophy ---
from typing import List

from utils import read_file


def do_work(password_table: List[str], puzzle_part: int):
    if puzzle_part == 1:
        return list(filter(lambda p: validator_pt1(p), password_table))
    return list(filter(lambda p: validator_pt2(p), password_table))


def validator_pt1(password_entry):
    policy, letter, password = password_entry.split(' ')
    min, max = policy.split('-')
    count = password.count(letter[0])
    if int(min) <= count <= int(max):
        return True
    return False


def validator_pt2(password_entry):
    policy, letter, password = password_entry.split(' ')
    min, max = policy.split('-')
    count = 0
    if letter[0] == password[int(min) - 1]:
        count += 1
    if letter[0] == password[int(max) - 1]:
        count += 1
    return True if count == 1 else False


def driver(file: str, puzzle_part):
    file = read_file(file)
    inputs = [v for v in file]
    return len(do_work(inputs, puzzle_part))


def solve_pt1a():
    return driver("D02P01.txt", 1)


def solve_pt1b():
    return driver("D02P02.txt", 1)


def solve_pt2a():
    return driver("D02P01.txt", 2)


def solve_pt2b():
    return driver("D02P02.txt", 2)


print(f"Day 2 Part 1a Answer: {solve_pt1a()}")
print(f"Day 2 Part 1b Answer: {solve_pt1b()}")
print(f"Day 2 Part 2a Answer: {solve_pt2a()}")
print(f"Day 2 Part 2b Answer: {solve_pt2b()}")

# Day 2 Part 1a Answer: 2
# Day 2 Part 1b Answer: 569
# Day 2 Part 2a Answer: 1
# Day 2 Part 2b Answer: 346
