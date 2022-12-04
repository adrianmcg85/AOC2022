with  open('./day4/input.txt', 'r') as file:
    data = file.read().split('\n')

output = 0
for pair in data:
    p1, p2 = pair.split(',')
    p1_start, p1_end = p1.split('-')
    p2_start, p2_end = p2.split('-')
    if (int(p1_start) <= int(p2_start) and int(p1_end) >= int(p2_end)):
        output += 1
    elif (int(p2_start) <= int(p1_start) and int(p2_end) >= int(p1_end)):
        output += 1
print(output)