from input import get_input  # pyright: ignore[reportImplicitRelativeImport]


def calorie_sums(calorie_list: list[str]) -> list[int]:
    summed_cals: list[int] = []
    cal_sum = 0
    for cal in calorie_list:
        if cal != '\n':
            cal_sum += int(cal.strip())
        else:
            summed_cals.append(cal_sum)
            cal_sum = 0
    return summed_cals

def get_three_largest(arr: list[int]) -> list[int]:
    first = second = third = -10000

    for i in arr:
        if i > first:
            third = second
            second = first
            first = i
        elif i > second and i != first:
            third = second
            second = i
        elif i > third and i != second and i != first:
            third = i
        
    three_largest = [first, second, third] 
    if -10000 in three_largest:
        return []
        
    return three_largest

 
puzzle_input = get_input('puzzle_inputs/day1_1.txt')

cal = calorie_sums(puzzle_input)
print(max(cal))
print(sum(get_three_largest(cal)))
