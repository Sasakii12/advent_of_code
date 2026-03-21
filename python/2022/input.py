# Opens the input file for each problem

def get_input(file: str) -> list[str]:
    input: list[str] = []
    with open(file) as f:
        for i in f.readlines():
            input.append(i)
    return input

def get_input_str(file: str) -> str:
    with open(file) as f:
        contents = f.read()

    return contents