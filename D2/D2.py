import time
import math
import csv

starttime = time.time()
total = 0

# def dial(dial_current, number):
#     new_dial_mod = 1
#     return new_dial_mod

with open("input.txt") as file:
    for line in file:
        output = line.split(',');
        # output is now an array with all entries seperated.
        for y in output:
            total_range = y.split('-');
            print(y)
            print(total_range)
            start = int(total_range[0])
            end = int(total_range[1])
            print(start)
            print(end)
            for var_number in range(start, end):
                str_number  = str(var_number)
                first_half  = math.floor(len(str_number)/2)
                second_half = math.floor(len(str_number));
                first_number  = (str_number[:first_half])
                second_number = (str_number[first_half:])
                if first_number == second_number:
                    total = total + var_number

endtime = time.time()
print("The output is number: ", total);
print("Program took: ", endtime-starttime, " seconds");