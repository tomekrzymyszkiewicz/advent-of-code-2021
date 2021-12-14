# program wczytuje dane z pliku input.txt i umieszcza każdą liczbę w liście input_list
# iterując od indeksu 2 do końca listy input_list sumuje 3-liczbowe bloki zapisując je w liście sum_list
# iterując listę sum_list od 1 do końca sprawdza czy poprzednia suma jest mniejsza od bieżącej i zlicza takie przypadki
with open('input.txt') as input:
    lines = input.readlines()
input_list = [int(num) for num in lines]
sum_list = [input_list[i-2] + input_list[i-1] + input_list[i] for i in range(2,len(input_list))]
prev_sum = sum_list[0]
count = 0
for i,sum in enumerate(sum_list,1):
    if (sum > prev_sum):
        count += 1;
    prev_sum = sum
print(count)