import time
import math

starttime = time.time()
total = 0

# def invalid_id(value):
#     length = len(value);
    
#     for x in range(length):
#         divide = length//x;
#         if divide == length/x: ## check for round division
#             list = set()
#             value  = str(value)
#             ##### AAAAAAAAAAAAAAA create for loop to add all segments
#             for 
#             ## add edge case for single length
#             segment = math.floor(len(value)/2)
            
#             if segment in list:
#                 return False;
#             else:
#                 list.add(segment);
#     return True

def invalid_id(value):
    # https://www.geeksforgeeks.org/python/python-check-if-string-repeats-itself/
    # ik fucking haat deze opdracht
    return value in (value + value)[1:-1]


# MAIN

filename = "input.txt"
# filename = "input_test.txt"

with open(filename) as file:
    for line in file:
        output = line.split(',');
        # output is now an array with all entries seperated.
        for y in output:
            total_range = y.split('-');
            start = int(total_range[0])
            end = int(total_range[1])
            for var_number in range(start, end):
                if invalid_id(str(var_number)):
                    # print(var_number)
                    total += var_number;
                # total += invalid_id(str(var_number));
                # str_number  = str(var_number)
                # first_half  = math.floor(len(str_number)/2)
                # second_half = math.floor(len(str_number));
                # first_number  = (str_number[:first_half])
                # second_number = (str_number[first_half:])
                # if first_number == second_number:
                #     total = total + var_number

endtime = time.time()
print("The output is number: ", total);
print("Program took: ", endtime-starttime, " seconds");