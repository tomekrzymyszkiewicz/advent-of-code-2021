from collections import Counter

file_name = '12_2/input.txt'
edges = []
paths = []


def main():
    edges = [line.strip('\n').split('-') for line in open(file_name, 'r')]
    for edge in edges:
        if 'start' in edge:
            if edge[0] == 'start':
                path = [edge[0], edge[1]]
            else:
                path = [edge[1], edge[0]]
            paths.append(path)
    for path in paths:
        print(len(paths))
        end_of_path = path[-1]
        if end_of_path == 'end':
            continue
        for edge in edges:
            if edge[0] == end_of_path:
                destination = edge[1]
            elif edge[1] == end_of_path:
                destination = edge[0]
            else:
                continue
            if 'start' in edge:
                continue
            number_of_lowercases = Counter([point for point in path if point.islower() and not point in ('start','end')])
            number_of_lowercases[destination] += 1
            if number_of_lowercases[destination] > 2:
                continue
            if len([num_of_lowers for num_of_lowers in number_of_lowercases.values() if num_of_lowers > 1]) > 1:
                continue
            else:
                new_path = path.copy()
                new_path.append(destination)
                if not new_path in paths:
                    paths.append(new_path)

    result = [path for path in paths if path[-1] == 'end']

    for path in result:
        for point in path:
            if point != path[-1]:
                print(point, end='')
                print(',', end='')
            else:
                print(point, end='')
        print('')
    print(len(result))


if __name__ == "__main__":
    main()
