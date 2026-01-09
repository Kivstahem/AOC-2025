# D9, find the largest red area square from the list of coords [x,y]
import math
import time
starttime = time.time()
debug = False

def load_data(filename):
    array = [];
    with open(filename) as file:
        for line in file:
            line = line.strip().split(',');
            array.append([int(line[0]), int(line[1])]) # create a X,Y,Z,INDEX layout. 
    return array

def area_calc(xyz1,xyz2):
    # Calculate the straight line distance from the first set of coords to the second set of coords
    return (abs(xyz2[0]-xyz1[0])+1)*(abs(xyz2[1]-xyz1[1])+1)

def find_largest_area(array):
    max_area = 0;
    for x in range(len(array)):
        for y in range(x+1, len(array)):
            area = area_calc(array[x],array[y])
            if area > max_area:
                max_area = area;
    return max_area

## MAIN
filename = "input.txt" # correct answer: 4760959496
# filename = "input_test.txt" # correct answer 50 ([2,5];[11,1])
array = load_data(filename)
total = find_largest_area(array)

endtime = time.time()
print("The total sum is going to be: ", total)
print("The total time this code used is: ", endtime-starttime, "seconds");