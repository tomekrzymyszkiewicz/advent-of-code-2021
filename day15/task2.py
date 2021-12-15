import heapq
import itertools
file_name = 'input.txt'
lines = [line.strip('\n') for line in open(file_name, 'r')]
G = {}


def adjacency(i, j):
    return [point for point in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)) if point[0] >= 0 and point[0] < len(lines) and point[1] >= 0 and point[1] < len(lines[0])]


def dijkstra(graph, start, end):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == end:
            return cost
        for v, c in graph[u]:
            if v in visited:
                continue
            next = cost + c
            heapq.heappush(heap, (next, v))
    return -1


def increase_level(num, level): return str(((num+level-1) % 9)+1)


def main():
    initial_size = len(lines[0])
    for i in range(len(lines[0])):
        int_line = [int(val) for val in list(lines[i])]
        new_line = [''.join(
            list(map(increase_level, int_line, itertools.repeat(j)))) for j in range(5)]
        lines[i] = ''.join(new_line)

    for j in range(1, 5):
        for i in range(initial_size):
            int_line = [int(val) for val in list(lines[i])]
            new_line = ''.join(
                list(map(increase_level, int_line, itertools.repeat(j))))
            lines.append(new_line)

    for i, line in enumerate(lines):
        for j, point in enumerate(line):
            G[(i, j)] = [[adjacent_point, int(lines[adjacent_point[0]]
                                              [adjacent_point[1]])] for adjacent_point in adjacency(i, j)]
    end_point = (len(lines[0])-1, len(lines)-1)
    return dijkstra(G, (0, 0), end_point)


if __name__ == "__main__":
    print(main())
