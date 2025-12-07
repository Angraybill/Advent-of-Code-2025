#type:ignore

grid = []
with open("day7data.txt", "r") as f:
    grid = f.readlines()
    for i in range(len(grid)):
        grid[i] = grid[i].strip()



def part_one():
    total = 0
    beams = set()
    for i, c in enumerate(grid[0]):
        if c == "S":
            beams.add(i)
            break
    row = 1
    while row < len(grid):
        remove = []
        add = []
        for beam in beams:
            if grid[row][beam] == "^":
                remove.append(beam)
                add.extend([beam+1, beam-1])
                total += 1
        for b in remove:
            beams.remove(b)
        for a in add:
            beams.add(a)
        row += 1
    
    
    print(total)




def part_two():
    timelines = [0]*len(grid[0])
    for i, c in enumerate(grid[0]):
        if c == "S":
            timelines[i] += 1
            break

    row = 1
    while row < len(grid):
        if row % 2 == 1:
            row += 1
            continue
        timelines_hold = [0]*len(grid[0])
        for i, t in enumerate(timelines):
            if grid[row][i] == ".":
                timelines_hold[i] += t
            else:
                timelines_hold[i-1] += t
                timelines_hold[i+1] += t
                timelines_hold[i] = 0 if timelines_hold[i] == 0 else timelines_hold[i] - t
        timelines = timelines_hold
        row += 1

    total = 0
    for t in timelines:
        total += t
    print(total)
                




part_one()
part_two()