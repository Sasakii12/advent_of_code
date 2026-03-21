from input import get_input
import string

def rucksack_compartments(sack: str) -> tuple[str, str]:
    sack_len = len(sack)
    return (sack[0: (sack_len // 2)], sack[(sack_len // 2): sack_len])

def find_intersecting_char(rucksack: tuple[str,str]):
    comp1 = set(rucksack[0])
    comp2 = set(rucksack[1])

    return comp1.intersection(comp2)
    
def get_priority(puzzle_inp: list[str]) -> int: 
    alphabet = {string.ascii_letters[priority - 1]: priority for priority in range(1, len(string.ascii_letters)+1)}
    prio = 0
    for rucksack in puzzle_inp:
        rucksack_comps = rucksack_compartments(rucksack)
        inter_chars = find_intersecting_char(rucksack_comps)
        print(inter_chars)
        prio += sum(list(map(lambda x: alphabet[x],inter_chars)))
    return prio

def get_priority2(puzzle_inp: list[str]) -> int: 
    alphabet = {string.ascii_letters[priority - 1]: priority for priority in range(1, len(string.ascii_letters)+1)}
    prio = 0
    for rucksack in range(0, len(puzzle_inp), 3):
        if rucksack + 2 >= len(puzzle_inp):
            break
        set1 = set(puzzle_inp[rucksack])
        set2 = set(puzzle_inp[rucksack + 1])
        set3 = set(puzzle_inp[rucksack + 2])
        inter_chars = set1.intersection(set2).intersection(set3) 
        print(inter_chars)
        prio += sum(list(map(lambda x: alphabet[x],inter_chars)))
        
    return prio

puzzle_inp = list(map(lambda x: x.strip(),get_input('puzzle_inputs/day3.txt')))
# print(puzzle_inp)
# print(get_priority(puzzle_inp))
test = ["vJrwpWtwJgWrhcsFMMfFFhFp" ,"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT" ,"CrZsJsPPZsGzwwsLwLmpwMDw"]
# print(get_priority(test))
print(get_priority2(puzzle_inp))
print(get_priority2(test))