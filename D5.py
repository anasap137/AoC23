file = open("input.txt", "r")
seeds = file.readline().split(":")[1].strip().split(" ")
 
seedsCopy = []

for i in range(2,len(seeds) + 1):
    if i % 2 == 0:
        subSeeds = seeds[:i]
        seeds = seeds[i:]
        seedsCopy.append(subSeeds) 

#1 - seed to soil
#2 - soil to fertilizer
#3 - fertilizer to water
#4 water to light
#5 light to temperature
#6 temperature to humidity
#7 humidity to location
input = file.readlines()

mapped_values = []
current_map = None

for item in input:
    if item.startswith('\n'):
        continue
    elif item.endswith(':\n'):
        current_map = [item.strip(), []]
        mapped_values.append(current_map)
    else:
        current_map[1].append(item.strip())

curr_lowest_location = 100000000000000


for seed_range in seedsCopy:
    for seed in range(int(seed_range[0]), int(seed_range[0]) + int(seed_range[1])):
    
        curr_value = seed
        for stage in mapped_values: #Go through all stages
            ranges = stage[1]
            value_in_range = False
            for value in ranges:
                if value_in_range:
                    continue
                destination_id_start, source_id_start, length = value.split(" ")
                curr_range = range(int(source_id_start), (int(source_id_start) + int(length)))
                if curr_value in curr_range:
                    value_in_range = True
                    if int(source_id_start) > int(destination_id_start):
                        curr_value -= abs(int(destination_id_start) - int(source_id_start))
                        continue
                    elif int(source_id_start) < int(destination_id_start):
                        curr_value += abs(int(destination_id_start) - int(source_id_start))
                        continue
                    else: # If they are the same
                        continue
        print("Calculated location for seed ", seed)
        if curr_value < curr_lowest_location:
            
            curr_lowest_location = curr_value
file.close()

print(curr_lowest_location)
    
                




