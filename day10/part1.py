with  open('./day10/input.txt', 'r') as file:
    data = file.read().split('\n')

x = 1
c = 0
output = 0

readings = [20,60,100,140,180,220]

for line in data:
    if line == 'noop':
        c += 1
        if c in readings:
            output += c * x
        
    else:
        v = int(line.split(' ')[1])
        x += v
        c +=1
        if c in readings:
            output += c * (x-v)
        c += 1
        if c in readings:
            output += c * (x-v)

print(output)