file = open("input.txt", "r")

def allZero(list):
    for elem in list:
        if elem != 0:
            return False
    return True

def find_value(list):
    differences = []
    test = True
    differences.append(list)
    while test:
        currlist = []
        for i in range(len(list) - 1):
            sub = int(list[i+1]) - int(list[i+1])
            currlist.append(sub)
        #Check if all elements are zero
        if allZero(currlist):
            differences.append(currlist)
            test=False
            continue
        differences.append(currlist)
        list = currlist
    #print("List ", "Sublist: ", differences)
    # Sum all last elements of sublists, 
    # last element = previous last element + second last in current

    for i in range(1, len(differences)):
        secondLast = differences[-1 - i]
        last = differences[-i]
        new_last = secondLast[-1] + last[-1]
        secondLast.append(new_last)  
        if i == len(differences) -1:
            return new_last


total_sum = 0

while line := file.readline().strip():
    numbers = line.split(" ")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    print( "Number ", numbers)
    summa = find_value(numbers)
    total_sum += summa

print(total_sum)