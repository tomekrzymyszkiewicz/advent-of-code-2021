file_name = '10_2/input.txt'
lines = []
scores = []
correct_pairs ={'}':'{','>':'<',')':'(',']':'['}
missing_points = {'(':1,'[':2,'{':3,'<':4}
points = {'}':1197,'>':25137,')':3,']':57,'':0}
def main():
    with open(file_name, 'r') as input:
        lines = input.readlines()
        lines = [[bracket for bracket in line.strip('\n')] for line in lines]
    sum = 0
    for line in lines:
        check_val = first_incorrect_bracket(line)
        if type(check_val) == list:
            current_sum = 0
            for bracket in reversed(check_val):
                current_sum *= 5
                current_sum += missing_points[bracket]
            scores.append(current_sum)
    scores.sort()
    return scores[int(len(scores)/2)]
    
    
def first_incorrect_bracket(sequence):
    stack = []
    for bracket in sequence:
        if bracket in ('(','[','{','<'):
            stack.append(bracket)
        elif correct_pairs[bracket] == stack[len(stack)-1]:
            stack.pop()
        else:
            return bracket
    if len(stack) == 0:
            return ''
    else:
        return stack
if __name__ == "__main__":
    print(main())
