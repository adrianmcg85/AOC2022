with  open('./day1/input.txt', 'r') as file:
    data = file.read().split('\n\n')

top3 = []

for elf in data:
    cal = 0
    food = elf.split('\n')
    for i in food:
        cal = cal + int(i)
    if(len(top3) < 3):
        top3.append(cal)
    elif(cal > min(top3)):
        top3.remove(min(top3))
        top3.append(cal)
    

print(sum(top3))