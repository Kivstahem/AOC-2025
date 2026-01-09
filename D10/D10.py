# input:
# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# end goal lights [0,1,2,3]. Find the least button presses to turn on the middle two lights.
# add the smallest amount of button presses to total
# test case answer: 7

import time
from collections import deque
from z3 import *
starttime = time.time()
debug = False

def load_data(filename):
    buttons   = [];
    lights  = [];
    joltage = [];
    with open(filename) as file:
        for line in file:
            line = line.strip().split();
            # print(line)
            lights.append(line[0])
            
            jolts = line[-1].strip("{}").split(",")
            jolts = list(map(int, jolts))
            joltage.append(jolts)
            
            temp = []
            for var in line[1:-1]:
                number = var.strip("()")
                temp.append(list(map(int,number.split(","))))
            buttons.append(temp)

            # print("This is the lights",lights)
            # print("This is the array",buttons);
            # print("This is the joltage",joltage)
    return lights, buttons, joltage

def process_data(lights, buttons, joltage):
    # we currently do not care about joltage so let's ignore it for a bit
    length_array = len(buttons);
    local_total_P1 = 0;
    local_total_P2 = 0;
    for i in range(length_array):
        # print("loop start");
        temp = BFS(lights[i], buttons[i]);
        # print("P1:", temp)
        local_total_P1 += temp;
        # print("loop end local_total: ", temp)
    # BFS_P2(lights[0], buttons[0], joltage[0]);
    for i in range(length_array):   
        # temp =  BFS_P2(buttons[i], joltage[i]);
        temp = Z3(buttons[i], joltage[i])
        # print("P2:",temp)
        local_total_P2 += temp;
    
    return local_total_P1, local_total_P2;

def BFS(light_goal, button_presses):
    # https://www.geeksforgeeks.org/python/python-program-for-breadth-first-search-or-bfs-for-a-graph/
    
    # create the start state, and target state
    # start_state = int("0000",2);
    start_state = 0;
    target_state = light_goal.strip("[]").replace(".", "0").replace("#", "1");
    target_state = int(target_state[::-1],2) #oeps
    # print(target_state)
    
    # convert the button mask to actually usable binary masks
    button_mask = [];
    for button in button_presses:
        mask = 0
        for idx in button:
            # mask |= (1 << (num_lights - 1 - idx))
            mask |= (1<<idx)
        button_mask.append(mask)
    
    # target_state = 0b1111 ^ target_state;
    queue = deque()
    queue.append((start_state, 0))
    visited = {start_state}
    
    while queue:
        state, dist = queue.popleft();
        
        # base case
        if state == target_state:
            return dist # found the max number of button presses needed
        
        for mask in button_mask:
            next = state ^ mask; #XOR
            if next not in visited:
                visited.add(next);
                queue.append((next, dist+1));
    print("fuck i didn't find it")
    return 0;

def BFS_P2(button_presses, joltage_input):
    # https://www.geeksforgeeks.org/python/python-program-for-breadth-first-search-or-bfs-for-a-graph/
    # process the joltage too slow
    # pos
    joltage_target = joltage_input;
    joltage_target = tuple(joltage_target)
    joltage_start  = [0]*len(joltage_target);
    joltage_start  = tuple(joltage_start)
    # print("here?",joltage_input, joltage_target, joltage_start)
    length = len(joltage_target)

    # convert the button mask to actually usable binary masks
    button_mask = [];
    for button in button_presses:
        mask = [0]*length;
        for idx in button:
            mask[idx] = 1
        button_mask.append(tuple(mask))
    
    # target_state = 0b1111 ^ target_state;
    queue = deque()
    queue.append((joltage_start, 0))
    visited = {joltage_start}
    
    while queue:
        state, dist = queue.popleft();        
        # base case
        if state == joltage_target:
            return dist # found the max number of button presses needed
        
        for mask in button_mask:
            next = list(state);
            valid = True

            for i in range(length):
                next[i] += mask[i]
                if next[i] > joltage_target[i]:
                    valid = False
                    print("invalid")
                    break
            if not valid:
                continue;
            
            temp = tuple(next);
            if temp not in visited:
                visited.add(temp);
                queue.append((temp, dist+1));
    print("fuck i didn't find it")
    return 0;

def Z3(button_presses, joltage_target):
    # https://ericpony.github.io/z3py-tutorial/guide-examples.htm fucking magie dank je reddit
    # add the lengths
    length_target = len(joltage_target)
    length_array = len(button_presses)

    # convert the button mask to actually usable binary masks
    button_mask = [];
    for button in button_presses:
        mask = [0]*length_target;
        for idx in button:
            mask[idx] = 1
        button_mask.append(tuple(mask))

    opt = Optimize()

    # tracking button presses
    x = []
    # var per button
    for i in range(length_array):
        var = Int("x" + str(i))  #x0,x1,x2
        x.append(var)
    # button press >= 0
    for var in x:
        opt.add(var >= 0)

    # track how many times button is pressed
    for j in range(length_target):
        terms = []
        for i in range(length_array):
            temp = x[i] * button_mask[i][j]
            terms.append(temp)
        constraint = Sum(terms) == joltage_target[j] # this should become equal
        opt.add(constraint)

    total = Sum(x)
    opt.minimize(total) # magic shit

    if opt.check() != sat:
        # we done goofed
        return None
    
    model = opt.model();
    total_presses = 0
    for var in x:
        value = model[var].as_long()  # Z3 to python int
        total_presses += value
    return total_presses




def main():
    starttime = time.time();
    totalP1 = 0;
    totalP2 = 0;
    filename = "input.txt"; #P1: 401, P2: ?
    # filename = "input_test.txt"; # P1: 7, P2 33
    lights, buttons, joltage = load_data(filename);
    totalP1, totalP2 = process_data(lights, buttons, joltage);
    
    print("The total output is P1: ", totalP1, "P2: ", totalP2);
    stoptime = time.time()
    print("Total time:",stoptime-starttime,"seconds");



if __name__=="__main__":
    main()
