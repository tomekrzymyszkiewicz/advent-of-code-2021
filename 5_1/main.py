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
        if vector[0][0] == vector[1][0]:
            y_from = min(vector[0][1], vector[1][1])
            y_to = max(vector[0][1], vector[1][1])
            for i in range(y_from, y_to+1):
                field[i][vector[0][0]] += 1
        if vector[0][1] == vector[1][1]:
            x_from = min(vector[0][0], vector[1][0])
            x_to = max(vector[0][0], vector[1][0])
            for i in range(x_from, x_to+1):
                field[vector[0][1]][i] += 1
    counter = 0
    for line in field:
        counter += len([i for i in line if i >= 2])
    return counter


if __name__ == "__main__":
    print(main())
