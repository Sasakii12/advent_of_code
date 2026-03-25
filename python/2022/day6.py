from input import get_input

# Plan: Recursively traverse the characters in the string
# Check if that char is in a list of already checked chars
# If not push to list
# For every fourth recursive step clear the list
# When four chars are found without repeats return the first elem of the list

import collections
from input import get_input_str

    
def datastream(inp: str, start=4):
    for i in range(start, len(inp)):
        print(f"i: {i}")
        print(inp[(i - start):i])
        if len(list(set(inp[i-start:i]))) == len(list(inp[i-start:i])):
            return i


puzzle_inp = get_input_str("puzzle_inputs/day6.txt")
print(datastream("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14))
print(datastream(puzzle_inp, 14))
