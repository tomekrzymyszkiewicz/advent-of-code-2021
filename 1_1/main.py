with open('input.txt') as input:
    lines = input.readlines()
input_list = [int(num) for num in lines]
prev_num = input_list[0]
count = 0
for i,num in enumerate(input_list,1):
    if (num > prev_num):
        count += 1;
    prev_num = num
print(count)