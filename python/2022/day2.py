from input import  get_input_str

def get_line(line: str) -> tuple[str,str]:
    rps_arr = line.strip().split(' ')
    return (rps_arr[0], rps_arr[1])

def puzzle_arr(inp: str) -> list[str]:
    return inp.split('\n')
    
def game_result(puzzle_inp: list[str]) -> int:
    points = 0
    game_table = {'A': 'Y',
                             'B': 'Z',
                             'C': 'X'}
    point_table = {'X': 1, 'Y': 2, 'Z': 3}
    for game in puzzle_inp:
       game_tuple = get_line(game) 
       win_con = game_table[game_tuple[0]]
       if win_con == game_tuple[1]:
        points += 6 + point_table[game_tuple[1]]
       elif win_con != game_tuple[1] and game_tuple[0]:
        pass #idea just translate the xyz into abc for comparison im too tired 




puzzle_input = get_input_str('puzzle_inputs/day2_1.txt')

print(puzzle_input)
puzzle_list = puzzle_arr(puzzle_input)
print(get_line(puzzle_list[0]))