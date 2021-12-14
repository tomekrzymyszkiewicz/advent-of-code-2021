file_name = '12_1/input.txt'
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
            if destination in path and destination.islower():
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
