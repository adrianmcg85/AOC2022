with  open('./day2/input.txt', 'r') as file:
    tournament = file.read().split('\n')


rps_map = {
    'A X' : 3, 'A Y' : 4, 'A Z' : 8,
    'B X' : 1, 'B Y' : 5, 'B Z' : 9,
    'C X' : 2, 'C Y' : 6, 'C Z' : 7    
}
score = 0
for game in tournament:
    score = score + rps_map[game]
print(score)
