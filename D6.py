file = open("input.txt", "r")

tmp = file.readline().split(":")[1].strip().split(" ")
time = ''
for elem in tmp:
    if elem.isdigit():
        time += elem 

tmpDist = file.readline().split(":")[1].strip().split(" ")
record = ''
for elem in tmpDist:
    if elem.isdigit():
        record += elem 

total = 0

# PART 2: Brute-force approach
for i in range(int(time)):
    if i * (int(time) - i) > int(record):
        total += 1

print(total)
