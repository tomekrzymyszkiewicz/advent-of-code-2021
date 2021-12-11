file_name = 'input.txt'
levels = []
flashed = []
flash_counter = 0


def main(steps):
    global levels, flashed, flash_counter
    with open(file_name, 'r') as input:
        lines = input.readlines()
        levels = [[int(level) for level in line.strip('\n')] for line in lines]
    for step in range(steps):
        levels = [[int(level+1) for level in line] for line in levels]
        flashed = [[False for level in line] for line in levels]
        for i, line in enumerate(levels):
            for j, level in enumerate(line):
                if level > 9:
                    flash(i, j)
    return flash_counter


def is_in_levels(i, j):
    return i >= 0 and i < len(levels) and j >= 0 and j < len(levels[0])


def flash(i, j):
    global flash_counter, levels, flashed
    if flashed[i][j] == True:
        return
    flashed[i][j] = True
    levels[i][j] = 0
    flash_counter += 1
    adjacency = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j+1],
                 [i+1, j+1], [i+1, j], [i+1, j-1], [i, j-1]]
    for point in adjacency:
        if is_in_levels(point[0], point[1]) and flashed[point[0]][point[1]] == False:
            levels[point[0]][point[1]] += 1
            if levels[point[0]][point[1]] > 9:
                flash(point[0], point[1])


if __name__ == "__main__":
    print(main(100))
