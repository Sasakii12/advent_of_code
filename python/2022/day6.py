from input import get_input

# Plan: Recursively traverse the characters in the string
# Check if that char is in a list of already checked chars
# If not push to list
# For every fourth recursive step clear the list
# When four chars are found without repeats return the first elem of the list

import collections
from input import get_input_str

    
def datastream(inp: str):
    for i in range(4, len(inp)):
        print(f"i: {i}")
        print(inp[(i - 4):i])
        if len(list(set(inp[i-4:i]))) == len(list(inp[i-4:i])):
            return i


puzzle_inp = get_input_str("puzzle_inputs/day6.txt")
print(datastream("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
print(datastream(puzzle_inp))
