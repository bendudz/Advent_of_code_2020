# --- Day 3: Toboggan Trajectory ---
from typing import List
from utils import read_file


def do_work(routes: List[str], slope: tuple):
    x, y = slope
    tree_list = []
    new_x, new_y = slope
    x_width_max = len(routes[0])
    while True:
        if routes[new_y][new_x] == '#':
            tree_list.append('Y')

        new_x += x

        if new_x >= x_width_max:
            new_x -= x_width_max

        new_y += y

        if new_y >= len(routes):
            break

    return tree_list


def driver(file: str, slope: tuple):
    puzzle_input = read_file(file)
    routes = [v for v in puzzle_input]
    return len(do_work(routes, slope))


def solve_pt1a():
    return driver("D03P01a.txt", (3, 1))


def solve_pt1b():
    return driver("D03P01b.txt", (3, 1))


def solve_pt2a():
    a = driver("D03P01a.txt", (1, 1))
    b = driver("D03P01a.txt", (3, 1))
    c = driver("D03P01a.txt", (5, 1))
    d = driver("D03P01a.txt", (7, 1))
    e = driver("D03P01a.txt", (1, 2))
    return a * b * c * d * e


def solve_pt2b():
    a = driver("D03P01b.txt", (1, 1))
    b = driver("D03P01b.txt", (3, 1))
    c = driver("D03P01b.txt", (5, 1))
    d = driver("D03P01b.txt", (7, 1))
    e = driver("D03P01b.txt", (1, 2))
    return a * b * c * d * e


print(f"Day 3 Part 1a Answer: {solve_pt1a()}")
print(f"Day 3 Part 1b Answer: {solve_pt1b()}")
print(f"Day 3 Part 2a Answer: {solve_pt2a()}")
print(f"Day 3 Part 2b Answer: {solve_pt2b()}")

# Day 3 Part 1a Answer: 7
# Day 3 Part 1b Answer: 167
# Day 3 Part 2a Answer: 336
# Day 3 Part 2b Answer: 736527114
