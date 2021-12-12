file_name = 'input.txt'
edges = [line.strip('\n').split('-') for line in open(file_name, 'r')]
possible_moves = {}
for x, y in edges:
    for a, b in ((x, y), (y, x)):
        possible_moves[a] = possible_moves[a] + \
            [b] if possible_moves.get(a) else [b]


def main():
    print(visit('start', [], []))


def check_double_small_cave(visited):
    for i in visited:
        if i != 'start' and i.islower() and visited.count(i) > 1:
            return i
    return None


def visit(path, visited, paths):
    global possible_moves
    if path == 'end':
        paths.append([*visited, 'end'])
        return
    if path.islower() and path in visited:
        if path == 'start' or check_double_small_cave(visited):
            return
    visited = [*visited, path]
    for possible_move in possible_moves[path]:
        visit(possible_move, visited, paths)
    return len(paths)


if __name__ == "__main__":
    main()
