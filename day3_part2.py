import re

text_input = ''
with open('day3_input.txt') as f:
    for line in f.readlines():
        text_input += line


# search through the input and find all the matches regex expressions "mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
matches = []
matches = re.findall(pattern, text_input)

print (f"Number of matches: {len(matches)}")

# process the list based on the valid instruction `do()` or `don't()` that is found prior to the `mul()` instruction
sum = 0
valid = True
for match in matches:
    if match == 'do()':
        valid = True
    elif match == 'don\'t()':
        valid = False
    elif valid:
        curr_nums = re.findall(r'\d{1,3}', match)
        sum += int(curr_nums[0]) * int(curr_nums[1])
    

print (f"Sum: {sum}")

