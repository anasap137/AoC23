file = open("testInput.txt", "r")

tmp = file.readline().split(":")[1].strip().split(" ")
time = [x for x in tmp if x.isdigit()]

tmpDist = file.readline().split(":")[1].strip().split(" ")
records = [x for x in tmpDist if x.isdigit()]

races = []
for i in range(len(time)):
    races.append((int(time[i]), int(records[i])))

total = 1

# PART 1: Brute-force approach
for race in races:
    time = race[0]
    record = race[1]
    curr_distance = 0
    amount_wins = 0
    for ms in range(time):
        curr_distance = ms * (time - ms)
        if(curr_distance > record):
            amount_wins += 1
    total *= amount_wins

print(total)
