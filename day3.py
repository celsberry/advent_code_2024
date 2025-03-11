import re

text_input = ''
with open('day3_input.txt') as f:
    for line in f.readlines():
        text_input += line


# search through the input and find all the matches regex expressions r'mul\(\d{1,3},\d{1,3}\)'
pattern = r'mul\(\d{1,3},\d{1,3}\)'
matches = []
matches = re.findall(pattern, text_input)

print (f"Number of matches: {len(matches)}")
    
# multiply the numbers in each single match entry and add the multipled numbers to the total sum
sum = 0
multipled_list = []
for match in matches:
    temp_list = re.split('\(|,|\)', match)
    sum += int(temp_list[1]) * int(temp_list[2])
    

print (f"Sum: {sum}")

