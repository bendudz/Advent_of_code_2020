# --- Day 7: Handy Haversacks ---
from typing import Dict

from utils import read_file


def do_work(rules: Dict, part: int) -> int:
    if part == 1:
        return sum(map(lambda b: contains_shiny_gold(b, rules), rules.keys()))
    else:
        return count_all_bags("shiny gold", rules)


def count_all_bags(bag, rules) -> int:
    sum_list = []
    for inner in rules[bag]:
        for bag, count in inner.items():
            sum_list.append(count * (1 + count_all_bags(bag, rules)))
    return sum(sum_list)


def contains_shiny_gold(bag, rules):
    for inside in rules[bag]:
        if inside.get("shiny gold") or contains_shiny_gold(list(inside.keys())[0], rules):
            return True
    return False


def parse_input(data) -> dict:
    """
    bags:
    {'light red': [{'bright white': 1}, {'muted yellow': 2}] .....
    """

    rules = dict()
    for line in data:
        line = line.replace("bags", "").replace("bag", "").replace(".", "").strip()
        colour, contents = line.split("contain")
        if contents.strip() == 'no other':
            rules[colour.strip()] = []

        else:
            child_list = list(map(str.strip, contents.split(',')))
            myl = []
            for bag in child_list:
                count, adj, col = bag.split()
                myl.append({adj + " " + col: int(count)})
            rules[colour.strip()] = myl
    return rules


def driver(file: str, part: int) -> int:
    file = read_file(file)
    rules = parse_input(file)
    return do_work(rules, part)


def solve_pt1a():
    return driver("D07P01a.txt", 1)


def solve_pt1b():
    return driver("D07P01b.txt", 1)


def solve_pt2a():
    return driver("D07P01a.txt", 2)


def solve_pt2b():
    return driver("D07P01b.txt", 2)


def solve_pt2c():
    return driver("D07P01c.txt", 2)


print(f"Day 7 Part 1a Answer: {solve_pt1a()}")
print(f"Day 7 Part 1b Answer: {solve_pt1b()}")
print(f"Day 7 Part 2a Answer: {solve_pt2a()}")
print(f"Day 7 Part 2b Answer: {solve_pt2b()}")
print(f"Day 7 Part 2c Answer: {solve_pt2c()}")

# Day 7 Part 1a Answer: 4
# Day 7 Part 1b Answer: 164
# Day 7 Part 2a Answer: 32
# Day 7 Part 2b Answer: 7872
# Day 7 Part 2c Answer: 126
