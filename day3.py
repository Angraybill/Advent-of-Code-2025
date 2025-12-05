banks = []
with open("day3data.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        banks.append(l.strip())


def part_one():
    total = 0
    for bank in banks:
        val1 = 0
        index = -1
        for i, battery1 in enumerate(bank[:-1]):
            if int(battery1) > val1:
                val1 = int(battery1)
                index = i
        val2 = 0
        for battery2 in bank[index + 1:]:
            if int(battery2) > val2:
                val2 = int(battery2)
        total += (val1 * 10) + val2
        #print((val1 * 10) + val2)

    print(total)

def part_two():
    total = 0
    for bank in banks:
        vals = [0]*12
        start = 0
        for r in range(11, -1, -1): # 11 extra spaces down to 0 extra spaces
            idx = 0
            for i, battery in enumerate(bank[start:len(bank)-r]):
                if int(battery) > vals[r]:
                    idx = i + start
                    vals[r] = int(battery)
            start = idx + 1
            
        for i in range(12):
            total += vals[i] * (10 ** i)
    print(total)

part_two()
