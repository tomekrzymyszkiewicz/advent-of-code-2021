# wczytuje wszystkie wektory i iteruje po nich szukając tych które mają 1 wspólną składową
# jeśli takie znajdę to dodaje 1 na tablicy field w miejscach gdzie przechodzi dany wektor
# szukam też wektorów idealnie przekątnych (rozpoznaje je po równej różnicy x i y)
# następnie rysuje przekątne w rozpatrująć kąt i kieurnek wektora
# na koniec zliczam pola gdzie wartość jest>= 2

file_name = 'input.txt'
vectors = []
field = []


def main():
    with open(file_name, 'r') as input:
        lines = input.readlines()
        vectors = [[[int(num) for num in end.split(',')] for end in line.strip(
            '\n').split(' -> ')] for line in lines if line is not None]
    max_x = max([max(end[0] for end in vector) for vector in vectors])+1
    max_y = max([max(end[1] for end in vector) for vector in vectors])+1
    field = [[0 for x in range(max_x)] for y in range(max_y)]
    for vector in vectors:
        y_from = min(vector[0][1], vector[1][1])
        y_to = max(vector[0][1], vector[1][1])
        x_from = min(vector[0][0], vector[1][0])
        x_to = max(vector[0][0], vector[1][0])
        x_len = x_to - x_from
        y_len = y_to - y_from
        if vector[0][0] == vector[1][0]:
            for i in range(y_from, y_to+1):
                field[i][vector[0][0]] += 1
        elif vector[0][1] == vector[1][1]:
            for i in range(x_from, x_to+1):
                field[vector[0][1]][i] += 1
        elif x_len == y_len:
            if vector[0][0] < vector[1][0] and vector[0][1] < vector[1][1]:
                x = vector[0][0]
                y = vector[0][1]
                for i in range(x_len+1):
                    field[y][x] += 1
                    x += 1
                    y += 1
            elif vector[1][0] < vector[0][0] and vector[1][1] < vector[0][1]:
                x = vector[1][0]
                y = vector[1][1]
                for i in range(x_len+1):
                    field[y][x] += 1
                    x += 1
                    y += 1
            elif vector[0][0] > vector[1][0] and vector[0][1] < vector[1][1]:
                x = vector[1][0]
                y = vector[1][1]
                for i in range(x_len+1):
                    field[y][x] += 1
                    x += 1
                    y -= 1
            else:
                x = vector[1][0]
                y = vector[1][1]
                for i in range(x_len+1):
                    field[y][x] += 1
                    x -= 1
                    y += 1
    counter = 0
    for line in field:
        counter += len([i for i in line if i >= 2])
    return counter


if __name__ == "__main__":
    print(main())
