with  open('./day1/input.txt', 'r') as file:
    data = file.read().split('\n\n')

max = 0

for elf in data:
    cal = 0
    food = elf.split('\n')
    for i in food:
        cal = cal + int(i)
    if(cal > max):
        max = cal

print(max)
