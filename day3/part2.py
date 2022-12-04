import string  

with  open('./day3/input.txt', 'r') as file:
    data = file.read().split('\n')

letters = string.ascii_lowercase + string.ascii_uppercase
output = 0
e = 3

for i in range(0, len(data), 3):
    rucksacks = data[i:e]
    e += 3
    c1, c2, c3 = set(rucksacks[0]), set(rucksacks[1]), set(rucksacks[2])
    for priortiy, char in enumerate(letters):
        if char in c1 and char in c2 and char in c3:
            output += priortiy + 1
print(output)