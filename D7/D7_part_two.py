# The teleporter is busted!
# S (tachyon) always move DOWNWARDS and pass freely through space (.)
# However, if a splitter (^) is encountered the beam is split into two 
# Begin only one S and in total 21 times is the bem split
# .......S.......
# .......|.......
# ......|^|......
# ......|.|......
# .....|^|^|.....
# .....|.|.|.....
# ....|^|^|^|....
# ....|.|.|.|....
# ...|^|^|||^|...
# ...|.|.|||.|...
# ..|^|^|||^|^|..
# ..|.|.|||.|.|..
# .|^|||^||.||^|.
# .|.|||.||.||.|.
# |^|^|^|^|^|||^|
# |.|.|.|.|.|||.|

import time
starttime = time.time()
total = 0
global play_field;

def create_playfield(filename):
    # Loading in the play field and adding a border of E (edge) around it
    global play_field;
    play_field = [];
    with open(filename) as file:
        for line in file:
            # play_field.append(line.strip("\n"));
            play_field.append(line);
            
def replacer(x_cord,y_cord,character):
    temp_str = list(play_field[y_cord]);
    temp_str[x_cord] = character;
    temp_str = "".join(temp_str);
    play_field[y_cord] = temp_str;
    
def write_file(filename, array):
    # write file to test output (DEBUG)
    with open(filename, 'w') as file:
        for line in array:
            file.write(str(line))


def check_row(y, length_play_field):
    local_total_beamsplit = 0;
    for x in range(length_play_field):
        if play_field[y][x] == "^":
            # Found the splitter check if ABOVE is a beam
            local_total_beamsplit += splitter(x,y);
        elif play_field[y-1][x] == "|":
            replacer(x,y,"|");
    return local_total_beamsplit
            
    
def find_start(length_play_field):
    y = 0;
    for x in range(length_play_field):
        if play_field[y][x] == "S":
            # if play_field[y+1][x] == ".":
                # replacer(x,y+1,"|");
            # SHOULD CALL REPLACER TO PLACE A BEAM
            return x,y;
    print("FAILED TO FIND THE START")
    
def splitter(x,y):
    # call replacer to replace . with |
    # y = height
    # x - 1 left, x + 1 right
    if play_field[y-1][x] == "|" or play_field[y-1][x] == "S":
        replacer(x-1,y,"|");
        replacer(x+1,y,"|");
        return 1 # return 1 if there was a valid BEAMSPLIT
    return 0;

def recursive_dimension_splitter(x,y, height_play_field):
    # print("Calling recursive dimension splitter now at y: ",y)
    # print("Current loc: ",play_field[y][x])
    # print("Low below: ", play_field[y+1][x]);
    # given X,Y are the previous LAST position
    temp_total_dimension_split = 0;
    # Base case, check for last row
    if y == height_play_field:
        # print("We have reache the bottom!");
        temp_total_dimension_split += 1;
        return temp_total_dimension_split
    elif play_field[y][x] == "^":
        print("Something went wrong and I started on a ^?? cöords are [x,y]: ",x,y);
    elif play_field[y+1][x] == ".":
        temp_total_dimension_split += recursive_dimension_splitter(x,y+1,height_play_field);
    elif play_field[y+1][x] == "^":
        temp_total_dimension_split += recursive_dimension_splitter(x-1,y+1,height_play_field);
        temp_total_dimension_split += recursive_dimension_splitter(x+1,y+1,height_play_field);
    return temp_total_dimension_split

def path_splitter(x_start,y_start,height_playfield,length_play_field):
    # okay let's maybe do it smarter
    # print("height: ", height_play_field);
    # print("length: ", length_play_field)
    temp_play_field = [[0 for col in range(length_play_field)] for row in range(height_play_field)]
    # we start at x/y_start:
    temp_play_field[y_start][x_start] = 1; ## One timeline starts HERE
    for y in range(1,height_play_field):
        temp_play_field = check_row_quantum(y, length_play_field, temp_play_field);
    
    temp = ""
    for i in range(len(temp_play_field)):
        temp += str(temp_play_field[i]).replace("[", "").replace("]", "").replace(",", "").replace(" ", "")+"\n"
    write_file("output.txt", temp);
    print(temp_play_field[height_play_field-1])
    return sum(temp_play_field[height_play_field-1])
    
def check_row_quantum(y, length_play_field, temp_play_field):
    for x in range(length_play_field):
        if play_field[y][x] == "^":
            # Found the splitter check if ABOVE is a beam
            temp_play_field[y][x-1] += temp_play_field[y-1][x];
            temp_play_field[y][x+1] += temp_play_field[y-1][x];
        elif temp_play_field[y-1][x] != 0:
            # print("Found a non zero value above me!");
            temp_play_field[y][x] += temp_play_field[y-1][x];
    return temp_play_field





## MAIN # PART 2
global total_beamsplit;
global total_dimensions;
total_dimensions = 0;
total_beamsplit = 0;
filename = "input.txt";

create_playfield(filename)
length_play_field = len(play_field[0].strip("\n")); 
height_play_field = len(play_field)
x_start,y_start = find_start(length_play_field);
# total_dimensions += recursive_dimension_splitter(x_start,y_start,length_play_field-1); # surprise surprise recursive blows up :(

total_dimensions = path_splitter(x_start, y_start, height_play_field, length_play_field);


# write_file("output.txt", play_field); # write output (DEBUG)


print("The total beamsplits are: ", total_beamsplit, "and the total amount of dimensions: ", total_dimensions);