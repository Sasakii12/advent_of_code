from input import get_input
from functools import reduce


def part1(puzzle_inp: list[str]):
    pairs = 0
    form_inp = list(map(lambda x: x.split(','), puzzle_inp))
    for ranges in form_inp:
        r1 = list(map(lambda x: int(x),ranges[0].split('-')))
        r2 = list(map(lambda x: int(x),ranges[1].split('-')))
        range_cap1 = reduce(lambda x,y: y - x, r1)
        range_cap2 = reduce(lambda x,y: y - x, r2)
        if range_cap1 > range_cap2:
            if r1[0] <= r2[0] and r1[1] >= r2[1]:
                pairs += 1
        elif range_cap1 < range_cap2:
            if r2[0] <= r1[0] and r2[1] >= r1[1]:
                pairs += 1 
        else:
            if r1[0] == r2[0] and r1[1] == r2[1]:
                pairs += 1

    return pairs

def part2(puzzle_inp: list[str]) -> int:
    pairs = 0
    form_inp = list(map(lambda x: x.split(','), puzzle_inp))
    for ranges in form_inp:
        r1 = list(map(lambda x: int(x),ranges[0].split('-')))
        r2 = list(map(lambda x: int(x),ranges[1].split('-')))
        if r1[0] <= r2[1] and r2[0] <= r1[1]:
            pairs += 1
    return pairs



test = ["2-4,6-8", "2-8,3-7", "6-6,4-6", "2-6,4-8"]
puzzle_inp = list(map(lambda x: x.strip(),get_input('puzzle_inputs/day4.txt')))
print(part1(test))
print(part1(puzzle_inp))
print(part2(puzzle_inp))