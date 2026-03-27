# Plan: Extract the lines starting with $ and not and have some reference to the cd and ls commands along with their args
# keep track of current directory and depth, when .. is found return to previous dir
# For none $ lines it is not a command and differentiate between starting with dir or not, to find size and filename 
# If its a dir ignore, else its a file, therefore store its size. 


# Idea: have a function recursively iterate throught the input
# one argument thats a string keeps track of the dir IE "abc/dce"
# when a cd command is found append to or trim the dir of the string and return the numbers computed
from input import get_input
from functools import reduce

def parse_line(line: str) -> list[str]:
    return line.split(" ")

def trim_dir(d: str) -> str:
    d_list = d.split("/")[:-1]
    print(len(d_list))
    if len(d_list) > 1:
        return reduce(lambda x,y: x + "/" + y, d_list)
    else:
        return "/"

def dir_to_str(s : list[str]) -> str:
    return "/" + reduce(lambda x,y: x + "/" + y, s)

def sum_upper_dirs(dir_dict, dir_str):
    if dir_str == "/":
        return dir_dict
    trimmed_dir = trim_dir(dir_str)
    dir_dict[trimmed_dir] += dir_dict[dir_str]
    return sum_upper_dirs(dir_dict, trimmed_dir)



def parse_dir(puzzle_inp: list[str]):
    dir_stack = []
    dir_dict = {"/": 0}
    for i in puzzle_inp:
        line = parse_line(i)
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    dir_stack.pop()
                elif line[2] != "/":
                    dir_stack.append(line[2])
        else:
            if line[0] == "dir":
                temp = dir_stack + [line[1]]
                dir_dict[dir_to_str(temp)] = 0
            elif line[0] != "":
                size = int(line[0])
                if dir_stack == []:
                    dir_dict["/"] += size
                    continue
                dir_dict[dir_to_str(dir_stack)] += size
                dir_dict = sum_upper_dirs(dir_dict, dir_to_str(dir_stack))
    print(dir_stack)
    print(dir_dict)
    res = 0
    for i in dir_dict.keys():
        if dir_dict[i] <= 100000:
            res += dir_dict[i]
    return res

puzzle_inp = get_input('puzzle_inputs/day7.txt')
clean_puzzle = list(map(lambda x : x.strip(), puzzle_inp))
print(parse_dir(clean_puzzle))
