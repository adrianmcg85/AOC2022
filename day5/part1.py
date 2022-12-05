with  open('./day5/input.txt', 'r') as file:
    data = file.read().split('\n\n')

# Build stacks
stacks = []
drawing = data[0].split('\n')
stacks = [[] for _ in range(9)]
lines = len(drawing)-1
for i in range(lines):
    line = drawing[i]
    crate = line[1::4]
    for s in range(len(crate)):
        if crate[s] != ' ':
            stacks[s].append(crate[s])


for row in data[1].split('\n'):
    split = row.split(' ')
    move, from_stack, to_stack = [int(split[1]), int(split[3])-1, int(split[5])-1]
    for _ in range(move):
        item = stacks[from_stack].pop(0)
        stacks[to_stack].insert(0, item)

code = ''
for stack in stacks:
    code += stack[0]

print(code)