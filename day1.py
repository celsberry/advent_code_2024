with open('Day1_input.txt') as f:
    lines = f.readlines()


first_list = []
second_list = []
for line in lines:
    line_array = line.split("   ")
    first_list.append(line_array[0])
    second_list.append(line_array[1].split()[0])

first_list.sort()
second_list.sort()

sum = 0
for index, (first, second) in enumerate(zip(first_list, second_list)):
    diff = abs(int(second) - int(first))
    sum += diff

print (f"Sum: {sum}")

similarity_score = 0
for first in first_list:
    count = 0
    for second in second_list:
        if first == second:
            count += 1
    similarity_score += (int(first) * count)
    

print (f"Similarity Score: {similarity_score}")