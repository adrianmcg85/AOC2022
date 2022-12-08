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
ans = 0
for k, v in sizesDict.items():
    if v <= 100000:
        ans += v

print(ans)
