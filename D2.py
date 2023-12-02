# only 12 red cubes, 13 green cubes, and 14 blue cubes
from sys import stdin

file = open("input.txt", "r")


sum = 0

while line := file.readline():
    games =line.split(":")[1].split(";")
    x = [game.strip() for game in games]
    print(x)
    currMinRed = 0
    currMinBlue = 0
    currMinGreen = 0
    for game in games:
        cubes = [ob.strip() for ob in x]
        #Highest number of cubes ina game that still does not more that max.
        sets = []
        for set in cubes:
            temp = set.split(",")
            for obj in temp:
                obj = obj.strip()
                amount = obj[0:2]
                color = obj[2:].strip()
                #Break if amount ever exceeds given amount
                if color == 'red' and int(amount) > currMinRed:
                    currMinRed = int(amount)
                if color == 'blue' and int(amount) > currMinBlue:
                    currMinBlue = int(amount)
                if color == 'green' and int(amount) > currMinGreen:
                    currMinGreen = int(amount)
    sum += currMinRed*currMinGreen*currMinBlue
    print(sum)
    
print(sum)
file.close()
    



#for lines in stdin:
#    print(lines)