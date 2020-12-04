# --- Day 4: Passport Processing ---
import re
from typing import List


def do_work(groups: List[str], part: int) -> List:
    valid_docs = []
    for entry in groups:
        proposed_passport = {}
        new_entry = entry.strip().replace('\n', ' ').split(' ')
        for line in new_entry:
            e = line.split(':')
            proposed_passport[e[0]] = e[1]

        if valid(proposed_passport, part):
            valid_docs.append('Y')

    return valid_docs


def valid(document: dict, part: int) -> bool:
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # , 'cid']
    if len(document) < 7:
        return False

    if all(field in document for field in valid_fields):
        if part == 1:
            return True
        else:
            return validate_fields(document)
    else:
        return False


def validate_fields(document: dict) -> bool:
    if not len(document['byr']) == 4:
        return False

    if not len(document['iyr']) == 4:
        return False

    if not len(document['eyr']) == 4:
        return False

    if not 1920 <= int(document['byr']) <= 2002:
        return False

    if not 2010 <= int(document['iyr']) <= 2020:
        return False

    if not 2020 <= int(document['eyr']) <= 2030:
        return False

    if str(document['hgt']).endswith('cm') and 150 <= int(document['hgt'][:-2]) <= 193:
        pass
    elif str(document['hgt']).endswith('in') and 59 <= int(document['hgt'][:-2]) <= 76:
        pass
    else:
        return False

    if not re.match(r'^#[0-9a-f]{6}', document['hcl']):
        return False

    if not any(colour in document['ecl'] for colour in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False

    if len(document['pid']) != 9:
        return False

    return True


def driver(file: str, part: int) -> int:
    puzzle_input = ''.join(list(open(f'resources/{file}')))
    groups = puzzle_input.split('\n\n')
    return len(do_work(groups, part))


def solve_pt1a():
    return driver("D04P01a.txt", 1)


def solve_pt1b():
    return driver("D04P01b.txt", 1)


def solve_pt2a():
    return driver("D04P02a.txt", 2)


def solve_pt2b():
    return driver("D04P02b.txt", 2)


def solve_pt2c():
    return driver("D04P01b.txt", 2)


print(f"Day 4 Part 1a Answer: {solve_pt1a()}")
print(f"Day 4 Part 1b Answer: {solve_pt1b()}")
print(f"Day 4 Part 2a Answer: {solve_pt2a()}")
print(f"Day 4 Part 2b Answer: {solve_pt2b()}")
print(f"Day 4 Part 2c Answer: {solve_pt2c()}")

# Day 4 Part 1a Answer: 2
# Day 4 Part 1b Answer: 233
# Day 4 Part 2a Answer: 0
# Day 4 Part 2b Answer: 4
# Day 4 Part 2c Answer: 111
