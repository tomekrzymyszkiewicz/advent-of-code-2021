file_name = 'input.txt'

def main(steps):
    pair_insertion_rules = {}   
    sub_polymers_quantity = {}
    lines = [line.strip('\n') for line in open(file_name,'r')]
    polymer_template = lines[0]
    for line in lines[2:]:
        pair_insertion_rules[line.split(' -> ')[0]] = line.split(' -> ')[0][0]+line.split(' -> ')[1]+line.split(' -> ')[0][1]
        sub_polymers_quantity[line.split(' -> ')[0]] = 0
    for i in range(len(polymer_template)-1):
        pair = polymer_template[i:i+2]
        sub_polymers_quantity[pair] += 1
    for i in range(steps):
        new_sub_polymers_quantity = sub_polymers_quantity.copy()
        for pair in sub_polymers_quantity:
            if sub_polymers_quantity[pair] > 0:
                new_sub_polymers_quantity[pair] -= sub_polymers_quantity[pair]
                first_new_pair = pair_insertion_rules[pair][:2]
                second_new_pair = pair_insertion_rules[pair][1:]
                new_sub_polymers_quantity[first_new_pair] += sub_polymers_quantity[pair]
                new_sub_polymers_quantity[second_new_pair] += sub_polymers_quantity[pair]
        sub_polymers_quantity = new_sub_polymers_quantity
    letters_quantity = {}
    for pair in sub_polymers_quantity:
        letters_quantity[pair[0]] = 0
    for pair in sub_polymers_quantity:
        letters_quantity[pair[0]] += sub_polymers_quantity[pair]
    letters_quantity[polymer_template[-1]] += 1
    return max(letters_quantity.values()) - min(letters_quantity.values())



if __name__ == "__main__":
    print(main(40))
