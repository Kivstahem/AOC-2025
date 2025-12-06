# D6: calculate for the poor elfs
# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  
# each item to calculate is in a column and not a row, so either load in the data and flip it or deal with it...?
# partial loading can also be done, but that confuses me

import time
import numpy as np
starttime = time.time()

def load_data(filename):
    with open(filename) as file:
        # for line in file:
        data = [line.split() for line in file]
        array = np.array(data);
        return array.T
    
def load_data_KUT(filename): # part two load in data (absolutely horrid I hate it with a passion)
    col = []
    # row = []
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "-");
            line = line.replace(" ", "-")
            col.append(line)
    
    check_case = "-" * (len(col)-1)
    index = 0;
    temp_array = []
    output = []
    for x in range(len(col[0])):
        temp = "";
        for i in range(len(col)-1):
            temp += col[i][x]
        if index == 0:
            operator = col[i+1][x]
        index += 1
        if temp == check_case:
            temp_array.append(operator)
            output.append(temp_array);
            temp_array = []
            index = 0;
        else:
            temp_array.append(temp.strip("-"));
    return output

def calculator(array):
    temp_calc = 0;
    length_array = len(array)-1;
    if array[length_array] == "*": # multiplication
        temp_calc = int(array[0]) * int(array[1]);
        for i in range(2,len(array)-1):
            temp_calc = temp_calc * int(array[i]);
        return temp_calc
    elif array[length_array] == "+": # multiplication
        for i in range(length_array):
            temp_calc = temp_calc + int(array[i]);
        return temp_calc
    else:
        print("I DONT RECOGNISE THIS CHARACTER!", array[len(array)])
        return 0
    
# MAIN
# filename = "input_test.txt"
filename = "input.txt"
total_calculated = 0;
# array = load_data(filename);
array = load_data_KUT(filename)

for i in range(len(array)):
    total_calculated = total_calculated + calculator(array[i])

endtime = time.time()

print("total calculatd items: ", total_calculated);
print("Program took: ", (endtime-starttime)*1000, " ms");
