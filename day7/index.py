from collections import defaultdict

with  open('./day7/input.txt', 'r') as file:
    data = file.readlines()


sizesDict = defaultdict(int)
path = []
sizes = []
for line in data:
    command = line.strip().split(' ')
    if command[0] == '$' and command[1] == 'cd':
        if command[2] == '..':
            path.pop()
        else:
            path.append(command[2])
    else:
        try:
            size = int(command[0])
            for i in range(1, len(path)+1):
                sizesDict['/'.join(path[:i])] += size
        except:
            pass
p1 = 0

file_space = 70000000
space_required = 30000000
file_thresh = space_required - (file_space - sizesDict['/'])
can_del = []
for k, v in sizesDict.items():
    if v <= 100000:
        p1 += v
    if v >= file_thresh:
        can_del.append(v)
p2 = min(can_del)

for i in sizesDict:
    sizesDict[i]

print('Part 1: ' + str(p1))
print('Part 2: ' + str(p2))
