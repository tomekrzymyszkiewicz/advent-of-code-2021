file_name = 'input.txt'
heightmap = []
basin_sizes = []


def main():
    with open(file_name, 'r') as input:
        lines = input.readlines()
        heightmap = [[[int(num), False, False]
                      for num in line.strip('\n')] for line in lines]
    for i, line in enumerate(heightmap):
        for j, num in enumerate(line):
            a, b = i, j
            while True:
                if heightmap[a][b][1] == True:
                    break
                current_value = heightmap[a][b][0]
                left, right, down, up = [9, 0, 0], [
                    9, 0, 0], [9, 0, 0], [9, 0, 0]
                if b != 0:
                    left = [heightmap[a][b-1][0], a, b-1]
                if b != len(line)-1:
                    right = [heightmap[a][b+1][0], a, b+1]
                if a != 0:
                    up = [heightmap[a-1][b][0], a-1, b]
                if a != len(heightmap)-1:
                    down = [heightmap[a+1][b][0], a+1, b]
                values = [current_value, left[0], right[0], down[0], up[0]]
                if all(v == 9 for v in values):
                    break
                local_min = min(values)
                if local_min == current_value:
                    heightmap[a][b][1] = True
                    break
                else:
                    if local_min == left[0]:
                        a, b = left[1], left[2]
                    elif local_min == right[0]:
                        a, b = right[1], right[2]
                    elif local_min == up[0]:
                        a, b = up[1], up[2]
                    elif local_min == down[0]:
                        a, b = down[1], down[2]
    for i, line in enumerate(heightmap):
        for j, num in enumerate(line):
            if num[1] == True:
                local_basin_points = [[i, j]]
                heightmap[i][j][2] = True
                while True:
                    new_point = False
                    for basin_point in local_basin_points:
                        left, right, down, up = [9, 0, 0], [
                            9, 0, 0], [9, 0, 0], [9, 0, 0]
                        if basin_point[1] != 0:
                            if heightmap[basin_point[0]][basin_point[1]-1][0] != 9 and not heightmap[basin_point[0]][basin_point[1]-1][2]:
                                local_basin_points.append(
                                    [basin_point[0], basin_point[1]-1])
                                new_point = True
                                heightmap[basin_point[0]
                                          ][basin_point[1]-1][2] = True
                        if basin_point[1] != len(line)-1:
                            if heightmap[basin_point[0]][basin_point[1]+1][0] != 9 and not heightmap[basin_point[0]][basin_point[1]+1][2]:
                                local_basin_points.append(
                                    [basin_point[0], basin_point[1]+1])
                                new_point = True
                                heightmap[basin_point[0]
                                          ][basin_point[1]+1][2] = True
                        if basin_point[0] != 0:
                            if heightmap[basin_point[0]-1][basin_point[1]][0] != 9 and not heightmap[basin_point[0]-1][basin_point[1]][2]:
                                local_basin_points.append(
                                    [basin_point[0]-1, basin_point[1]])
                                new_point = True
                                heightmap[basin_point[0] -
                                          1][basin_point[1]][2] = True
                        if basin_point[0] != len(heightmap)-1:
                            if heightmap[basin_point[0]+1][basin_point[1]][0] != 9 and not heightmap[basin_point[0]+1][basin_point[1]][2]:
                                local_basin_points.append(
                                    [basin_point[0]+1, basin_point[1]])
                                new_point = True
                                heightmap[basin_point[0] +
                                          1][basin_point[1]][2] = True
                    if not new_point:
                        break
                basin_sizes.append(len(local_basin_points))
    basin_sizes.sort(reverse=True)
    return basin_sizes[0]*+ basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    print(main())
