# D4

# import an playing field and find how many rolls(@) you can pick up.
# They can only be accessed from the locations marked as (.) and in the fewer then 4 (@) must be around the (.) in the 8 spots
# . . .                     . . . 
# @ . . cannot pick up >3   . . . Can pick up
# @ @ @                     @ @ @

import time
import copy
starttime = time.time()
total = 0

MAX_ROLLS = 4 # three surrounding rolls, also counting the one in the centre

def create_playfield(filename):
    # Loading in the play field and adding a border of E (edge) around it
    global play_field;
    global modified_play_field;
    play_field = [];
    with open(filename) as file:
        for line in file:
            play_field.append("EE"+line.strip("\n")+"EE\n");
    edge = "E" * (len(play_field[1])-1);
    play_field.insert(0,edge+"\n");
    play_field.insert(0,edge+"\n");
    play_field.insert(len(play_field), str(edge)+"\n");
    play_field.insert(len(play_field), str(edge)+"\n");
    # play_field = list(play_field);
    # print(play_field)
    modified_play_field = play_field.copy();
    # modified_play_field = play_field;

    
def replacer(x_cord,y_cord,character):
    # print("Y, X", y_cord, x_cord);
    temp_str = list(modified_play_field[y_cord]);
    # print("Replacing: ", temp_str[y_cord], "with ", character);
    temp_str[x_cord] = character;
    temp_str = "".join(temp_str);
    modified_play_field[y_cord] = temp_str; 
    
def main_replacer(x_cord,y_cord,character):
    # print("Y, X", y_cord, x_cord);
    temp_str = list(play_field[y_cord]);
    # print("Replacing: ", temp_str[y_cord], "with ", character);
    temp_str[x_cord] = character;
    temp_str = "".join(temp_str);
    play_field[y_cord] = temp_str; 

def check_valid(x, y):
    # print("This should be @", play_field[y][x])
    amount_rolls  = 0;
    if modified_play_field[y][x] == "X":
        # This one has already been checked
        return 0;
    # print("    print("[x,y] OG", x,y)Start checking original coörds [x,y]", x,y);
    ## Check the 8 surrounding squares to see if there are more then 3 rolls
    for y_local in range(y-1, y+2):
        for x_local in range(x-1, x+2): # range doesn't include upper bound
            # print("[x,y] local", x_local,y_local, play_field[y_local][x_local], amount_rolls)
            if x == x_local and y == y_local:
                continue # Skip this entry 
            if play_field[y_local][x_local] == "@":
                amount_rolls = amount_rolls + 1;
                if amount_rolls >= MAX_ROLLS:
                    return 0; # too many, invalid

    replacer(x,y, "X");
    return 1
    
def check_four_acces(x,y):
    picked_up     = 0;
    # check_spots_x = [1, -1, 0, 0];
    # check_spots_y = [0, 0, 1, -1];
    if play_field[y][x] != ".":
        return picked_up;
    # print("Starting check four access");
    for y_local in range(y-1, y+2):
        for x_local in range(x-1, x+2): # range doesn't include upper bound
            if play_field[y_local][x_local] == "@":
                if y == y_local and x == x_local:
                    continue;
                ret_code = check_valid(x_local,y_local);
                if ret_code == 1:
                    picked_up = picked_up + 1;
    # print("Picked ", picked_up, " this many up")
    return picked_up

## MAIN
total_rolls = 0;
create_playfield("input.txt");

LOOP = True

while LOOP == True:
    for y in range(2, len(play_field)-2):
        for x in range(2, len(play_field[1])-3):
            # print(play_field[y][x])
            if play_field[y][x] == ".": # spot to check
                total_rolls = total_rolls + check_four_acces(x, y);
    ## First loop is completed, replace the X with . to indicate the new spots
    updated_field = False
    for y in range(2, len(play_field)-2):
        for x in range(2, len(play_field[1])-3):
            # print(play_field[y][x])
            if modified_play_field[y][x] == "X": # spot to check
                main_replacer(x,y,".");
                updated_field = True;
    modified_play_field = play_field.copy();
    if updated_field == False:
        LOOP = False;


# write file to test output (DEBUG)
with open("output.txt", 'w') as file:
    for line in modified_play_field:
        file.write(str(line))
    for line in play_field:
        file.write(str(line))

endtime = time.time()
print("The output is number: ", total_rolls);
print("Program took: ", endtime-starttime, " seconds");
# print(play_field)
