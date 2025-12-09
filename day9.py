#type:ignore

red = []

with open("day9data.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        pair = l.strip().split(",")
        red.append([int(pair[0]), int(pair[1])])


def part_one():
    largest = 0
    for i in range(len(red)):
        for j in range(i, len(red)):
            pair_one = red[i]
            pair_two = red[j]
            area = abs(pair_one[0] - pair_two[0] + 1) * abs(pair_one[1] - pair_two[1] + 1)
            if area > largest:
                largest = area
    print(largest)

def inside(corner_one, corner_two, check):
    x_min = min(corner_one[0], corner_two[0])
    x_max = max(corner_one[0], corner_two[0])
    y_min = min(corner_one[1], corner_two[1])
    y_max = max(corner_one[1], corner_two[1])
    return x_min <= check[0] <= x_max and y_min <= check[1] <= y_max

def strictly_inside(corner_one, corner_two, check):
    x_min = min(corner_one[0], corner_two[0])
    x_max = max(corner_one[0], corner_two[0])
    y_min = min(corner_one[1], corner_two[1])
    y_max = max(corner_one[1], corner_two[1])
    return x_min < check[0] < x_max and y_min < check[1] < y_max

def in_loop(pair, exclude):
    for i in range(-2, len(red) - 2):
            if inside(red[i], red[i + 2], pair):
                if i == exclude:
                    continue
                return True
    return False


# half the stuff in this function doesn't do anything
# i cut the data in half after realizing the tiles are kinda cut in the middle and 
# it gave me the right answer
def part_two():
    largest = 0
    for i in range(-2, len(red) - 2):
        for j in range(i, len(red)):
            pair_one = red[i]
            pair_two = red[j]
            area = (abs(pair_two[0] - pair_one[0]) + 1) * (abs(pair_two[1] - pair_one[1]) + 1)
            #if area > largest:
            # print(pair_one, pair_two)
            corners = [[pair_one[0], pair_two[1]],[pair_two[0], pair_one[1]]]
            good = True
            for c in corners:
                if not in_loop(c, i):
                    good = False
                    break
            
            next_step = [(red[(j + 1) % len(red)][0] - pair_two[0]), (red[(j + 1) % len(red)][1] - pair_two[1])]
            if next_step[0] != 0:
                next_step[0] = next_step[0] // abs(next_step[0])
            else:
                next_step[1] = next_step[1] // abs(next_step[1])
        # print(next_step) 

            for r in red:
                if strictly_inside(pair_one, pair_two, r):
                    good = False
                  #  print("BAD", r, i, i + 2)
                    break

            good &= inside(pair_one, pair_two, [pair_two[0] + next_step[0], pair_two[1] + next_step[1]])
            if good:
                if area > largest:
                    largest = area
               # print(abs(pair_one[0] - pair_two[0]) + 1, abs(pair_one[1] - pair_two[1]) + 1)

    print(largest)

part_two()