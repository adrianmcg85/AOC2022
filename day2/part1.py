with  open('./day2/input.txt', 'r') as file:
    tournament = file.read().split('\n')


rps_map = {
    'A X' : 4, 'A Y' : 8, 'A Z' : 3,
    'B X' : 1, 'B Y' : 5, 'B Z' : 9,
    'C X' : 7, 'C Y' : 2, 'C Z' : 6    
}
score = 0
for game in tournament:
    score = score + rps_map[game]
print(score)
