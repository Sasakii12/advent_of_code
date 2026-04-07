from input import get_input
from functools import reduce


def column_viewer(elem: int, col: list[str], ind: int):
    clear = 0
    for i in (col):
        if elem > int(i[ind]):
            clear += 1
    if clear == len(col):
        return True
    
    return False

def row_viewer(elem: int, row: str, ind: int):
    clear = 0
    for i in row:
        if elem > int(i):
            clear += 1
    if clear == len(row):
        return True
    return False

def column_viewer2(elem: int, col: list[str], ind: int):
    clear = 0
    for i in (col):
        if elem > int(i[ind]):
            clear += 1
        else:
            clear += 1
            break
    return clear    

def row_viewer2(elem: int, row: str, ind: int):
    clear = 0
    for i in row:
        if elem > int(i):
            clear += 1
        else:
            clear += 1
            break
    return clear

def parse_trees(inp: list[str]):
    visible = 0
    for i,r in enumerate(inp):
        if (i == 0 or i == len(inp) - 1):
            visible += len(inp[i])
            continue
        for k, elem in enumerate(r):
            if k == 0 or k == len(r) - 1:
                visible += 1
                continue
            
            up = inp[0:i]
            down = inp[i + 1: len(inp[i])]
            left = inp[i][0:k]
            right = inp[i][k+1: len(inp[i])]
            int_k = int(elem)
            if column_viewer(int_k, up, k):
                visible +=1
            elif column_viewer(int_k, down, k):
                visible += 1
            elif row_viewer(int_k, left, k):
                visible += 1
            elif row_viewer(int_k, right, k):
                visible += 1
    return visible


def parse_trees2(inp: list[str]):
    scenic_score = []
    for i,r in enumerate(inp):
        if (i == 0 or i == len(inp) - 1):
            continue
        for k, elem in enumerate(r):
            if k == 0 or k == len(r) - 1:
                continue
            
            up = inp[0:i][::-1]
            down = inp[i + 1: len(inp[i])]
            left = inp[i][0:k][::-1]
            right = inp[i][k+1: len(inp[i])]
            int_k = int(elem)
            clear = []
            clear.append(column_viewer2(int_k, up, k))
            clear.append(column_viewer2(int_k, down, k))
            clear.append(row_viewer2(int_k, right, k))
            clear.append(row_viewer2(int_k, left, k))
            scenic_score.append(reduce(lambda x,y: x * y, clear))
            
    return max(scenic_score)


    


input = get_input("puzzle_inputs/day8.txt")
clean_inp = list(map(lambda x: x.strip(), input))
string_array = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390"
]
print(parse_trees2(clean_inp))
