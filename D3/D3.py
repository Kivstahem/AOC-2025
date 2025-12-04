import time
import math

starttime = time.time()

total_joltage = 0;

# def dial(dial_current, number):
#     new_dial_mod = (dial_current+number)%(maxDial+1);
#     return new_dial_mod

with open("input.txt") as file:
    for line in file:
        print("SOL-------------------------");
        print("The battery bank: ", line);
        str_number     = line.strip();
        max_first      = 0;
        max_second     = 0;
        max_first_ind  = 0;
        max_second_ind = 0;
        index          = len(str_number);
        for x in reversed(str_number):
            if max_first == 9 and max_second == 9:
                continue;
            # print(x);
            if int(x) >= max_first and index != len(str_number):
                if max_second < max_first:
                    # if a new value that is larger is found, offload it onto the second entry
                    max_second = max_first;
                    max_second_ind = max_first_ind;
                max_first = int(x);
                max_first_ind = index;
                
            if int(x) > max_second and index != max_first_ind and max_first_ind < index:
                max_second = int(x);
                max_second_ind = index;
            # reversing through the list so DECREASING the index
            index = index - 1;
        total_joltage = total_joltage + int(str(max_first)+str(max_second));
        print("The best battery combination is: ", int(str(max_first)+str(max_second)));
        print("EOL------------------------");
        

endtime = time.time()
print("The final joltage is: ", total_joltage);
print("Program took: ", endtime-starttime, " seconds");