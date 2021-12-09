file_name = '9_1/input.txt'
heightmap = []


def main():
    with open(file_name, 'r') as input:
        lines = input.readlines()
        heightmap = [[[int(num), False]
                      for num in line.strip('\n')] for line in lines]
    for i, line in enumerate(heightmap):
        for j, num in enumerate(line):
            a ,b = i,j
            while True:
                if heightmap[a][b][1] == True:
                    break
                current_value = heightmap[a][b][0]
                left, right, down, up = [9,0,0],[9,0,0],[9,0,0],[9,0,0]
                if b != 0:
                    left = [heightmap[a][b-1][0],a,b-1]
                if b != len(line)-1:
                    right = [heightmap[a][b+1][0],a,b+1]
                if a != 0:
                    up = [heightmap[a-1][b][0],a-1,b]
                if a != len(heightmap)-1:
                    down = [heightmap[a+1][b][0],a+1,b]
                values = [current_value, left[0], right[0], down[0], up[0]]
                if all(v == 9 for v in values):
                    break
                local_min = min(values)
                if local_min == current_value:
                    heightmap[a][b][1] = True
                    print('a',a,'b',b,heightmap[a][b][0])
                    break
                else:
                    if local_min == left[0]:
                        a,b = left[1],left[2]
                    elif local_min == right[0]:
                        a,b = right[1],right[2]
                    elif local_min == up[0]:
                        a,b = up[1],up[2]
                    elif local_min == down[0]:
                        a,b = down[1],down[2]
    # for line in heightmap:
    #     for num in line:
    #         if num[1] == True:
    #             print('#',end='')
    #         else:
    #             print(num[0],end='')
    #     print(' ')
    sum = 0
    for line in heightmap:
        for num in line:
            if num[1] == True:
                sum += num[0]+1
    return sum


if __name__ == "__main__":
    print(main())
