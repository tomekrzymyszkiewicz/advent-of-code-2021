file_name = '8_2/input.txt'
values = []

def main():
    with open(file_name, 'r') as input:
        lines = input.readlines()
        values = [[[sequence.strip(' ') for sequence in segment.split(' ') if sequence.strip(' ') != ''] for segment in line.strip('\n').split('|')] for line in lines]
    sum = 0
    for i,line in enumerate(values):
        dictionary = {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
        for sequence in line[0]:
            if len(sequence) == 2:
                dictionary[1] = sequence
            elif len(sequence) == 3:
                dictionary[7] = sequence
            elif len(sequence) == 4:
                dictionary[4] = sequence
            elif len(sequence) == 7:
                dictionary[8] = sequence
        while min([len(item) for item in dictionary.values()]) == 0:
            for sequence in line[0]:
                if len(sequence) == 5: #2 3 or 5
                    if all(item in sequence for item in dictionary[7]): 
                        dictionary[3] = sequence
                    elif all(item in dictionary[9] for item in sequence): 
                        dictionary[5] = sequence
                    elif dictionary[9] != '':    
                        dictionary[2] = sequence
                elif len(sequence) == 6: #0 9 or 6
                    if all(item in sequence for item in dictionary[4]): # 4 in 9
                        dictionary[9] = sequence
                    elif all(item in sequence for item in dictionary[7]): # 7 in 0
                        dictionary[0] = sequence
                    elif dictionary[7] != '':
                        dictionary[6] = sequence
        number = []
        for sequence in line[1]:
            if all(item in dictionary[0] for item in sequence) and len(sequence) == len(dictionary[0]):
                number.append(0)
            elif all(item in dictionary[1] for item in sequence) and len(sequence) == len(dictionary[1]):
                number.append(1)
            elif all(item in dictionary[2] for item in sequence) and len(sequence) == len(dictionary[2]):
                number.append(2)
            elif all(item in dictionary[3] for item in sequence) and len(sequence) == len(dictionary[3]):
                number.append(3)
            elif all(item in dictionary[4] for item in sequence) and len(sequence) == len(dictionary[4]):
                number.append(4)
            elif all(item in dictionary[5] for item in sequence) and len(sequence) == len(dictionary[5]):
                number.append(5)
            elif all(item in dictionary[6] for item in sequence) and len(sequence) == len(dictionary[6]):
                number.append(6)
            elif all(item in dictionary[7] for item in sequence) and len(sequence) == len(dictionary[7]):
                number.append(7)
            elif all(item in dictionary[8] for item in sequence) and len(sequence) == len(dictionary[8]):
                number.append(8)
            elif all(item in dictionary[9] for item in sequence) and len(sequence) == len(dictionary[9]):
                number.append(9)
        current_sum = int("".join(str(i) for i in number))
        sum += current_sum
    return sum

if __name__ == "__main__":
    print(main())
