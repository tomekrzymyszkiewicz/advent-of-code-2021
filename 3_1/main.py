# wczytuje wszystkie liczby, usuwam znaki \n i konwertuje do liczb dziesiętynch
# tworze listy zliczajace zera i jedynki
# w pętli iteruje po każdym bicie i dla wszystkich liczb zliczam jedynki i zera na i-tej pozycji
# tworze liste gamma i epsilon gdzie wpisuje zera lub jedynki w zależności których bitów było więcej w inpucie
# odwracam listy i konweruje do intów któe po wymnożeniu wypisuje
with open('input.txt') as input:
    numbers_input = input.readlines()
numbers_binary = [int(number.strip('\n'),2) for number in numbers_input]
ones = [0]*len(numbers_input[0].strip('\n'))
zeros = [0]*len(numbers_input[0].strip('\n'))
for i in range(len(numbers_input[0].strip('\n'))):
    for num in numbers_binary:
        if num>>i & 1:
            ones[i] += 1
        else:
            zeros[i] += 1

gamma = []
epsilon = []

for i in range(len(ones)):
    if ones[i] > zeros[i]:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)
gamma.reverse()
epsilon.reverse()

gamma_num = int(''.join([str(bit) for bit in gamma]),2)
epsilon_num = int(''.join([str(bit) for bit in epsilon]),2)

print(gamma_num*epsilon_num)