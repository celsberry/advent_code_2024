
rules: dict[int, set] = {}
updates = []
bad_updates = []

valid_middle_number_sum = 0

def parse_input(lines):
    # check to if the input has a pip symbol if it does then add it to a dictionary
    # then for for an empty new line to know the remainiing lines need to be added to a list as a list
    for line in lines:
        if '|' in line:
            items = line.replace('\n','').split('|')
            try:
                rules[int(items[0])].add(items[1])
            except KeyError:
                rules[int(items[0])] = set([items[1]])
        elif line == '\n':
            continue
        else:
            this_line = [int(x) for x in line.replace('\n','').split(',')]
            updates.append(this_line)


def check_updates_against_rules():
    middle_number_sum = 0
    count = 0
    for update in updates:
        if validate_update(update):
            count += 1
            middle_number_sum += int(update[len(update)//2])
 
    return middle_number_sum, count

# check if the update is valid based off of the rules
def validate_update(update):
    valid = True
    for i in range(len(update) - 1, 0, -1):
        print(f" key: {update[i]}; update[:i]: {update[:i]}")
        try:
            if not rules[update[i]].isdisjoint(set(update[:i])):
                valid = False
                bad_updates.append(update)
                break
        except KeyError:
            print(f"#### KeyError hit for {update[i]} ####")
            continue

    return valid
        

with open('day5_input_sample.txt') as f:
    lines = f.readlines()


parse_input(lines)

valid_middle_number_sum, valid_count = check_updates_against_rules()

print(f"number of valid middle numbers: {valid_count}")
print(valid_middle_number_sum)
