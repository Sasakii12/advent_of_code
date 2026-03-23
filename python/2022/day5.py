# Plan: Convert the input stacks into a nxn matrix and
# turn the columns into stack structures

from input import get_input
from string import ascii_letters

def trim_rows(row: str) -> list[str]:
    new_row: list[str] = []
    count_whitespace = 0
    for elm in row.split(' '):
        if elm == '' or elm == '\n':
            count_whitespace += 1
        elif elm != '\n':
            new_row.append(elm.strip())

        if count_whitespace == 4:
            new_row.append('')
            count_whitespace = 0

    return new_row        

def extract_state(board: list[str]) -> list[list[str]]:
    transp_tup = zip(*[trim_rows(row) for row in board])
    transp_mat = [list(i)[::-1] for i in transp_tup]
    for i, elm in enumerate(transp_mat):
        transp_mat[i] = list(filter(lambda x : x != '', elm ))

    return transp_mat 

def move(amount: int, from_i: int, to_i: int, board: list[list[str]]) -> list[list[str]]:
    for _ in range(amount):
        fr = board[from_i - 1] 
        to = board[to_i - 1]
        elm = fr.pop()
        to.append(elm)

def extract_nums(s : str) -> list[int]:
    sp = s.split(' ')
    return [int(sp[1]), int(sp[3]), int(sp[5].strip())]


def move2(amount: int, from_i: int, to_i: int, board: list[list[str]]) -> list[list[str]]:
    fr = board[from_i - 1] 
    to = board[to_i - 1]
    popped_boxes: list[str] = []  
    for _ in range(amount): 
        popped_boxes.append(fr.pop())
    print(f"popped:{popped_boxes}")
    print(f"to: {to}")
    to += (popped_boxes[::-1])


puzzle_inp = get_input('puzzle_inputs/day5.txt')
n = puzzle_inp[0:8] 
stacks_list = extract_state(n)

print(extract_nums(puzzle_inp[10]))
for moves in puzzle_inp[10: len(puzzle_inp)]:
    amt = extract_nums(moves)
    move2(amt[0], amt[1], amt[2], stacks_list)

top = ''
for i in stacks_list:
    top += i[-1]

print(top)