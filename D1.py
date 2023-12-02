# get number from first and last digit, create two-digit number
    #If one number in string, create two-digit number by adding same number again
#Summarize all two-number digits from each row

file = open("input.txt", "r")

counter = 0 # 2 per line
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] # index + 1 corresponding integer


sum = 0

while(True):
    line = file.readline()
    if not line:
        break

    tmpStr = ''
    digits = ''

    for char in line:
        if char.isdigit():
            digits += char   
            continue
        tmpStr += char
        currIndex = 1
        if len(tmpStr) >= 3:
            for num in numbers: 
                if num in tmpStr:
                    digits += str(currIndex)
                    tmpStr = tmpStr[-1:]
                    break
                currIndex += 1

    if len(digits) == 1: # handle single integers
       digits += digits[0]
       sum +=int(digits)
    else:
        first = digits[0]
        last = digits[-1]
        digits = first + last
        sum +=int(digits)


print(sum)

file.close()
