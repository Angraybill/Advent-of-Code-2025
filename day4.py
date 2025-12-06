#type:ignore
wall = []
with open("day4data.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        wall.append(list(l.strip()))

def part_one():
    total = 0
    for y in range(len(wall)):
        for x in range(len(wall[0])):
            if wall[y][x] != "@":
                continue
            square_tot = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx == dy and dx == 0:
                        continue
                    if x + dx >= 0 and x + dx < len(wall[0]) and y + dy >= 0 and y + dy < len(wall):
                        if wall[y + dy][x + dx] == "@":
                            square_tot += 1
            if square_tot < 4:
                total += 1
            
    print(total)


def part_two():
    total = 0
    num_changed = 1
    changed = []
    while num_changed != 0:
        num_changed = 0
        for y in range(len(wall)):
            for x in range(len(wall[0])):
                if wall[y][x] != "@":
                    continue
                square_tot = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dx == dy and dx == 0:
                            continue
                        if x + dx >= 0 and x + dx < len(wall[0]) and y + dy >= 0 and y + dy < len(wall):
                            if wall[y + dy][x + dx] == "@":
                                square_tot += 1
                if square_tot < 4:
                    num_changed += 1
                    changed.append((x,y))

        total += num_changed
        for pair in changed:
            wall[pair[1]][pair[0]] = "x"
        changed = []
    print(total)



part_two()