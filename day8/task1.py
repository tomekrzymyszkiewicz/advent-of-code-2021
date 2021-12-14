file_name = 'input.txt'
values = []


def main():
    with open(file_name, 'r') as input:
        lines = input.readlines()
        values = [[[sequence.strip(' ') for sequence in segment.split(' ') if sequence.strip(
            ' ') != ''] for segment in line.strip('\n').split('|')] for line in lines]
    counter = 0
    for line in values:
        for sequence in line[1]:
            if len(sequence) == 2 or len(sequence) == 3 or len(sequence) == 4 or len(sequence) == 7:
                counter += 1
    return counter


if __name__ == "__main__":
    print(main())
