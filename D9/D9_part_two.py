# D9, find the largest red area square from the list of coords [x,y]
# The square must ONLY contain red / green squares.
# the green squares connect between the red squares and once a section is encircled it is filled with green/red squares
import time
starttime = time.time()
debug = False

def load_data(filename):
    array = [];
    with open(filename) as file:
        for line in file:
            line = line.strip().split(',');
            array.append((int(line[0]), int(line[1]))) # create a X,Y,Z,INDEX layout. 
    return array

def create_field(array):
    # create the valid field on which the system can check if it is valid
    red = []
    # create the play_field
    play_field = set()
    red = [(x,y) for x,y in array]
    for x,y in red:
        play_field.add((x,y));
    # print(play_field)
    for x in range(len(red)):
        loc1 = red[x]
        for y in range(x+1, len(red)):
            loc2 = red[y]
            if loc1 != loc2: 
                # find two coörds if they allign on x/y make the points inbetween 1
                if loc1[1] == loc2[1]: #allignment on Y axis (vertical)
                    x_start,x_end = sorted((loc1[0],loc2[0]));
                    y = loc1[1]
                    for x in range(x_start, x_end+1):
                        play_field.add((x,y))
                if loc1[0] == loc2[0]: # allignment on X axis (horizontal)
                    x = loc1[0];
                    y_start,y_end = sorted((loc1[1],loc2[1]));
                    for y in range(y_start, y_end + 1):
                        play_field.add((x,y))
    # We still have to fill the inside of the field
    
    #     # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa
    # xs = [x for x, y in play_field]
    # ys = [y for x, y in play_field]
    # max_x = max(xs)
    # max_y = max(ys)
    # test = [[0] * (max_x + 1) for _ in range(max_y + 1)]
    # for x, y in play_field:
    #     test[y][x] = 1
    # for row in test:
    #     print(row)
    
    ys_in_field = sorted({y for x, y in play_field})

    for y in ys_in_field:
        # Get all Xs for this Y
        matching_xs = sorted([x for x in play_field if x[1] == y])
        # print(f"Y={y}, matching Xs: {matching_xs}")
        # Fill in missing Xs between min and max
        # x_start, x_end = matching_xs[0][0], matching_xs[-1][0]
        # for x in range(x_start, x_end + 1):
        #     play_field.add((x, y))
        x_old = matching_xs[0][0];
        flipped = False;
        for x in range(1,len(matching_xs)):
            x_new = matching_xs[x][0];
            # print(x_new, x_old)
            if x_new-x_old != 1:
                # print("there is a gap flipped = ", flipped)
                # there was an increase of more than 1
                if flipped == False:
                    # add these new entities as flip hadn't happened before (so inbetween #)
                    flipped = True;
                    for x_loc in range(x_old,x_new+1):
                        # print("adding", x_loc, y)
                        play_field.add((x_loc,y));
                        x_old = x_new
                elif flipped == True:
                    # ignore, flip already happened
                    flipped = False;
                    x_old = x_new
            else:
                x_old = x_new;
    
    # # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa
    # xs = [x for x, y in play_field]
    # ys = [y for x, y in play_field]
    # max_x = max(xs)
    # max_y = max(ys)
    # test = [[0] * (max_x + 1) for _ in range(max_y + 1)]
    # for x, y in play_field:
    #     test[y][x] = 1
    # for row in test:
    #     print(row)
    return play_field, red







def area_calc(xyz1,xyz2):
    # Calculate the straight line distance from the first set of coords to the second set of coords
    return ((abs(xyz2[0]-xyz1[0])+1)*(abs(xyz2[1]-xyz1[1])+1))

def find_largest_area(array, play_field):
    max_area = 0;
    for x in range(len(array)):
        for y in range(x+1, len(array)):
        # for y in range(len(array)):
            xyz1 = array[y];
            xyz2 = array[x];
            area = area_calc(xyz1, xyz2)
            if area >= max_area:
                if area_valid(xyz1,xyz2, play_field):
                    max_area = area;
                    print(xyz1,xyz2, max_area)
    return max_area

def area_valid(xyz1,xyz2, play_field):
    # x_cords
    if xyz1[0] < xyz2[0]:
        x_start = xyz1[0];
        x_end   = xyz2[0];
    else:
        x_start = xyz2[0];
        x_end   = xyz1[0];
    # y-cords
    if xyz1[1] < xyz2[1]:
        y_start = xyz1[1];
        y_end   = xyz2[1];
    else:
        y_start = xyz2[1];
        y_end   = xyz1[1];
    # check Y
    for y in range(y_start, y_end + 1):
        if ((x_start,y) not in play_field):
            return False;
        if ((x_end,y) not in play_field):
            return False
    # check X
    for x in range(x_start, x_end + 1):
        if ((x,y_start) not in play_field):
            return False;
        if ((x,y_end) not in play_field):
            return False;
    return True;


## MAIN
filename = "input.txt" # wrong answer: 186554000
# filename = "input_test.txt" # correct answer 30
print("load data start");
array = load_data(filename)
print("create field start")
play_field, red = create_field(array)
print("find largest area start")
total = find_largest_area(red, play_field)
endtime = time.time()
print("The total sum is going to be: ", total)
print("The total time this code used is: ", endtime-starttime, "seconds");