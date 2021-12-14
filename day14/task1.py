from collections import Counter
file_name = 'input.txt'

def main(steps):
    lines = [line.strip('\n') for line in open(file_name,'r')]
    polymer_template = lines[0]
    pair_insertion_rules = {}
    for line in lines[2:]:
        pair_insertion_rules[line.split(' -> ')[0]] = line.split(' -> ')[0][0]+line.split(' -> ')[1]+line.split(' -> ')[0][1]
    for step in range(steps):
        print(step)
        separated_polymer_template = []
        for i in range(len(polymer_template)-1):
            separated_polymer_template.append(polymer_template[i:i+2])
        for i,part in enumerate(separated_polymer_template):
            separated_polymer_template[i] = pair_insertion_rules[part]
            if i < len(separated_polymer_template)-1:
                separated_polymer_template[i] = separated_polymer_template[i][0:-1]
        polymer_template = ''.join(separated_polymer_template)
    quantity = Counter(polymer_template)
    return max(quantity.values()) - min(quantity.values())
if __name__ == "__main__":
    print(main(10))
