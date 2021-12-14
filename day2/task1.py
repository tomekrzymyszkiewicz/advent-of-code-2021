# wczytuje linie pliku i tworze listę par [rodzaj ruchu,wartość ruchu]
# następnie dla każdego ruchu sprawdzam jego rodzaj i dodaje wartość do zmiennych sumujących pozycję
#na koniec wypisuje iloczyn składowych
with open('input.txt') as input:
    lines = input.readlines()
input_list = [line.strip('\n').split(' ') for line in lines]
pos = 0
depth = 0
for move in input_list:
    if move[0] == 'forward':
        pos += int(move[1])
    elif move[0] == 'down':
        depth += int(move[1])
    elif move[0] == 'up':
        depth -= int(move[1])
print(pos*depth)