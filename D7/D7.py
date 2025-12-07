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
            if play_field[y-1][x] == ".":
                replacer(x,y+1,"|");
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




## MAIN
global total_beamsplit;
total_beamsplit = 0;
create_playfield("input_test.txt")
# create_playfield("input.txt")
length_play_field = len(play_field[0])-1; 
x,y = find_start(length_play_field);
# print("Start S location is: ",x,y);
for y in range(len(play_field)):
    total_beamsplit += check_row(y, length_play_field);
# total_beamsplit += check_row(2, length_play_field);




write_file("output.txt", play_field); # write output (DEBUG)


print("The total beamsplits are: ", total_beamsplit);