# wczytuje wszystkie liczby, usuwam znaki \n i konwertuje do liczb dziesiętynch
# tworze listy zliczajace zera i jedynki
# w pętli iteruje po każdym bicie i dla wszystkich liczb zliczam jedynki i zera na i-tej pozycji
# tworze na nowo liste liczb bez liczb które na i tej pozycji mają niedominujący bit
# pobeiram jedyny element jaki został
# powtarzam to dla dominującego zera
#wypisuje iloczyn otrzymanych liczb
file_name = '3_2/input.txt'
with open(file_name) as input:
    numbers_input = input.readlines()
numbers_binary = [int(number.strip('\n'), 2) for number in numbers_input]
line_len = len(numbers_input[0].strip('\n'))
ones = [0]*line_len
zeros = [0]*line_len
for i in range(line_len):
    if len(numbers_binary) != 1:
        for num in numbers_binary:
            if (num >> (line_len-i-1) & 1):
                ones[i] += 1
            else:
                zeros[i] += 1
        if ones[i] >= zeros[i]:
            numbers_binary = [num for num in numbers_binary if (
                num >> (line_len-i-1) & 1)]
        else:
            numbers_binary = [num for num in numbers_binary if not (
                num >> (line_len-i-1) & 1)]
oxygen = numbers_binary[0]
            
with open(file_name) as input:
    numbers_input = input.readlines()
numbers_binary = [int(number.strip('\n'), 2) for number in numbers_input]
line_len = len(numbers_input[0].strip('\n'))            
ones = [0]*line_len
zeros = [0]*line_len
for i in range(line_len):
    if len(numbers_binary) != 1:
        for num in numbers_binary:
            if (num >> (line_len-i-1) & 1):
                ones[i] += 1
            else:
                zeros[i] += 1
        if ones[i] >= zeros[i]:
            numbers_binary = [num for num in numbers_binary if not(
                num >> (line_len-i-1) & 1)]
        else:
            numbers_binary = [num for num in numbers_binary if  (
                num >> (line_len-i-1) & 1)]          
            
co2 = numbers_binary[0]
            
print(oxygen*co2)

