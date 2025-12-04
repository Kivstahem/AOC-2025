import time
import math

start = time.time()

initial = 50;
maxDial = 99;
minDial = 0;
goalLocaltion = 0;
dial_location = initial;

passcode = 0;

def dial(dial_current, number):
    new_dial_mod = (dial_current+number)%(maxDial+1);
    return new_dial_mod

def dial_part_two(dial_current, number):
    new_location = (dial_current+number)%(maxDial+1); # known working to give the correct new dial location    
    old_location = dial_current;
    transistions = 0
    full_loops = 0
    partial_loops = 0
    
    full_loops = abs(number)//100 # this does the full loops correctly I think?    

    if number < 0: #LEFT
        if new_location > old_location:
            partial_loops = 1
        if new_location == 0:
            partial_loops = 1
        if old_location == 0:
            partial_loops = 0
    else:       # RIGHT (WORKING CORRECT)
        if new_location < old_location:
            partial_loops = 1
    transistions = full_loops + partial_loops
    return new_location, transistions

with open("input.txt") as f:
    for x in f:
        print("SOL-------------------------");
        print("No processing [begin]", x) # prints LXXX or RXXX (first have to seperate)
        print("The initial location of the dial: ", dial_location);
        direction = ''.join(filter(str.isalpha, x));
        number = int(''.join(filter(str.isdigit, x)));
        if direction == "L": # not handeling the exceptions
            dial_location, transistions = dial_part_two(dial_location, -number);
            passcode = passcode + transistions;  
        else:
            dial_location, transistions = dial_part_two(dial_location, number);
            passcode = passcode + transistions;
        print(dial_location);
        # if dial_location == 0:  
            # passcode = passcode + 1; 
        print("Everything processed, intial MSG: ", x, "Direction: ", direction, "dial location: ", dial_location, "transistions: ", transistions, "passcode: ", passcode);
        print("EOL------------------------");
        

end = time.time()
print("Final passcode", passcode, "in ",end-start, "seconds");
print("INITIAL LOCATION SHOULD BE 50 IT IS: ", initial);