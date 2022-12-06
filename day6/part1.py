with  open('./day6/input.txt', 'r') as file:
    data = file.read()

i = 0

for i in range(len(data)):
    sgnl = data[i:i+4]
    if len(set(list(sgnl))) == 4:
        print(i + 4)
        break
