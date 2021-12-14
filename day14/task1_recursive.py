from collections import Counter
file_name = 'input.txt'
pair_insertion_rules = {}
def main(steps):
    steps -= 1
    lines = [line.strip('\n') for line in open(file_name,'r')]
    polymer_template = lines[0]
    for line in lines[2:]:
        pair_insertion_rules[line.split(' -> ')[0]] = line.split(' -> ')[0][0]+line.split(' -> ')[1]+line.split(' -> ')[0][1]
    separated_polymer_template = []
    for i in range(len(polymer_template)-1):
        separated_polymer_template.append(polymer_template[i:i+2])
    for i,part in enumerate(separated_polymer_template):
        if i < len(separated_polymer_template)-1:
            separated_polymer_template[i] = extend_polymer(steps,part)[0:-1]
        else:
            separated_polymer_template[i] = extend_polymer(steps,part)
    polymer_template = ''.join(separated_polymer_template)
    quantity = Counter(polymer_template)
    return max(quantity.values()) - min(quantity.values())

def extend_polymer(step_to_stop,polymer):
    if step_to_stop < 1:
        return pair_insertion_rules[polymer]
    extended_polymer = pair_insertion_rules[polymer]
    first_part = extend_polymer(step_to_stop-1,extended_polymer[0:2])[0:-1]
    second_part = extend_polymer(step_to_stop-1,extended_polymer[1:])
    return ''.join([first_part,second_part])

if __name__ == "__main__":
    print(main(40))
