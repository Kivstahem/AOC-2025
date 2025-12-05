#D5, check if an item is fresh via it's ID.
# 1. The first range's are given these are considered FRESH
# 2. blank line to seperate the input
# 3. Items to check are given

import time
starttime = time.time()

def load_data(filename):
    # Loading in the play field and adding a border of E (edge) around it
    inDate  = list();
    toCheck = list();
    with open(filename) as file:
        for line in file:
            # fresh item range
            if line.__contains__('-'):
                line = line.split('-');
                start = int(line[0]);
                end   = int(line[1]);
                # inDate.__add__(start,end)
                inDate.append([start, end])            
            elif line == "\n":
                # ignore
                continue
            else:
                toCheck.append(int(line)) 
                # continue
                
    return inDate, toCheck

import numpy as np
def merge_interval(interval):
    interval = np.array(interval);
    interval.sort(axis=0);
    start_bounds = interval[:,0]
    end_bounds   = interval[:,1]
    start_bounds_filter = ~np.convolve(end_bounds >= np.concatenate([start_bounds[1:], [np.inf]]), [False, True], mode='same')
    end_bounds_filter = np.flip(~np.convolve(np.flip(start_bounds <= np.concatenate([[-np.inf], end_bounds[:-1]])), [False, True], mode='same'))
    sorted_interval = np.vstack([start_bounds[start_bounds_filter], end_bounds[end_bounds_filter]]).T.tolist()
    return sorted_interval


def binary_search(array, x):
    #slighlty modified binary search as intervals are utilised
    low = 0;
    high = len(array)-1;
    while low <= high:
        middle = low + (high - low)//2
        # print("Value to find", x,"Middle", middle, "array[middle][0]", array[middle][0], "array[middle][1]", array[middle][1]);

        if array[middle][0] <= x:
            # the array value is SMALLER then our WANTED entry
            if array[middle][1] >= x:
                # it fits between the interval so it is a valid entry
                return True;
            low = middle + 1;
        elif array[middle][0] >= x:
            # The array interval entry is LARGER then our wanted entry

            high = middle - 1;
        else:
            return False;
    return False;

# MAIN
filename = "input.txt"
total_fresh = 0;
inDate, toCheck = load_data(filename);

# print(inDate)
inDate = merge_interval(inDate);
# print(inDate)
# print(toCheck)

for item in toCheck:
    # time to do a binary search  
    if binary_search(inDate, item):
        total_fresh = total_fresh + 1;
        
# now to see the total amount of ingredients considered to be fresh
total_items_fresh = 0;
for item in inDate:
    total_items_fresh = total_items_fresh + item[1] - item[0] + 1; # lower bound is also a VALID fresh item
    

endtime = time.time()
print("total fresh items: ", total_fresh, "and the total amount of items that are fresh are: ", total_items_fresh);
print("Program took: ", endtime-starttime, " seconds");
# print(play_field)
