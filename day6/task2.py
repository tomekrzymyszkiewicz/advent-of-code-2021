file_name = '6_2/input.txt'
fish_list = []
num_of_fishes_in_day = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
days = 8


def main(day):
    with open(file_name, 'r') as input:
        lines = input.readline()
        fish_list = [int(num) for num in lines.strip('\n').split(',')]
    for i in range(days+1):
        num_of_fishes_in_day[i] = fish_list.count(i)
    for i in range(day):
        print(''.join(['Day: ', str(i)]))
        print(num_of_fishes_in_day)
        new_fishes = num_of_fishes_in_day[0]
        for i in range(days):
            num_of_fishes_in_day[i] = num_of_fishes_in_day[i+1]
        num_of_fishes_in_day[8] = new_fishes
        num_of_fishes_in_day[6] += new_fishes
    return sum(num_of_fishes_in_day.values())


if __name__ == "__main__":
    print(main(256))
