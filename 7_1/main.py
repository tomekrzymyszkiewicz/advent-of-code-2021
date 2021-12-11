file_name = 'input.txt'
crab_list = []


def main():
    with open(file_name, 'r') as input:
        line = input.readline()
        crab_list = [int(num) for num in line.strip('\n').split(',')]
    pos_fuel = [0 for i in range(max(crab_list))]
    for i in range(len(pos_fuel)):
        pos_fuel[i] = sum([abs(crab - i) for crab in crab_list])
    return (pos_fuel.index(min(pos_fuel)), min(pos_fuel))


if __name__ == "__main__":
    print(main())
