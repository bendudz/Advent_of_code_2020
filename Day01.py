# --- Day 1: Report Repair ---

# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
#
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
#
# For example, suppose your expense report contained the following:
#
# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
#
# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
from utils import read_file
import itertools
import operator
from functools import reduce
from typing import List


def do_work(ledger_values: List[int], combo_qty: int) -> int:
    combos = list(itertools.combinations(ledger_values, combo_qty))
    multiple = ''
    for combo in combos:
        multiple = sum_combo(combo)
        if multiple is not None:
            break
    return multiple


def sum_combo(combo: tuple) -> int:
    if sum(combo) == 2020:
        return reduce(operator.mul, combo, 1)


def solve_pt1():
    input = read_file("D01P01.txt")
    amounts = [int(v) for v in input]
    return do_work(amounts, 2)


def solve_pt2():
    input = read_file("D01P02.txt")
    amounts = [int(v) for v in input]
    return do_work(amounts, 3)


print(f"Day 1 Part 1 Answer: {solve_pt1()}")
print(f"Day 1 Part 2 Answer: {solve_pt2()}")
