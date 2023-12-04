
file = open("input.txt", "r")

#Create 2 lists, winning numbers - numbers I have
# For each of my num, check if it is in winning numbers, increase counter
# double 1 n times, return sum!

game_index = 0
total_sc = [] #(index, amount)



while line := file.readline():
    total_sc.append([game_index, 1])
    game_index += 1

file.close()

file = open("input.txt", "r")
curr_game_index = 0

while line := file.readline():
    score = 0
    winning_nums = []
    my_nums = []

    winning_nums, my_nums = line.split(":")[1].strip().split("|")
    winning_nums = winning_nums.strip().split(" ")
    my_nums = my_nums.strip().split(" ")
    
    for num in my_nums:
        if not num:
            continue
        if num in winning_nums:
            score += 1

    for i in range(1,score + 1):
        total_sc[curr_game_index + i][1] += 1 * total_sc[curr_game_index][1] #Add copy to following card
    curr_game_index += 1 #increase row index

total_sum = 0
for card in total_sc:
    total_sum += card[1]
print(total_sum)
    
    
    
    


