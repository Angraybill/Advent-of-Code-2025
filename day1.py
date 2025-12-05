nums = []
with open("day1data.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        nums.append(int(l[1:]) * (-1 if l[0] == "L" else 1))

trace = 50
count = 0
skip = False

print(50)
for n in nums:
    if trace == 0:
        skip = True
    trace += n
    
   # print(trace, trace % 100, n)
    while trace > 100:
        trace -= 100
        count += 1
    #    print("Over *", trace)
    while trace <= -100:
        trace += 100
        count += 1
     #   print("Under *", trace)
    hold = trace
    trace %= 100
    if hold != trace and trace != 0 and not skip:
        count += 1
      #  print("Mod *")
    if trace == 0:
        count += 1
       # print("Zero *")
    
    zeroed = False
    skip = False
   # input()
    
    

    
print(count)
    
