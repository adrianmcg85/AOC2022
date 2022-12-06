with  open('./day6/input.txt', 'r') as file:
    data = file.read()

def signalDetect(signal):
    i = 0

    for i in range(len(data)):
        sgnl = data[i:i+signal]
        if len(set(list(sgnl))) == signal:
            return i + signal
            break
# Part 1
print('Part 1:',signalDetect(4))
# Part 2
print('Part 2:', signalDetect(14))