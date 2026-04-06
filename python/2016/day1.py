from file import get_input_str # pyright: ignore[reportImplicitRelativeImport]

class Grid:
    x: int
    y: int
    direction: str

    def __init__(self, x: int =0, y: int =0, direction: str="North") -> None:
        self.x = x
        self.y = y
        self.direction = direction

    def change_dir(self, rot: str):
        if rot == "R":
            if self.direction == "North":
                self.direction = "East"
            elif self.direction == "East":
                self.direction = "South"
            elif self.direction == "South":
                self.direction = "West"
            else:
                self.direction = "North"

        else:
            if self.direction == "North":
                self.direction = "West"
            elif self.direction == "West":
                self.direction = "South"
            elif self.direction == "South":
                self.direction = "East"
            else:
                self.direction = "North"

    def move(self, rot: str, steps: int):
        self.change_dir(rot)

        if self.direction == "North":
            self.y += steps
        elif self.direction == "West":
            self.x -= steps
        elif self.direction == "East":
            self.x += steps
        else:
            self.y -= steps

    def step(self, steps: int):
        if self.direction == "North":
            self.y += steps
        elif self.direction == "West":
            self.x -= steps
        elif self.direction == "East":
            self.x += steps
        else:
            self.y -= steps

    def __eq__(self, others):
        if self.x == others.x and self.y == others.y:
            return True
        else:
            return False



def manhat_dist(x1: int,y1: int,x2: int,y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)

pos = Grid()

inp = get_input_str('puzzle_input/day1.txt').split(',')
print(inp)

for i  in inp:
    clean = i.strip()
    print(clean[1:])

    pos.move(clean[0], int(clean[1:]))

print(f"x: {pos.x} y: {pos.y}")

print(manhat_dist(0,0, pos.x, pos.y))

pos2 = Grid()
pos_lists = []
for i in inp:
    clean = i.strip()
    steps = clean[1:]
    pos2.move(clean[0], 0)
    for i in range(int(steps)):
        pos2.step(1)

        if pos2 in pos_lists:
            print(f"{manhat_dist(0,0, pos2.x, pos2.y)}")
            exit()
            break
        pos_lists.append(Grid(pos2.x, pos2.y))



