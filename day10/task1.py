file_name = 'input.txt'
lines = []
correct_pairs = {'}': '{', '>': '<', ')': '(', ']': '['}
points = {'}': 1197, '>': 25137, ')': 3, ']': 57, '': 0}


def main():
    with open(file_name, 'r') as input:
        lines = input.readlines()
        lines = [[bracket for bracket in line.strip('\n')] for line in lines]
    sum = 0
    for line in lines:
        sum += points[first_incorrect_bracket(line)]
    return sum


def first_incorrect_bracket(sequence):
    stack = []
    for bracket in sequence:
        if bracket in ('(', '[', '{', '<'):
            stack.append(bracket)
        elif correct_pairs[bracket] == stack[len(stack)-1]:
            stack.pop()
        else:
            return bracket
    return ''


if __name__ == "__main__":
    print(main())
