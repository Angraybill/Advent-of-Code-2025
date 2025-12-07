#type:ignore
ranges = []
ids = []
with open("day5dad.txt", "r") as f:
    lines = f.readlines()
    phase_one = True
    for line in lines:
        if line == "\n":
            phase_one = False
            continue
        if phase_one:
            ranges.append(line.strip().split("-"))
            ranges[-1][0] = int(ranges[-1][0])
            ranges[-1][1] = int(ranges[-1][1])
        else:
            ids.append(int(line.strip()))

def insertion_sort(input):
    for i in range(1, len(input)):
        temp = input[i]
        k = i
        while (k > 0 and temp[0] <= input[k - 1][0]):
            input[k] = input[k-1]
            k -= 1
        input[k] = temp



def part_one_wrong():
    insertion_sort(ranges)
    total = 0
    for id in ids:
        low = 0
        high = len(ranges) - 1
        while low <= high:
            mid = (low + high) // 2
            look = ranges[mid]
            if id >= look[0] and id <= look[1]:
                total += 1
                break
            elif look[0] > id:
                high = mid - 1
            else:
                low = mid + 1
    print(total)


def part_one():
    total = 0
    for id in ids:
        for r in ranges:
            if id >= r[0] and id <= r[1]:
                total += 1
                break
    print(total)

def part_two():
    insertion_sort(ranges)
    all_ranges = [ranges[0]]
    for r in ranges[1:]:
        handled = False
        for trace in all_ranges:
            if r[0] >= trace[0] and r[0] <= trace[1] and r[1] >= trace[1]:
                trace[1] = r[1]
                handled = True
            if r[1] <= trace[1] and r[1] >= trace[0] and r[0] <= trace[0]:
                trace[0] = r[0]
                handled = True
            if r[0] <= trace[0] and r[1] >= trace[1]:
                trace = r
                handled = True
            if r[0] >= trace[0] and r[1] <= trace[1]:
                handled = True

        if not handled:
            all_ranges.append(r)
    total = 0
    for pair in all_ranges:
        total += pair[1] - pair[0] + 1
    print(total)



part_two()