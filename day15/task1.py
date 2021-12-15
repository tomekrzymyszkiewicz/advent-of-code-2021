import heapq
file_name = 'day15/input.txt'
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


def main():
    for i, line in enumerate(lines):
        for j, point in enumerate(line):
            G[(i, j)] = [[adjacent_point, int(lines[adjacent_point[0]]
                                              [adjacent_point[1]])] for adjacent_point in adjacency(i, j)]
    end_point = (len(lines[0])-1, len(lines)-1)
    return dijkstra(G, (0, 0), end_point)


if __name__ == "__main__":
    print(main())
