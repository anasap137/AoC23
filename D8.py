import itertools as it
file = open("input.txt", "r")

steps = file.readline().strip()

mapped = {}

while line:=file.readline():
    if line == '\n':
        continue
    key, directions = line.split(" = ")
    left, right = directions.strip().strip("(").strip(")").split(",")
    mapped[key] = left, right

currKey = next(iter(mapped))
total_steps = 0
for direction in it.cycle(steps):
    if currKey == 'ZZZ':
        print(total_steps)
        break
    total_steps += 1
    if direction == 'L':
        currKey = mapped[currKey][0].strip() #Get left element

    elif direction == 'R':
        currKey = mapped[currKey][1].strip() #Get left element



   
    