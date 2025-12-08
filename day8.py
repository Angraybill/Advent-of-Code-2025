# type:ignore
import time

class box:
    
    def __init__(self, loc, name):
        self.loc = loc
        self.name = name

    def __str__(self):
        return str(self.name)
class distance:
    
    def __init__(self, box1, box2):
        self.box1 = box1
        self.box2 = box2
        self.val = round(((box1.loc[0] - box2.loc[0])**2 + (box1.loc[1] - box2.loc[1])**2 + (box1.loc[2] - box2.loc[2])**2) ** (1/2), 2)

    def __str__(self):
        return f"{str(self.box1)} <--> {str(self.box2)}: {self.val}"

boxes = []

with open("day8data.txt", "r") as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        loc = line.strip().split(",")
        for i in range(3):
            loc[i] = int(loc[i])
        boxes.append(box(loc, count))
        count += 1


def key(input):
    return input.val



def insert(circuts, box1, box2):
    one_in = -1
    two_in = -1
    for c in range(len(circuts)):
        for b in circuts[c]:
            if box1 == b:
                one_in = c
            if box2 == b:
                two_in = c
            if one_in != -1 and one_in == two_in:
                return
        
    if one_in == two_in and one_in == -1:
        circuts.append([box1, box2])
    elif one_in == -1:
        circuts[two_in].append(box1)
    elif two_in == -1:
        circuts[one_in].append(box2)
    else:
        hold = circuts.pop(max(one_in, two_in))
        circuts[min(one_in, two_in)].extend(hold)


def part_one():
    distances = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distances.append(distance(boxes[i], boxes[j]))

    list.sort(distances, key=key)

    connected = 0
    circuts = []
    while connected < 1000 and len(distances) > 0:
        test = distances.pop(0)
        insert(circuts, test.box1, test.box2)
        connected += 1
    


    list.sort(circuts, key=lambda input: len(input), reverse=True)
    total = len(circuts[0]) * len(circuts[1]) * len(circuts[2])

    print(total)

    

def part_two():
    distances = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distances.append(distance(boxes[i], boxes[j]))

    list.sort(distances, key=key)

    connected = 0
    circuts = []
    while True:
        test = distances.pop(0)
        insert(circuts, test.box1, test.box2)
        connected += 1

        if connected > 10 and len(circuts) == 1:
            print(test.box1.loc[0] * test.box2.loc[0])
            break
    



part_one()
part_two()