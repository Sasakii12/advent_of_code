from input import get_input

# Plan: Recursively traverse the characters in the string
# Check if that char is in a list of already checked chars
# If not push to list
# For every fourth recursive step clear the list
# When four chars are found without repeats return the first elem of the list

import collections
from input import get_input_str

def datastream_rec(inp : str, v: list[str]=[], start=0) -> int:
    if inp == "":
        return -1
    print(inp[0])
    print(v)
    print(start)
    if start % 3 == 0 and start != 0:
        if collections.Counter(list(set(v + [inp[0]]))) != collections.Counter(v + [inp[0]]):
            v = []
        else:
            return start

    return datastream_rec(inp[1:], v + [inp[0]], start + 1)
    
def datastream(inp: str):
    for i in range(4, len(inp)):
        print(f"i: {i}")
        print(inp[(i - 4):i])
        if collections.Counter(list(set(inp[i-4:i]))) == collections.Counter(list(inp[i-4:i])):
            return i


puzzle_inp = get_input_str("puzzle_inputs/day6.txt")
print(datastream("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
print(datastream(puzzle_inp))
