file_name = 'input.txt'


def main():
    dots = []
    folds = []
    paper = []
    with open(file_name, 'r') as input:
        lines = input.readlines()
    index_of_gap = 0
    for i, line in enumerate(lines):
        if line == '\n':
            index_of_gap = i
            break
        else:
            dots.append([int(val) for val in line.strip('\n').split(',')])
    for line in lines[index_of_gap+1:]:
        folds.append(line.lstrip('fold along ').rstrip('\n').split('='))
    folds = [[fold[0], int(fold[1])] for fold in folds]
    max_x = max(x for x, y in dots)
    max_y = max(y for x, y in dots)
    paper = [[False for i in range(max_x+1)] for i in range(max_y+1)]
    for dot in dots:
        paper[dot[1]][dot[0]] = True
    for fold in folds:
        print('fold',fold)
        if fold[0] == 'y':
            for line in range(fold[1]):
                for point in range(len(paper[line])):
                    if 2*fold[1]-line < len(paper):
                        paper[line][point] = paper[line][point] or paper[2*fold[1]-line][point]
            for line in range(fold[1], len(paper)):
                paper.pop()
        if fold[0] == 'x':
            for line in range(len(paper)):
                for point in range(fold[1]):
                    if 2*fold[1]-point < len(paper[line]):
                        paper[line][point] = paper[line][point] or paper[line][2*fold[1]-point]
            for line in range(len(paper)):
                for point in range(fold[1],len(paper[line])):
                    paper[line].pop()
        num_of_dots = 0
        for line in paper:
            for point in line:
                if point == True:
                    num_of_dots += 1
        print('num_of_dots',num_of_dots)
        # for line in paper:
        #     for point in line:
        #         if point == False:
        #             print('.', end='')
        #         else:
        #             print('#', end='')
        #     print('')

if __name__ == "__main__":
    main()
