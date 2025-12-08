# given list is in X Y Z cöords
# Your list contains many junction boxes
# connect together the 1000 pairs of junction boxes which are closest together. 
# Afterward, what do you get if you multiply together the sizes of the three largest circuits?
import math
import time
starttime = time.time()
debug = False
partTwo = True
def load_data(filename):
    array = [];
    with open(filename) as file:
        for line in file:
            line = line.strip().split(',');
            array.append([int(line[0]), int(line[1]), int(line[2])]) # create a X,Y,Z,INDEX layout. 
    return array

def straight_line_distance(x1,y1,z1,x2,y2,z2):
    # Calculate the straight line distance from the first set of coords to the second set of coords
    return math.sqrt(pow(x2-x1,2)+pow(y2-y1,2)+pow(z2-z1,2))

def find_shortest_distance(array, amount_connections_needed):
    current_connections_made = 0;
    distance_calculated = []
    for x in range(len(array)):
        for y in range(x+1, len(array)):
            # if item_1 != item_2:
            item_1 = array[x]
            item_2 = array[y]
            distance = straight_line_distance(item_1[0],item_1[1],item_1[2],item_2[0],item_2[1],item_2[2])
            distance_calculated.append([distance, item_1, item_2])
    
    groups = list()
    groups = [[point] for point in array];
    while len(groups) > 1:
        # print(smallest_distance[current_connections_made]);
        smallest_distance = min(distance_calculated, key=lambda x: x[0])
        distance_calculated.remove(smallest_distance)
        # print(smallest_distance)
        
        # check if the value is in the list
        xyz_1 = smallest_distance[1];
        xyz_2 = smallest_distance[2];
        # print(xyz_1)
        # print(xyz_2)
        last_X = [xyz_1[0], xyz_2[0]]
        # distance is now saved, we can delete the original entry in the thing we check
        
        
        # checking if the xyz coords are already in the list.
        # [1] xyz_1/2 not in the list -> add as a new group
        # [2] xyz_1/2 one of two in the list -> add the other to the group
        # [3] xyz_1/2 both in the list, but different groups
        # [4] both are in the list :( do NOT increment the counter
        index_1 = -1 #column
        index_2 = -1 
        # [xyz, xyz, xyz] -> row
        # [xyz, xyz, xyz]
        # [xyz, xyz, xyz] 
        #   |
        #  \_/ column
        for col, row in enumerate(groups):
            if xyz_1 in row:
                index_1 = col;
            if xyz_2 in row:
                index_2 = col;
                
        connection_made = False
        # we first check IF the values are in the list
        # if index_1 == -1 and index_2 == -1:
        #     groups.append([xyz_1,xyz_2])
        # elif index_1 != -1 and index_2 == -1:
        #     # xyz_2 not in the list yet
        #     groups[index_1].append(xyz_2);
        # elif index_2 != -1 and index_1 == -1:
        #     # xyz_1 not in the list yet
        #     groups[index_2].append(xyz_1);
        # else:
        if index_1 != -1 and index_2 != -1:
            # both entries are in the list
            if index_1 != index_2:
                # They are NOT in the same column so we have to add the two groups together!
                groups[index_1].extend(groups[index_2]);
                del groups[index_2]

        current_connections_made += 1; # add one every loop -> every time a new connection is formed
    groups = sorted(groups, key=len, reverse=True) #groups.sort(reverse=True)
    if debug:
        for i in range(len(groups)):
            print(len(groups[i]),": ",groups[i])
    # print(groups)
    # total = int(len(groups[0]))*int(len(groups[1]))*int(len(groups[2]));
    # total = int(groups[1][0][0])*int(groups[2][0][0])
    # print(last_X)
    total = last_X[0]*last_X[1];
    return total                

## MAIN

filename = "input.txt" # 330786 correct answer part 1
# filename = "input_test.txt" # correct answer 40 part 2: 25272
array = load_data(filename)
total = find_shortest_distance(array, len(array))

endtime = time.time()
print("The total sum is going to be: ", total)
print("The total time this code used is: ", endtime-starttime, "seconds");
