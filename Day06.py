# --- Day 6: Custom Customs ---
from copy import deepcopy
from typing import List, Set


def do_work(groups: List[str], part: int) -> int:
    if part == 1:
        return part1(groups)
    else:
        return part2(groups)


def part1(groups: List[str]) -> int:
    answer_count = []
    for group in groups:
        split_group = group.strip().split('\n')
        group_answers = [question for survey in split_group for question in survey]
        unique_answers = set(group_answers)
        answer_count.append(len(unique_answers))

    return sum(answer_count)


def part2(groups: List[str]) -> int:
    answer_count = []
    for group in groups:
        split_group = group.strip().split('\n')
        group_answers = [list(survey) for survey in split_group]
        unique_answers = find_common_answers(group_answers)
        answer_count.append(len(unique_answers))

    return sum(answer_count)


def find_common_answers(group_answers: List) -> Set:
    const = deepcopy(group_answers[0])
    for i in range(len(group_answers) - 1):
        const = set(const).intersection(group_answers[i + 1])
    return const


def driver(file: str, part: int) -> int:
    puzzle_input = ''.join(list(open(f'resources/{file}')))
    groups = puzzle_input.split('\n\n')
    return do_work(groups, part)


def solve_pt1a():
    return driver("D06P01a.txt", 1)


def solve_pt1b():
    return driver("D06P01b.txt", 1)


def solve_pt2a():
    return driver("D06P01a.txt", 2)


def solve_pt2b():
    return driver("D06P01b.txt", 2)


print(f"Day 6 Part 1a Answer: {solve_pt1a()}")
print(f"Day 6 Part 1b Answer: {solve_pt1b()}")
print(f"Day 6 Part 2a Answer: {solve_pt2a()}")
print(f"Day 6 Part 2b Answer: {solve_pt2b()}")

# Day 6 Part 1a Answer: 11
# Day 6 Part 1b Answer: 6161
# Day 6 Part 2a Answer: 6
# Day 6 Part 2b Answer: 2971
