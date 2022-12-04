import string  

with  open('./day3/input.txt', 'r') as file:
    data = file.read().split('\n')

letters = string.ascii_lowercase + string.ascii_uppercase
output = 0

for rucksack in data:

    half = len(rucksack)//2
    c1, c2 = set(rucksack[:half]), set(rucksack[half:])
    for priortiy, char in enumerate(letters):
        if char in c1 and char in c2:
            output += priortiy + 1
print(output)