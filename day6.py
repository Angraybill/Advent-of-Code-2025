#type:ignore

def open_part_one(nums, ops):
    with open("day6data.txt", "r") as f:
        lines = f.readlines()
        first = lines.pop(0).split(" ")
        for i in range(len(first)):
            first[i] = first[i].strip()
            if not first[i].isnumeric():
                continue
            first[i] = int(first[i])
            nums.append([first[i]])
        for line in lines:
            line = line.split(" ")
            tracer = 0
            for num in line:
                num = num.strip()
                if num.isnumeric():
                    nums[tracer].append(int(num))
                    tracer += 1

        ops_line = lines[-1]
        for op in ops_line:
            if op != "+" and op != "*":
                continue
            ops.append(op)

def open_part_two(nums_n, ops):
    nums = nums_n
    with open("day6data.txt", "r") as f:
        lines = f.readlines()
        first = True
        for line in lines:
            if line == lines[-1]:
                break
            line = list(line)
            if first:
                for l in line:
                    nums.append([l])
                first = False
                continue
            for i, n in enumerate(line):
                if i >= len(nums):
                    nums.append(n)
                    continue
                nums[i] += n
        ops_line = lines[-1]
        ops_lens = []
        for op in ops_line:
            if op != "+" and op != "*":
                ops_lens[-1] += 1
                continue
            ops.append(op)
            ops_lens.append(0)
        ops_lens[-1] += 1

        nums.pop(-1)
        nums_hold = []
        for i in range(len(nums)):
            nums[i] = "".join(nums[i]).strip()
            if nums[i].isnumeric():
                nums[i] = int(nums[i])
                nums_hold.append(nums[i])
        
        nums = []
        tracer = 0
        while len(nums_hold) > 0:
            chunk = []
           # print(tracer, end=" ")
            for i in range(ops_lens[tracer]):
                chunk.append(nums_hold.pop(0))
            tracer += 1
            nums.append(chunk)

        return nums, ops


def part_one():
    nums = []
    ops = []
    nums, ops = open_part_one(nums, ops)
    total = 0
    for i in range(len(ops)):
        if ops[i] == "+":
            tot = 0
            for n in nums[i]:
                tot += n
            total += tot
        if ops[i] == "*":
            tot = 1
            for n in nums[i]:
                tot *= n
            total += tot
    print(total)


def part_two():
    nums = []
    ops = []
    nums, ops = open_part_two(nums, ops)
    total = 0
    for i in range(len(ops)):
        if ops[i] == "+":
            tot = 0
            for n in nums[i]:
                tot += n
            total += tot
        if ops[i] == "*":
            tot = 1
            for n in nums[i]:
                tot *= n
            total += tot
    print(total)


part_two()