file_name = 'input.txt'
fish_list = []


def main(day):
    with open(file_name, 'r') as input:
        lines = input.readline()
        fish_list = [int(num) for num in lines.strip('\n').split(',')]
    for i in range(day):
        for i in range(len(fish_list)):
            fish_list[i] -= 1
            if fish_list[i] == -1:
                fish_list[i] = 6
                fish_list.append(8)
    return fish_list


if __name__ == "__main__":
    print(main(80))
