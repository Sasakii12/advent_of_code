from input import  get_input_str

def get_line(line: str) -> tuple[str,str]:
    rps_arr = line.strip().split(' ')
    return (rps_arr[0], rps_arr[1])

def puzzle_arr(inp: str) -> list[str]:
    return list(filter(None, inp.split('\n')))
    
def game_result(puzzle_inp: list[str]) -> int:
    points = 0

    rules = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    for game in puzzle_inp:
        game_vals = get_line(game)
        if (game_vals[0] == 'A' and game_vals[1] == 'Y') or (game_vals[0] == 'B' and game_vals[1] == 'Z') or (game_vals[0] == 'C' and game_vals[1] == 'X'):
            points += 6 + rules[game_vals[1]]
        elif (game_vals[0] == 'A' and game_vals[1] == 'Z') or (game_vals[0] == 'B' and game_vals[1] == 'X') or (game_vals[0] == 'C' and game_vals[1] == 'Y'):
            points += rules[game_vals[1]]
        else:
            points += 3 + rules[game_vals[1]]
    
    return points

# Im too tired for part 2
# def game_result2(puzzle_inp: list[str]) -> int: 
#     points = 0

#     rules = {
#         'A': 1,
#         'B': 2,
#         'C': 3,
#     }

#     for game in puzzle_inp:
#         game_vals = get_line(game)
#         if (game_vals[0] in ['A', 'B', 'C'] and game[1] == 'Y'):
#             points += 3 + 

puzzle_input = get_input_str('puzzle_inputs/day2_1.txt')

print(puzzle_input)
puzzle_list = puzzle_arr(puzzle_input)
print(get_line(puzzle_list[0]))
print(game_result(puzzle_list))