with open('Day2_input.txt') as f:
    lines = f.readlines()


report_sum = 0
for line in lines:
    line_array = line.rstrip().split(" ")
    
    count = 0
    single_bad_level_detected = False
    #if second number is greater than first number (greater than one but not exceeding 3) then check if all following numbers are consistently greater by one but not exceeding 3
    if int(line_array[1]) > int(line_array[0]):
        if abs(int(line_array[1]) - int(line_array[0])) <= 3:
            for index in range(2, len(line_array)):
                if int(line_array[index]) > int(line_array[index-1]):
                    if abs(int(line_array[index]) - int(line_array[index-1])) <= 3:
                        count = 1  
                    else:
                        count = 0
                        break                  
                else:
                    count = 0
                    break
    # if second number is less than first number (less than one but not exceeding less than 3) then check if all following numbers are consistently less than one but not exceeding less than 3
    elif int(line_array[1]) < int(line_array[0]):
        if abs(int(line_array[1]) - int(line_array[0])) <= 3:
            for index in range(2, len(line_array)):
                if (int(line_array[index]) < int(line_array[index-1])):
                    if abs(int(line_array[index]) - int(line_array[index-1])) <= 3:
                        count = 1
                    else:
                        count = 0
                        break                     
                else:
                    count = 0
                    break

    report_sum += count         

print (f"Report Sum: {report_sum}")