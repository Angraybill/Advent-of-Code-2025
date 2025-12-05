#type:ignore

ranges = []
with open("day2data.txt", "r") as f:
    r = f.readlines()[0].split(",")
    for i in r:
        nums = i.split("-")
        ranges.append((int(nums[0]), int(nums[1])))


def part_one():
    total = 0
    for s in ranges:
        for i in range(s[0], s[1] + 1):
            str_i = str(i)
            if len(str_i) % 2 != 0:
                continue
            front = str_i[:len(str_i)//2]
            back = str_i[len(str_i)//2:]
            if (front == back):
                total += i

    print(total)

def part_two():
    total = 0
    found = set()
    for s in ranges:
        for i in range(s[0], s[1] + 1):
            str_i = str(i)
            for j in range(1, len(str_i) // 2 + 1):
                if len(str_i) % j != 0:
                    continue
                ops = []
                equal = True
                for k in range(0, len(str_i), j):
                    ops.append(str_i[k:k+j])
                    equal &= ops[-1] == ops[0]
                if equal and i not in found:
                   # print(str_i, j, ops[0])
                    found.add(i)
                    total += i
    print(total)
                
                

part_two()
